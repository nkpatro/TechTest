from django.contrib.auth.models import User
import rest_framework_filters as filters

__author__ = 'npatro'


class UserFilter(filters.FilterSet):
    groups = filters.CharFilter(name='groups__name')

    class Meta:
        model = User
        # fields = ['username', 'groups',]
