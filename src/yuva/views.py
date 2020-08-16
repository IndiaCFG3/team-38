from django.shortcuts import render,render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Profile
from .models import Support_Team
from .models import Audit
from .models import HR
# Create your views here.# one parameter named request
def profile_upload(request):    # declaring template
  template = "profile_upload.html"
  data = Profile.objects.all()# prompt is a context variable that can have different values      depending on their context
  prompt = {
      'order': 'Order of the CSV should be name, email, address,    phone, profile',
      'profiles': data    
            }
  # GET request returns the value of the data with the specified key.
  if request.method == "GET":
      return render(request, template, prompt)    
  csv_file = request.FILES['file']    # let's check if it is a csv file
  if not csv_file.name.endswith('.csv'):
    messages.error(request, 'THIS IS NOT A CSV FILE')    
  data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
  io_string = io.StringIO(data_set)
  next(io_string)
  for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    _, created = Profile.objects.update_or_create(
        name=column[0],
        email=column[1],
        address=column[2],
        phone=column[3],
        profile=column[4]
    )
  context = {}
  return render(request, template, context)

def st_upload(request):    # declaring template
  template = "profile_upload.html"
  data = Support_Team.objects.all()# prompt is a context variable that can have different values      depending on their context
  prompt = {
      'order': 'Order of the CSV should be name, email, address,    phone, profile',
      'profiles': data    
            }
  # GET request returns the value of the data with the specified key.
  if request.method == "GET":
      return render(request, template, prompt)    
  csv_file = request.FILES['file']    # let's check if it is a csv file
  if not csv_file.name.endswith('.csv'):
    messages.error(request, 'THIS IS NOT A CSV FILE')    
  data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
  io_string = io.StringIO(data_set)
  next(io_string)
  for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    _, created = Support_Team.objects.update_or_create(
        candidate_id = column[0],
        name = column[1],
        email = column[2],
        batch_id = column[3],
        enrolled_course = column[4],
        enrolled_date = column[5],
        attendance = column[6],
        course_status = column[7],
        placement_status = column[8]
    )
  context = {}
  return render(request, template, context)

def audit_upload(request):    # declaring template
  template = "profile_upload.html"
  data = Audit.objects.all()# prompt is a context variable that can have different values      depending on their context
  prompt = {
      'order': 'Order of the CSV should be name, email, address,    phone, profile',
      'profiles': data    
            }
  # GET request returns the value of the data with the specified key.
  if request.method == "GET":
      return render(request, template, prompt)    
  csv_file = request.FILES['file']    # let's check if it is a csv file
  if not csv_file.name.endswith('.csv'):
    messages.error(request, 'THIS IS NOT A CSV FILE')    
  data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
  io_string = io.StringIO(data_set)
  next(io_string)
  for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    _, created = Audit.objects.update_or_create(
        center_id = column[0],
        city = column[1],
        student_count = column[2],
        staff_count = column[3],
        students_joined = column[4],
        students_completed = column[5],
        students_dropped = column[6],
        rating = column[7]
    )
  context = {}
  return render(request, template, context)

def hr_upload(request):    # declaring template
  template = "profile_upload.html"
  data = HR.objects.all()# prompt is a context variable that can have different values      depending on their context
  prompt = {
      'order': 'Order of the CSV should be name, email, address,    phone, profile',
      'profiles': data    
            }
  # GET request returns the value of the data with the specified key.
  if request.method == "GET":
      return render(request, template, prompt)    
  csv_file = request.FILES['file']    # let's check if it is a csv file
  if not csv_file.name.endswith('.csv'):
    messages.error(request, 'THIS IS NOT A CSV FILE')    
  data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
  io_string = io.StringIO(data_set)
  next(io_string)
  for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    _, created = HR.objects.update_or_create(
          employee_id = column[0],
          employee_name = column[1],
          employee_phone = column[2],
          employee_email = column[3],
          manager_id = column[4],
          doj = column[5],
          employee_status = column[6],
          leaves_applied = column[7],
    )
  context = {}
  return render(request, template, context)

def graph(request):

  data = HR.objects.all()
  leaves = {1:0}
  for item in data:
    leave = item.leaves_applied
    if leave in leaves.keys():
      leaves[leave] = leaves[leave] + 1
    else:
      leaves[leave] = 1

  plot = figure(title = 'Line Graph',x_axis_label = 'X-Axis', y_axis_label = 'Y-Axis', plot_width = 400, plot_height = 400)
  x = list(leaves.keys())
  y = list(leaves.values())
  print(x)
  print(y)
  plot.line(x,y, line_width = 2)

  script,div = components(plot)
  
  return render(request,'bokeh1.html', {'script':script, 'div':div})