from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView,DetailView,View
from . models import Course,Enroll,CourseContent,Category,SubCategory
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


# Create your views here.
class CourseList(ListView):
     template_name = "course/course_list.html"  
     def get(self, request, *args, **kwargs):
          category=Category.objects.all()
          subcategory=SubCategory.objects.all()
          return HttpResponse(category)
          if request.GET.get('test'):
               return HttpResponse(request.GET.get('test'))
          else:
               queryset=Course.objects.all()
              
               return render(request, self.template_name, {'object_list': queryset})




class CourseDetailView(View):
     template_name = "course/course_detail.html" 
     def get(self, request, slug):
           
           queryset=Course.objects.get(slug=slug)
           data=Enroll.objects.filter(course_id=queryset.id).exists()
          #  return HttpResponse(data)
           return render(request, self.template_name, {'course': queryset,'enrolled':data})
     



@method_decorator(login_required, name='dispatch')
class EnrollStudent(View):
       def get(self, request, slug):
            course=Course.objects.get(slug=slug)
            hasEnrolled=Enroll.objects.filter(course=course,user=request.user).exists()
            if hasEnrolled == False:
               enroll= Enroll(course=course,user=request.user)
               enroll.save();
               messages.success(request, f"You are Succesfully Enrolled")
               return redirect('/course/'+slug)
            else:
               messages.success(request, f"You are already Enrolled")
               return redirect('/course/'+slug)

class CoursePlay(View):
      template_name = "course/course_play.html" 
      def get(self, request, slug):

           play=request.GET.get('play')
           if play:
               play=int(play)
           else:
               play=0
           course=Course.objects.get(slug=slug)
           hasEnrolled=Enroll.objects.filter(course=course,user=request.user).exists()
           if hasEnrolled == False:
               messages.success(request, f"Please Enroll First")
               return redirect('/course/'+slug)

           content=CourseContent.objects.filter(course=course.id)
           
           
           return render(request, self.template_name, {'course': course,'content':content,'play':play})




            
          



   
