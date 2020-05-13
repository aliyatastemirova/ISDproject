from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView,DetailView,View
from . models import Course,Enroll
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class CourseList(ListView):
     template_name = "course/course_list.html"  
     def get(self, request, *args, **kwargs):
          if request.GET.get('test'):
               return HttpResponse(request.GET.get('test'))
          else:
               queryset=Course.objects.all()
              
               return render(request, self.template_name, {'object_list': queryset})




class CourseDetailView(DetailView):
     model=Course
     template_name = "course/course_detail.html" 



@method_decorator(login_required, name='dispatch')
class EnrollStudent(View):
       def get(self, request, slug):
            course=Course.objects.get(slug=slug)
            hasEnrolled=Enroll.objects.filter(course=course,user=request.user).exists()
            if hasEnrolled == False:
               enroll= Enroll(course=course,user=request.user)
               enroll.save();
               return HttpResponse('Success')
            else:
               return HttpResponse('Already Enrolled')

            
          



   
