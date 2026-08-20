class student:
    college_name = "jecrc"

    def __init__(self,name, math, english, hindi):
        self.name =name
        self.math=math
        self.english=english
        self.hindi=hindi

    def marks(self):
        print ("The marks of " , self.name , "is",self.math,self.english,self.hindi)

s1 = student ("karan", 99, 100, 97)
s1.marks()
# print(s1.marks)
print(s1.college_name)