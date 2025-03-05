# #父类1 父类2  子类
# class shimen(object):
#     __init__
#     def gongfu(self):
#         gongfu = (师门祖传法)
#
#     def shiyong(self):
#         shiyongjineng = (f'使用{self.gongfu}击败了敌人)
#
# xuanzangshifu = shimen()
#
# print(xuanzangshifu.shiyong())


# #定义一个类，创建两个对象，第一个对象添加属性，其他不加，打印测试类和对象单独设定属性对其他的影响。
# class Students():
#     studentid = 'ID unkown'
#     studentname = 'name unkown'
# #此处注意小括号，没有小括号代表等价创建一个相同的类，会指向同一个地址，造成属性说改都改。创建对象必须要有小括号
# #创建对象
# stu1=Students() #此处注意小括号，没有小括号代表等价创建一个相同的类，会指向同一个地址，造成属性说改都改。创建对象必须要有小括号
# stu2=Students()
# print('创建对象，并打印测试')
# print('stu1的id是%s，name is %s'%(stu1.studentid,stu1.studentname))
# print('student的id是%s，name is %s' % (Students.studentid, Students.studentname))
# print('stu2的id是%s，name is %s'%(stu2.studentid,stu2.studentname))
# #修改类属性，并打印测试
# print('修改类属性为 not set，并打印测试')
# Students.studentid= 'ID not set'
# Students.studentname= 'name not set'
# print('stu1的id是%s，name is %s'%(stu1.studentid,stu1.studentname))
# print('student的id是%s，name is %s' % (Students.studentid, Students.studentname))
# print('stu2的id是%s，name is %s'%(stu2.studentid,stu2.studentname))
# #修改str1属性，并打印测试
# print('修改str1属性，并打印测试')
# stu1.studentid='001'
# stu1.studentname='王耀日'
# print('student的id是%s，name is %s' % (Students.studentid, Students.studentname))
# print('stu1的id是%s，name is %s'%(stu1.studentid,stu1.studentname))
# print('stu2的id是%s，name is %s'%(stu2.studentid,stu2.studentname))
# #修改str2属性，并打印测试
# print('修改str2属性，并打印测试')
# stu2.studentid='002'
# stu2.studentname='李长河'
# print('student的id是%s，name is %s' % (Students.studentid, Students.studentname))
# print('stu1的id是%s，name is %s'%(stu1.studentid,stu1.studentname))
# print('stu2的id是%s，name is %s'%(stu2.studentid,stu2.studentname))
# print(stu1,stu2)

# 定义类，设定两个方法，并传参调用
# class Cwallet():
#     def setcolor(self,color):#设定颜色
#         self.color='color'
#     def printcolor(self): #显示颜色
#         print(self.color)
#
# wallet1=Cwallet()
# # print(wallet1.color) 此时未设定颜色属性，会报错
# wallet1.setcolor('black')  #调用设定颜色方法，传入一个参数
# wallet1.printcolor() #调用显示颜色 方法成功


#私有属性  设定  类外调用方法:对象._类名__属性
#
# class Cwallet():
#     def __init__(self):
#         self.manufacturer='村口小店'
#
#         self.__name='ccc'
#     def setnatrue(self,material='皮',size='normal',color='white'):
#         self.material=material
#         self.size=size
#         self.color=color
#     def printcolor(self): #显示颜色
#         print(self.color)
#
# wallet1=Cwallet()
# wallet1.setnatrue('铁','巨型','yellow')
# # print(wallet1.__name) 无法直接访问私有属性，会报错
# print(wallet1._Cwallet__name)#私有属性 方法成功
# wallet1.__dict__['material']='布'  #可以通过对象字典直接修改属性
# print(wallet1.__dict__)

# Cwallet.__dict__['_Cwallet__name']='曹'
# print(Cwallet.__dict__) #模组：自身，method name :function class name.method name  at 内存地址， method name :function class name.method name at 内存地址~~~~~~~~~~~~
# class MyClass:
#     class_attr = 10
#
#     def __init__(self, value):
#         self.instance_attr = value
#
#     def instance_method(self):
#         return self.instance_attr
#
#     @classmethod
#     def class_method(cls):
#         return cls.class_attr
#
#     @staticmethod
#     def static_method():
#         return "This is a static method"
#
#
# print(MyClass.__dict__)

#构造方法  #并设置默认参数，打印测试
# class Cwallet():
#     def __init__(self,manufacturer='村口小店'):
#         print('构造方法开始，对象创建')
#         self.manufacturer=manufacturer
#
#         self.__name='ccc'
#     def setnatrue(self,material='皮',size='normal',color='white'):
#         self.material=material
#         self.size=size
#         self.color=color
#     def printmanufacturer(self): #显示颜色
#         print(('生产厂家为%s')%(self.manufacturer))
# wallet1=Cwallet('奥特曼')
# wallet1.printmanufacturer()

