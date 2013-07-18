from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

fooadmin = admin.AdminSite(name='fooadmin')

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
fooadmin.register(User, UserAdmin)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'multiadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fooadmin/', include(fooadmin.urls)),
)
