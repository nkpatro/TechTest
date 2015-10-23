from django.conf.urls import include, url, patterns
from rest_framework.routers import DefaultRouter
from devtest import views

__author__ = 'npatro'

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
                       url(r'^token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
                       url(r'^health/', include('health_check.urls')),
                       )