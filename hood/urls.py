from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$',views.index, name = 'index'),
  url(r'^profile/$',views.profile,name='profile'),
  url(r'^search/', views.search_results, name='search_results'),
  url(r'^upload/$', views.upload_business, name='upload_business'),
  url(r'^hood/$', views.new_neighbourhood, name='new_neighbourhood'),
  url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)