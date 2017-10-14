#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
from django.conf.urls import include, url
""" domainNameManager  应用下 views 里面的 domainName_add 方法 """
urlpatterns = [
	url(r'^domainNameAdd/', 'domainNameManager.views.domainName_add'),
	url(r'^domainNameList/', 'domainNameManager.views.domainName_list'),
]