# class bank:
#     bname='BOB'
#     bloc='on earth'
#     bIFSC='BOB16446'

#     def __init__(self,name,accno,phno,addr,email):
#         self.name=name
#         self.accno=accno
#         self.phno=phno
#         self.addr=addr
#         self.email=email

# don=bank('don',420,789,'west delhi','asghagh@gmail.com')

# print(bank.bname,bank.bloc,bank.bIFSC)
# print(don.name,don.accno,don.addr,don.email)



# WAP to hospital

class hospital:
    hname='sharda hospital'
    hloc='greater noida'
    htype='private'

    def __init__(self,name,wardno,disease,drname):
        self.name=name
        self.wardno=wardno
        self.disease=disease
        self.drname=drname


ankit=hospital('Ankit',56,'typhoid','Dr RK')

print(hospital.hname)
print(ankit.name,ankit.disease)