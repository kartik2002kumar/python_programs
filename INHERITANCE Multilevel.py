class resume1:
    def __init__(self,name,email,phno,intermediate):
        self.name=name
        self.email=email
        self.phno=phno
        self.intermediate=intermediate

    def dis_obj(self):
        print(self.name,self.email,self.phno,self.intermediate)

class resume2(resume1):
    def __init__(self,name,phno,emai,intermediate,graduation,degree,project,internship):
        resume1.__init__(self,name,phno,email,intermediate)
        self.graduation=graduation
        self.degree=degree
        self.project=project
        self.internship=internship
    def display(self):
        super().display()

        








