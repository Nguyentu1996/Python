from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from api.customer.models import Hobbies,Profile,Skill
from api.customer.serializer import HobbiesSerializer,ProfileSerializer,SkillSerializer
# Create your views here.

class HobbiesList(generics.ListCreateAPIView):
    queryset = Hobbies.objects.all()
    serializer_class = HobbiesSerializer
class HobbiesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hobbies.objects.all()
    serializer_class = HobbiesSerializer
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
class SkillDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer