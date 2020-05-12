from django.conf import settings
from django.conf.urls.static import static
from course.views import CourseList
from django.urls import path
from django.conf import settings

urlpatterns=[

  
   path('course/', CourseList.as_view()),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

