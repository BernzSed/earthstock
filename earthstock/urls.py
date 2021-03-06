from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from earthstock import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'earthstock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.earthstock, name='index'),
    url(r'^earthstock/', views.earthstock, name='earthstock'),
    url(r'^updatestocks/', views.updatestocks, name='updatestocks'),
    url(r'^stocks.kml$', views.stocks_kml, name='stocks_kml'),
    url(r'^admin/', include(admin.site.urls)),
)
