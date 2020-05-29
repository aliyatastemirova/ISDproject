from django.conf import settings
from django.conf.urls.static import static
from course.views import CourseList, CourseDetailView, EnrollStudent, CoursePlay
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('course/', CourseList.as_view()),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course-detail'),
    path('enroll/<slug:slug>/', EnrollStudent.as_view()),
    path('course/<slug:slug>/play/', CoursePlay.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
