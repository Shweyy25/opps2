class ineuron:
    name= "shweta"
    __age = 25

    def disp1(self):
        print("The name is ",ineuron.name)
        print("the age is",ineuron.__age)


class course(ineuron):#child class

    def __init__(self,numb_of_course,blog,intern):
        self.num_of_course=numb_of_course
        self.blog=blog
        self.intern=intern
        self._jobs="ineuron"


    def opportunity(self):
        self._jobs="ineuron1"
        print("number of course taken by the student",self.num_of_course)
        print("number of blogs students has done",self.blog)
        print("number of intership certificate student has got",self.intern)
        print("job opportunities student got",self._jobs)
s1=ineuron()
print(s1.disp1())
s2=course(3,2,4)
print(s2.opportunity())





