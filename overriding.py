class ineuron:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp1(self):
        print("The name is ", self.name)
        print("the age is", self.age)


class course(ineuron):#child class

    def __init__(self,numb_of_course,blog,intern,jobs,):
        self.num_of_course=numb_of_course
        self.blog=blog
        self.intern=intern
        self.jobs=jobs

    def disp1(self,name,age):
        print("name is",name)
        print("age",age)

    def opportunity(self):
        print("number of course taken by the student",self.num_of_course)
        print("number of blogs students has done",self.blog)
        print("number of intership certificate student has got",self.intern)
        print("number of job opportunities student got",self.jobs)

s1=course(3,2,1,6)
print(s1.disp1("shweta",25))
print(s1.opportunity())
print(s1)

