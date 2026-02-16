# # Private

# class clg:
#     cname='bennit university'
#     cloc='GN'
#     __cwebsite='benifwhfwh'

#     def __init__(self,name,sid,sbatch,sYOP,sphno):
#         self.name=name
#         self.__sid=sid 
#         self.sbatch=sbatch
#         self.sYOP=sYOP
#         self.sphno=sphno

#     def disp_obj(self):
#          print(self.name,self.sbatch,self.sYOP,self.sphno)


#     def _disp_sphno(self):
#         print(self.sphno)

#     @classmethod
#     def dis_cls(cls):
#         print(cls.cname,cls.cloc,cls.__cwebsite)

# samir=clg('samir',420,'btech',1947,7995130)

# # clg.disp_cls()
# # print(clg.__cwebsite)


# print(clg._clg__cwebsite)

# print(samir._clg__sid)
# samir._clg__sid=789
# print(samir._clg__sid)





class bank:
    bname='HDFC'
    bloc='New delhi'
    bIFSC='HDFC0064'

    def __init__(self,cname,caccno,cphno):
        self.cname=cname
        self.caccno=caccno
        self.cphno=cphno


    def disp_obj(self):
        print(self.cname,self.caccno,self.cphno)


    @classmethod

    def dis_cls(cls):
        print(cls.bname,cls.bIFSC)




