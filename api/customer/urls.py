from django.urls import path
from api.customer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('skill/',views.SkillList.as_view()),
    path('skill/<int:pk>/',views.SkillDetails.as_view()),
    path('hobbies/',views.HobbiesList.as_view()),
    path('hobbies/<int:pk>/',views.HobbiesDetails.as_view()),
     path('profile/',views.ProfileList.as_view()),
    path('profile/<:pk>/',views.ProfileDetails.as_view()),
]