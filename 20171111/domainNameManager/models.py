#coding: utf-8

from django.db import models
"""
look this  20171018am
密码
SSL证书类型  credential type 
证书费用
证书到期时间
"""
# Create your models here. 用户密码') #add
class domainName(models.Model):
    name = models.CharField(max_length=20, verbose_name='域名')
    nameDistributor = models.CharField(max_length=50,verbose_name='域名供应商')
    exptresDate = models.CharField(max_length=20, verbose_name='到期时间')
    user = models.CharField(max_length=50, verbose_name='注册用户')
    password = models.CharField(max_length=50, verbose_name='用户密码')
    ssltype = models.CharField(max_length=20, verbose_name='SSL证书类型')
    sslcost = models.CharField(max_length=20, verbose_name='SSL证书费用')
    sslexptresDate = models.CharField(max_length=20, verbose_name='SSL证书到期时间')
    email = models.CharField(max_length=50, verbose_name='注册邮箱')
    organization = models.CharField(max_length=50, verbose_name='注册公司')
    availabity = models.BigIntegerField(default=1, verbose_name='是否可用')
    other = models.CharField(max_length=50, verbose_name='备注')

    def __unicode__(self):
       return self.name

    def natural_key(self):
        return self.name

    class Meta:
        #指定自定义数据库表名
        db_table = 'domainName'
        #两个字段保持唯一性时使用
        unique_together = (('name', 'availabity'),)
        #unique_together = (('name', 'nameDistributor ', 'exptresDate', 'user', 'email', 'organization',   'availabity'),)