from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, View
from .models import Course, Enroll, CourseContent, Category, SubCategory, CourseTag
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail


# Create your views here.
class CourseList(ListView):
    template_name = "course/course_list.html"

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        subcategory = SubCategory.objects.all()
        if request.GET.get('key'):
            key = request.GET.get('key')
            queryset = Course.objects.filter(Q(name__icontains=key))
        else:
            queryset = Course.objects.all()

        return render(request, self.template_name, {'object_list': queryset})


class CourseDetailView(View):
    template_name = "course/course_detail.html"

    def get(self, request, slug):
        queryset = Course.objects.get(slug=slug)
        # return HttpResponse(queryset.description)
        if request.user.is_authenticated:
            datas = Enroll.objects.filter(Q(course=queryset.id), Q(user=request.user)).exists()
        else:
            datas = False

        return render(request, self.template_name, {'course': queryset, 'enrolled': datas})


@method_decorator(login_required, name='dispatch')
class EnrollStudent(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        has_enrolled = Enroll.objects.filter(course=course, user=request.user).exists()
        if not has_enrolled:
            enroll = Enroll(course=course, user=request.user)
            enroll.save()
            messages.success(request, f"You are Succesfully Enrolled")
            return redirect('/course/' + slug)
        else:
            messages.success(request, f"You are already Enrolled")
            return redirect('/course/' + slug)


@method_decorator(login_required, name='dispatch')
class CoursePlay(View):
    template_name = "course/course_play.html"

    def get(self, request, slug):

        play = request.GET.get('play')
        if play:
            play = int(play)
        else:
            play = 0
        course = Course.objects.get(slug=slug)
        tag = CourseTag.objects.filter(course=course.id)
        has_enrolled = Enroll.objects.filter(course=course, user=request.user).exists()
        if not has_enrolled:
            messages.success(request, f"Please Enroll First")
            return redirect('/course/' + slug)

        content = CourseContent.objects.filter(course=course.id)

        context = {
            'content': content,
            'course': course,
            'play': play,
            'tag': tag
        }

        return render(request, self.template_name, context)
