"""
URL configuration for job project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('rec_signin', views.rec_signin, name='rec_signin'),
    path('app_signin', views.app_signin, name='app_signin'),
    path('applicant', views.applicant, name='applicant'),
    path('recruiter', views.recruiter, name='recruiter'),
    path('postjob', views.postjob, name='postjob'),
    path('myjob', views.myjob, name='myjob'),
    path('viewjob', views.viewjob, name='viewjob'),
    path('delete_job', views.delete_job, name='delete_job'),
    path('edit_job/<int:job_id>', views.edit_job, name='edit_job'),
    path('application/<int:job_id>/', views.view_application, name='application'),
    path('apply_job', views.apply_job, name='apply_job'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)