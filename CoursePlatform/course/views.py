from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from . models import Course


# Create your views here.
class CourseList(ListView):
     model = Course
   
