
class MyClass():
    def my_method(self):
        pass

class SomeOtherClassThatUsesMyClass():
    def method_under_test(self):
        myclass = MyClass()
        return myclass.my_method()
