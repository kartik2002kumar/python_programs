class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print('rec',a*b)
        elif a!=None:
            print('sqr',a*a)

        else:
            print("np finding")


ob1=Area()
ob1.find_area()
ob1.find_area(4)
ob1.find_area(5,5) 
