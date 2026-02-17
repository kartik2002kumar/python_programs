# class A:
#     a=10
#     b=20
# class B(A):
#     p=30
#     q=40

# print(A.a,A.b)
# print(B.a)




# WAP to create a bank online,offline,where show the single level inheritance 


# class Bank:

#     bank='SBI'
#     bankIFSC='SBI0054'

#     def __init__(self,Cname,Cbalance):
#         self.Cname=Cname
#         self.Cbalance=Cbalance

#     def deposit(self,amount):
#         self.balance+=amount


#         print("Amount is ",amount)
#         print("balance is ",self.balance)


#     def withdraw(self,amount):
#          if amount <= self.balance:
#             self.balance -= amount
#             print("Amount Withdrawn:", amount)
#             print("Remaining Balance:", self.balance)
#         else:
#             print("Insufficient Balance")
    
# class Onlinebank:
     





class online:
     bname='ICICI'
     bloc='Noida'
     Bifsc='ICICI634646'

     def __init__(self,name,addr,phno,accno):
          self.name=name
          self.addr=addr
          self.phno=phno
          self.accno=accno

     @classmethod

     def disp_cls(cls):
          print(cls.bname,cls.bloc,cls.Bifsc)

# badal=pnline('badal','meerut',464666465497,7894)

class offline(online):
     def __init__(self,name,addr,phno,accno,aadhar,PAN):
           super().__init__(name,addr,phno,accno)      #construcur chaining
           self.aadhar=aadhar
           self.PAN=PAN

     def disp_obj(self):  #method chaining
          super().dis_obj()
          print(self.aadhar,self.PAN)

badal=offline('badal','meerut',464666465497,7894,5698989,'nkfdjhdk5')


          

