class Student:
    size = 5

    def __init__(self):
        print("Inside Student Constructor")
        self.name = "Demo"
        self.marks = 70

    def get_marks(self):
        print("Inside Student get_marks")
        return self.marks
    

class Teacher:

    def __init__(self):
        print("Inside Teacher Constructor")
        self.name = "Teacher"
        self.marks = 50

    def get_marks1(self):
        print("Inside Teacher get_marks")
        return self.marks


class Child(Teacher,Student) :

    def __init__(self):
        print("Do nothing")
        self.marks = None

    def get_marks1(self):
        print("Inside Child get_marks")
        return self.marks

class A: pass


print(Student().get_marks())
print(Student.size)
print(Student().size)

print(Child().get_marks())
print(Child().get_marks1())

class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(P.mro())