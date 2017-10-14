#coding: utf-8
from django import forms
#domainNameManager app 里面的models 文件 中的 domainName类
from domainNameManager.models import domainName

class domainForm(forms.ModelForm):
    class Meta:
        model = domainName
        #fields = ('name', 'nameDistributor','exptresDate','user','email','organization','availabity',)
        #fields = ['group', 'server_type', 'ip', 'intraip', 'other_ip', 'port', 'is_monitoring', 'is_backup', 'config','app_name', 'role_name', 'editor']
        fields = ['name', 'nameDistributor', 'exptresDate', 'user', 'email', 'organization'] #有一次是这个有个 , 出错
        #fields = ['name', 'nameDistributor', 'exptresDate', 'user', 'email', 'organization', 'availabity']
        #fields = ['name', 'nameDistributor', 'exptresDate', 'user', 'email', 'organization']
        #fields = ('name',)  #bak  原来 是元组 改为列表 就好了 20171010
