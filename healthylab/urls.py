# coding: utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from rest_framework.authtoken import views as drf_views

from healthyapp.urls import urlpatterns as app_urls, api_urlpatterns as app_api
from healthyfood.urls import urlpatterns as food_urls, api_urlpatterns as food_api


admin.site.site_header = _("Healthy Lab")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='healthyapp/login.html')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    # Django REST Framework
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/', drf_views.obtain_auth_token, name='token'),
    # Auth / Social
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth')),
    url(r'^social/ ', include('social_django.urls', namespace='social')),
    # Healthy Lab
    # url(r'^$', RedirectView.as_view(pattern_name='healthyapp_index', permanent=True)),
    url(r'^healthyapp/', include(app_urls)),
    url(r'^api/healthyapp/', include(app_api)),
    url(r'^healthyfood/', include(food_urls)),
    url(r'^api/healthyfood/', include(food_api)),
]

# Common framework
if 'common' in settings.INSTALLED_APPS:
    from common.urls import urlpatterns as common_urls
    from common.api.urls import urlpatterns as common_api
    urlpatterns += [
        url(r'^common/', include(common_urls, namespace='common')),
        url(r'^api/common/', include(common_api, namespace='common-api'))]

# Debug
if settings.DEBUG:
    # Static and media files
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Django Debug Toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [url(r'^debug/', include(debug_toolbar.urls))]
