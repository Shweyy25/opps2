class ineuron:

    def __init__(self, name,age,course,):
        self.name= name
        self.age=age
        self.course=course
        self.__intern="ineuron"
        self._job="hdfc bank"


    def identity(self):
        print("Name",self.name,"age",self.age)
    def courses(self):
        print("is studying",self.course)
    def work(self):
        print("has done internship",self.__intern)
    def job(self):
        print(self.name,"has worked in",self._job)
    def job_change(self,new):
        self._job=new
        print("changed the job to",self._job)



obj=ineuron("Shweta",25,"datascience",)
obj.identity()
obj.courses()
obj.work()
obj._ineuron__intern="ineuron1"
obj.work()
obj.job()
obj.job_change("icici bank")


