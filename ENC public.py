# public
class clg:
    cname='bennit university'
    cloc='GN'
    cwebsite='benifwhfwh'

    def __init__(self,name,sid,sbatch,sYOP,sphno):
        self.name=name
        self.sid=sid 
        self.sbatch=sbatch
        self.sYOP=sYOP
        self.sphno=sphno

    def disp_obj(self):
        print(self.name,self.sid,self.sbatch,self.sYOP,self.sphno)

    @classmethod
    def dis_cls(cls):
        print(cls.cname,cls.cloc,cls.cwebsite)

samir=clg('samir',420,'btech',1947,7995130)

print(clg.cname)
print(samir.name)
samir.disp_obj()


