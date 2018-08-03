
def list_demo():
    listName = list(("Evans", "Chi", "Kh3m", "Rita"))
    for name in listName:
        if name == "Chi" or name == "Rita":
            print(name, "Female")
        else:
            print(name, " Male")