#析构方法，str方法 内置比较方法 设定并使用
# class Cwallet():
#     def __init__(self,manufacturer='村口小店',adate='2010'):
#         print('构造方法开始，对象创建')
#         self.manufacturer=manufacturer
#         self.adate=adate
#
#         self.__name='ccc'
#     # def setnatrue(self,material='皮',size='normal',color='white'):
#     #     self.material=material
#     #     self.size=size
#     #     self.color=color
#     def printmanufacturer(self): #显示颜色
#         print(('生产厂家为%s')%(self.manufacturer))
#     def __del__(self):
#         print('%s对象已删除'%(self.manufacturer))
#     def __str__(self):
#         return ('%s的部分属性是%s，别的属性没问'%(self.manufacturer,self.adate))
#     def __eq__(self, other):
#         print(self.adate<=other.adate)
# wallet1=Cwallet('奥特曼','1950')
# wallet2=Cwallet('小猪','1888')
#
# print(wallet1)
# wallet2!=wallet1# 这里比较符号写什么不影响结果，类内比较函数那里写什么决定结果
# '''结果是  构造方法开始，对象创建
# 构造方法开始，对象创建
# 奥特曼的部分属性是1950，别的属性没问
# True
# 奥特曼对象已删除
# 小猪对象已删除
# '''


#类的继承  写三个类，继承
# class animal():
#
#     # def __init__(self,livedead='dead'):  #之所以注释掉，因为子类不会拥有父类中init的属性，init再创建对象时候才调用
#     #     self.ddddd =livedead
#
#     def setlive(self,livedead='dead'):   #子类不会获得父类init method中的属性
#         self.livedead=livedead
# class persion(animal):
#     def __init__(self,cname='unkown',birthday='19000101'):
#         self.cname=cname
#         self.birthday=birthday
# class cat(animal):
#     def __init__(self,cvioce='miur'):
#         self.cvioce=cvioce
# cat1=cat('ao')
# persion1=persion('lily')
#
# print(cat1.cvioce)
# print(persion1.cname)
# cat1.setlive('live')  #先调用继承于父类的方法设定属性，下面才能打印成功
# print(cat1.livedead)


#多态，设定不同类有共同属性，便于使用同一函数调用共同属性输出
# class animal():
#     #此处设置基本属性，便于后续子类直接拥有
#     clivedead='dead'
#     cvoice='unkown'
#     cname='notdef'
#     chand='1'
#     cleg='1'
#     cend='0'#此属性测试super方法时追加
#     def setlive(self,clivedead='dead'):   #子类不会获得父类init method中的属性
#         self.clivedead=clivedead
#     def setvoice(self,cvoice='unkown'):
#         self.cvoice=cvoice
#     def setname(self,cname='unkown'):
#         self.cname=cname
#     def setvoice(self,chand='1'):
#         self.chand=chand
#     def setvoice(self,cleg='1'):
#         self.cleg=cleg
#     def setcend(self,cend='0'):
#         self.cend=cend
#     def __init__(self,clivedead='dead',cvoice='unkown',cname='unkown',chand='1',cleg='1'):
#         self.clivedead=clivedead
#         self.cvoice = cvoice
#         self.cname = cname
#         self.chand = chand
#         self.cleg = cleg
#
# class persion(animal):
#
#     def setbirthday(self,birthday='19000101'):
#         self.birthday=birthday
# class cat(animal):
#
#     def setvoice(self,cvioce='miur'):
#         self.cvoice=cvioce
#
#     def csuperuse(self):  #尝试失败
#
#         super().setcend('11')
#         print(self.cend)
#
# persion1=persion('live','hello','朱高鸣','2','2')
# print(persion1.__dict__)
# persion1.cvoice='hello,i am ming'
# cat1=cat()
# cat1.clivedead='live'
# cat1.setvoice('mer')
# print(cat1.__dict__)
#
# #此处设定method可以调用对象内同属性修改，实现多态
# def setshuxing(duixiang,age):
#     duixiang.age=age
#     print('属性已修改%s'%(duixiang.age))
# setshuxing(persion1,99)
# print(persion1.__dict__)
# setshuxing(cat1,7)
# print(cat1.__dict__)
#
#
# cat1.csuperuse()  #调用成功，几次失败原因：必须类内使用super方法，类外报错，super不能直接修改父类属性，需调用setatt内置方法。
# print(animal.cend)
#super方法尝试
# cat1.csuperuse #这行代码错误，卡了我很久，因为又忘了小括号了，所以，发现代码无效，注意看格式，可能格式问题导致没有执行
# # print(cat1.cend)
# print(cat1.cend)
# print(persion1.cend)


#类外添加方法和 slot限制扩展方法
#创建两个无属性继承关系的类，内置slot方法，类外添加方法
# class a():
#     __slots__='setname','setatt'
#
#     pass
# class b(a):
#     __slots__='setno'
# class c(b):
#     pass
# #创建实例测试 solts
# bb=b()
# bb.setname='wang'
# print(bb.setname)
# cc=c()
# cc.setcolor='green'
# # bb.setcolor='green' 报错，表明即使是继承父类，但如果子类没有solts设定，继承于父类的slots无效
# print(cc.setcolor)
# # print(bb.setcolor)

#类外添加方法
#设定函数，然后类和示例分别添加
# 因为类添加简单，实例添加需借助methodtype完成
# class a():
#
#
#     pass
# class b(a):
#     pass
# class c(b):
#     pass
# def setatt(self,catt='cat'):
#     self.setatt=catt
# #类添加方法
# b.setatt=setatt
# bb=b()
# bb.setatt('power')
# print(bb.setatt)
# aa=a()
# # aa.setatt=setatt()  #此处报错，
# # print(aa.setatt)
#
# #加载type模块，使用methodtype给实例添加方法
# import types
# aa.setatt=classmethod(setatt)    #类方法方式添加
# aa.setatt='dog'
# print(aa.setatt)
# aa.setatt=types.MethodType(setatt,aa)   #types.MethodType方法添加，此处M是大写
# aa.setatt('alephont')
# print(aa.setatt)

