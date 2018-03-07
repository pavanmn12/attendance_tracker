from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from attendance_tracker import views as core_views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^login/$',
        'django.contrib.auth.views.login', {'template_name': 'login.html'}
        ),
    url(r'^checkinn/new/$', views.entry, name='checkinn'),
    url(r'^checkout/new/$', views.exit_out, name='exit_out'),
    url(r'^accounts/profile/$', views.details, name='details'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout', {'next_page': '/login/'}
        ),

]
