暂时用这个 mycmdb2018 是新的 不死加了很多新功能 
云机器第一个够用
蓝本就是风行
https://github.com/voilet/cmdb



time
2017 12  15  

http://192.168.30.56
use dkm
password dkm123456

centos7上一定成功的 

注意  
这个是在debian上的问题　
sudo python manage.py  runserver 0.0.0.0:80 运行 可能会 
AttributeError at /
class Meta has no attribute 'object_class'

怎么样才能搞成可以用 80端口的呢  



#CMDB
### 目前拥有功能有：
####资产管理
    * 根据不同数据中心(IDC),分类管理
    * 支持导出excel文件

####应用管理
  
####域名管理
  	* 输入域名自动获取域名信息

####用户管理
    * 根据不同需求设置用户可访问该系统的那些菜单

####告警接口
    * 接口使用请看alarm/readme

##安装环境
install mysql
自己的软件仓库
配置mysql
mkdir  /var/lib/mysql/
ln -s /tmp/mysql.sock  /var/lib/mysql/




wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

yum install gcc  -y 
yum install  python-devel

ImportError No module named MySQLdb解决方法
pip install mysql-python

[root@localhost hcmdb]# pip install MySQL-python
Collecting MySQL-python
  Using cached MySQL-python-1.2.5.zip
    Complete output from command python setup.py egg_info:
    sh: mysql_config: 未找到命令

source  /etc/profile #就可以了 哈哈



清空数据库
python manage.py flush

* python2.7
* pip install -r requirements.txt

##初始化
###初始数据库
####创建数据库(进入数据库操作)
    #* create database hcmdb CHARACTER SET utf8;
    * create database mycmdb CHARACTER SET utf8;
    grant all on mycmdb.* to mycmdb@'localhost' identified by 'evan886DKdk****#d'; (根据settings.py中设定修改)
    #* grant all on hcmdb.* to HCmdbAdmin@'localhost' identified by 'nDrDyXd#dnoMqH2'; (根据settings.py中设定修改)
####初始化数据表
    * python2.7 manage.py makemigrations
    * python2.7 manage.py migrate

####初始化数据  我一般 是导入为自己的
#看你自己本地的密码了
mysql -uroot -p'00000l!q$EWQ23FD23'


   mysql -umycmdb -p mycmdb < hcmdb20170926.sql
    #* mysql -uHCmdbAdmin -p hcmdb < init.sql

##运行 为什么 有一次用 80 和sudo 不行呢 
   * python2.7 manage.py runserver 0.0.0.0:8888

##登陆
   * 用户名: cmdbAdmin
	 密码: cmdbAdmin

#err 395292

  File "/usr/lib/python2.7/dist-packages/MySQLdb/connections.py", line 50, in defaulterrorhandler
    raise errorvalue
django.db.utils.OperationalError: (1005, 'Can\'t create table `hcmdb`.`#sql-19cb_39` (errno: 150 "Foreign key constraint is incorrectly formed")')



raise ImproperlyConfigured("Error loading MySQLdb module: %s" % e)
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: libmysqlclient.so.20: cannot open shared object file: No such file or directory

#前面是你的真正位置 
ln -s  /data/apps/mysql/lib/libmysqlclient.so.20   /usr/lib64/

