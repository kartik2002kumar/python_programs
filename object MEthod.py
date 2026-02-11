# class bank:
#     def __init__(self,name,phnno,addr,email):
#         self.name=name
#         self.phno=phnno
#         self.addr=addr
#         self.email=email

#     def dis_obj(self):
#         print(self.name,self.phno,self.addr,self.email)

#     def ch_phno(self,new):
#         self.phno=new

# samir=bank('samir',446116,'delhi','jhjhua@gmail.com')

# samir.dis_obj()

# samir.ch_phno(564645646)
# samir.dis_obj()




class A29:
    cname='Python'
    ctiming=11 - 1
    ctrainer= 'Deepak sir'

    def __init__(self,name,roll,mock,mockday):
        self.name=name
        self.roll=roll
        self.mock=mock
        self.mockday=mockday

    def dis_obj(self):
         print(self.name,self.roll,self.mock,self.mockday)


    def ch_mock(self,new):
         self.mock=new


s1=A29('Kartik',73,'best')

s1.dis_obj()
s1.ch_mock('remock')
s1.dis_obj()
    
    
    
    