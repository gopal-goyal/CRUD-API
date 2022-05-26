from django.conf.urls import url 
from userdata import views 
 
urlpatterns = [ 
    url(r'^api/userdata$', views.userdatalist),
    url(r'^api/userdata/(?P<pk>[0-9]+)$', views.userdata_detail),
    url(r'^api/userdata/published$', views.userdata_list_published)
]