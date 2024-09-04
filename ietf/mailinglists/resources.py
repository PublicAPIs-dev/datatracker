# Copyright The IETF Trust 2016-2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Autogenerated by the makeresources management command 2016-06-12 12:29 PDT


from ietf.api import ModelResource
from tastypie.fields import ToManyField                 # pyflakes:ignore
from tastypie.constants import ALL, ALL_WITH_RELATIONS  # pyflakes:ignore
from tastypie.cache import SimpleCache

from ietf import api
from ietf.api import ToOneField                         # pyflakes:ignore

from ietf.mailinglists.models import Allowlisted, NonWgMailingList


from ietf.person.resources import PersonResource
class AllowlistedResource(ModelResource):
    by               = ToOneField(PersonResource, 'by')
    class Meta:
        queryset = Allowlisted.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'allowlisted'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "time": ALL,
            "email": ALL,
            "by": ALL_WITH_RELATIONS,
        }
api.mailinglists.register(AllowlistedResource())

class NonWgMailingListResource(ModelResource):
    class Meta:
        queryset = NonWgMailingList.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'nonwgmailinglist'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "domain": ALL,
            "description": ALL,
        }
api.mailinglists.register(NonWgMailingListResource())



