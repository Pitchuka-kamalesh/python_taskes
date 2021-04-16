# todo class with instance static and class models and variables
class Today:

    def __init__(self, name, roll):     # imp: __init__ method it will activate when object is created and
        # variables are given when object is  creating a variable
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Name is {self.name}")
        print(f"Roll Number {self.roll}")

# class method and static method


class Method:
    @staticmethod
    def show():
        pass

    @classmethod
    def c_show(cls):
        pass


data = Today('kamal', 102030)
data.show()
