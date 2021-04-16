# class 
"""
class Fun:
    b = 100
    def __init__(self,a):
        self.a = a
    
    def show(self):
        print("instance varable",self.a)
        print("class variable",Fun.b)
    
    @classmethod
    def c_meth(cls):
        print("class variable",cls.b)
        # print("instance variable",self.a)

    @staticmethod
    def s_meth():
        print("Enter the static variable s_meth",Fun.b)
        # print("Enter the class variable s_meth",Fun.a)



Fun.c_meth()
Fun.s_meth()
obj = Fun(100)
obj1 = Fun(200)
obj.show()
print(obj.a)
obj1.show()
"""
class Adder:

    def __init__(self,door_no,street,picode,near_by):

      self.door_no  =   door_no  

      self.street   =   street 

      self.pincode  =   pincode

      self.near_by  =   near_by


class Student:

    def __init__(self,name,roll,per,addr):

        self.name = name
        self.roll = roll
        self.per = per
        self.addr = Adder(door_no, street, picode, near_by)
    
    def show(self):

        
   