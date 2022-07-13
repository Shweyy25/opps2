
'''''''''''

ineuron,students,class ,classtype, number of courses,affiliates,
blog,internship,jobs as reference example

'''''''''''


#class- class type-students
#courses- number of courses-data science--data analytics--programming
#opportunities- blog-internship-jobs


class ineuron :

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("The name is ",self.name)
        print("the age is",self.age)
s1=ineuron("Shweta",25)
print(s1.disp())

class course(ineuron :
    def __init(self,numb_of_course,opp):
