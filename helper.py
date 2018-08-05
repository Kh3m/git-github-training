
class Helper:
    def list_demo(self):
        listName = list(("Evans", "Chi", "Kh3m", "Rita"))
        for name in listName:
            if name == "Chi" or name == "Rita":
                print(name, "Female")
            else:
                print(name, " Male")

    @staticmethod
    def fibonacci(n):
        a,b = 0,1
        while a < n:
            print(a)
            a,b = b,a+b 


