
class Demo:
    Value=1
    def __init__(self,no1,no2):
        self.Value1=no1
        self.Value2=no2
        
    def fun(self):
        print("Inside Fun")
        print(self.Value1)
        print(self.Value2)

    def gun(self):
        print("Inside Gun")
        print(self.Value1)
        print(self.Value2)


def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()


if __name__=="__main__":
    main()