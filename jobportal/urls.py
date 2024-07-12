from django.contrib import admin
from django.urls import path,include
from job.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('admin_login/', admin_login, name="admin_login"),
    path('user_login/', user_login, name="user_login"),
    path('recruiter_login/', recruiter_login, name="recruiter_login"),
    path('user_signup/', user_signup, name="user_signup"),
    path('recruiter_home/', recruiter_home, name="recruiter_home"),
    path('user_home/', user_home, name="user_home"),
    path('Logout/', Logout, name="Logout"),
    path('admin_home/', admin_home, name="admin_home"),
    path('recruiter_signup/', recruiter_signup, name="recruiter_signup"),
    path('view_users', view_users, name="view_users"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('delete_recruiter/<int:pid>', delete_recruiter, name="delete_recruiter"),
    path('change_status/<int:pid>', change_status, name="change_status"),
    path('recruiter_pending', recruiter_pending, name="recruiter_pending"),
    path('recruiter_accepted', recruiter_accepted, name="recruiter_accepted"),
    path('recruiter_rejected', recruiter_rejected, name="recruiter_rejected"),
    path('recruiter_all', recruiter_all, name="recruiter_all"),
    path('change_passwordadmin', change_passwordadmin, name="change_passwordadmin"),
    path('change_passworduser', change_passworduser, name="change_passworduser"),
    path('change_passwordrecruiter',change_passwordrecruiter, name="change_passwordrecruiter"),
    path('add_job', add_job, name="add_job"),
    path('job_list', job_list, name="job_list"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)