
from django.contrib import admin
from django.urls import path,include
from websitedata.views import *
from django.conf import settings
from django.conf.urls.static import static



from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetCompleteView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('signup',signup),
    path('signin',login,name='signin'),
    path('logout',logout),
    path('',index,name='index'),
    path('forum',forum,name='forum'),
    path('forum/<int:post_id>',ForumPostDetail,name="ForumPostDetail"),
    path('forum/create',create,name='create'),
    path('user/profile/',user_profile,name='user_profile'),
    path('profile/<username>',user_profile, name='view_profile_with_pk'),
    path('user/profile/edit',profile_edit,name='profile_edit'),
    path('user/profile/upload',upload_profile,name='upload_profile'),
    path('edit_post',edit_post,name='edit_post'),
    path('create',create_profiles,name='create_profiles'),



    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='User/password_reset.html'), name='password_reset'),
    path('reset-password-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='User/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='User/password_reset_done.html'), name='password_reset_done'),

    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='User/password_reset_complete.html'), name='password_reset_complete'),














]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



