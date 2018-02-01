





from django.urls import path
from django.conf.urls import url
from library import views
from django.contrib import admin


urlpatterns = [ 
path('admin/',admin.site.urls),
url(r'^$',views.indeX)
,
 ]

