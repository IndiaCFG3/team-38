from django.contrib import admin
# Register your models here.
from .models import Profile
from .models import Support_Team
from .models import Audit
from .models import HR

admin.site.register(Profile)
admin.site.register(Support_Team)
admin.site.register(Audit)
admin.site.register(HR)