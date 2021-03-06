from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns =[
    path('home', views.home, name="home"),
    path('allpost/', views.all_posts, name="allposts"),
    path('update_profile/<user_id>', views.update_profile, name="update_profile"),   
    path('profile/<str:pk>', views.profile, name="profile"),
    path('facilities',views.facilities,name='facilities'),
    path('post',views.create_post,name='post'),
    path('create_facility',views.create_biz,name='create_facility'),
    # path('update_post/<str:pk>', views.update_post, name='update_post'),
    path('delete_post/<str:pk>', views.delete_post, name='delete_post'),
    # path('review/<post_id>', views.review, name="review"),
    path('search', views.search_biz, name="search"),



    path('', views.login_user, name="login"),
    path('logout-user', views.logout_user, name="logout"),
    path('register-user', views.register_user, name="register"),
    # path('edit_profile', views.edit_profile, name="edit_profile"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)