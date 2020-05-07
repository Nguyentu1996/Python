from django.contrib import admin
from api.customer.models import Hobbies
from api.customer.models import Profile
from api.customer.models import Skill
# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Hobbies)