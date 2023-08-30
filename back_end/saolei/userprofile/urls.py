from django.urls import include, path

from . import views
app_name = 'userprofile'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    # path('delete/<int:id>/', views.user_delete, name='delete'),
    path('captcha/', include('captcha.urls')),
    path('refresh_captcha/',views.refresh_captcha),
    path('get_email_captcha/',views.get_email_captcha),
    
    # path('captcha/captcha', views.captcha, name='captcha'),
    # path('edit/<int:id>/', views.profile_edit, name='edit'),
]