# A class is a blueprint for creating objects
# class is like structure in C
class student:
    name = "Abhishek"
    def getBranch(self):
        print("branch is not there")

#object intantiation
abhi = student() 
abhi.name
student.name = "Abhi"  #changing class attribute
abhi.branch = "cse"  #Adding instance attrubute

abhi.getBranch()




