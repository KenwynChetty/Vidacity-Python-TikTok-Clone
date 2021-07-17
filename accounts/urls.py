from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.loginPage, name="login"),
    path('new_chat/', views.UserChatList, name='users_chat_list'),
    path('profile-setup/',views.setup_profile, name='setup_profile'),
    path('like/', views.like, name='like'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)