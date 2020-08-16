from django.shortcuts import render,render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import csv, io
from math import pi
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .models import Support_Team
from .models import Audit
from .models import HR

from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def home(request):
  return render(request, 'home.html')

def register(request):
  form = UserRegisterForm()
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, 'Account has been created!')
      return redirect('home')
    else:
      form = UserRegisterForm()
  return render(request, 'register.html', {'form': form})
  
@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def graph(request):

  data = HR.objects.all()
  leaves = {1:0}
  for item in data:
    leave = item.leaves_applied
    if leave in leaves.keys():
      leaves[leave] = leaves[leave] + 1
    else:
      leaves[leave] = 1
  coord = dict(sorted(leaves.items()))
  plot = figure(title = 'Line Graph',x_axis_label = 'X-Axis', y_axis_label = 'Y-Axis', plot_width = 400, plot_height = 400)
  x = list(coord.keys())
  y = list(coord.values())
  print(x)
  print(y)
  plot.line(x,y, line_width = 2)

  script,div = components(plot)
  
  return render(request,'bokeh1.html', {'script':script, 'div':div})

def scatterplot(request):

  plot = figure(plot_width=400, plot_height=400)
  plot.circle([1,2,3,4,5],[6,7,5,2,1],size=20,color="navy",alpha=0.5)
  script,div = components(plot)

  return render(request,'scatterplot.html',{'script':script,'div':div})

def bargraph(request):

  plot = figure(plot_width=400, plot_height=400)
  plot.vbar(x=[1,2,3,4,5],width=0.5,bottom=0, top = [1.2,2.5,3.7,2.9,4.8],color="firebrick")
  script,div = components(plot)

  return render(request,'bargraph.html',{'script':script,'div':div})

def piegraph(request):
  chart_colors = ['#44e5e2', '#e29e44', '#e244db',
                '#d8e244', '#eeeeee', '#56e244', '#007bff', 'black']

  x={'Yes':270,
    'No':180,
    'Maybe':70,
    'idk':20}
  data = pd.Series(x).reset_index(name='value').rename(columns={'index':'choice'})
  data['angle'] = data['value']/data['value'].sum() * 2*pi
  data['color'] = chart_colors[:len(x)]

  plot= figure(plot_height=350,title="Pie Chart",toolbar_location=None,
           tools="hover", tooltips="@choice: @value", x_range=(-0.5, 1.0))
  plot.wedge(x=0, y=1, radius=0.4,
        start_angle=0, end_angle=0,
        line_color="white",fill_color='color', source=data)

  plot.axis.axis_label=None
  plot.axis.visible=False
  plot.grid.grid_line_color = None
  script,div = components(plot)

  return render(request,'piegraph.html',{'script':script,'div':div})