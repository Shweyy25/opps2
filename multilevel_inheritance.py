class ineuron:  # parent class

    def name(self,nam):
        print("The name is ",nam)
    def age(self,ag):
        print("the age is",ag)


class course_details(ineuron):

    def details(self,course):
        print("name of course", course)
    def opportunity(self,blog, intern, jobs):
        print("blogs written", blog)
        print("internship done", intern)
        print("jobs opportunity given", jobs)


class student_details(course_details):
    pass


s3 = student_details()
s3.name("Shweta")
s3.age(25)
s3.details("data science")
s3.opportunity(3,2,6)
