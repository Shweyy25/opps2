
class ineuron:
    def __init__(self,name,yob):
        self._name=name
        self.yob=yob
    def disp(self,course_name) :
        print("course name",course_name)
    def __age(self,curnt_yr):
        return curnt_yr-self.yob

class students(ineuron):
    _name="shweyy"
    __yob=1994
    def birthday(self,current_year):
        return current_year-self.__yob

    def opportunity(self, blog, intern, jobs):
        print("blogs written", blog)
        print("internship done", intern)
        print("jobs opportunity given", jobs)

i=ineuron("shweta",1996)
print(i._name)
print(i._ineuron__age(2022))
print(i.disp("data science"))
s=students("sh",1994)
print(s._name)
print(s.birthday(2022))
print(s.opportunity(3,4,5))
