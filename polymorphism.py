class ineuron:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp1(self):
        print("The name is ", self.name)
        print("the age is", self.age)


class course(ineuron):#child class

    def __init__(self,numb_of_course,blog,intern,jobs):
        self.num_of_course=numb_of_course
        self.blog=blog
        self.intern=intern
        self.jobs=jobs


    def disp1(self):
        print("number of course taken by the student",self.num_of_course)
        print("number of blogs students has done",self.blog)
        print("number of intership certificate student has got",self.intern)
        print("number of job opportunities student got",self.jobs)

s1=ineuron("shweta",25)
s2=course(3,2,4,5)
for s3 in (s1,s2):
    s3.disp1()
