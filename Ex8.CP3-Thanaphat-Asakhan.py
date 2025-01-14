Username = input(("Press Username : "))
Password = input(("Press Password : "))
if Username == "admin" and Password == "1234" :
    print("Done!")
    print("-----STARS SHOP-----")
    print("1.Food")
    print("2.Drink")
    print("3.check bill")
    UserSelected = int(input("list : "))
    if UserSelected == 1:
        print("1. padkapaw",40,"baht")
        print("2. tomyumkung",80,"baht")
    elif UserSelected == 2:
        print("1. water",10,"baht")
        print("2. coffee",20,"baht")
    elif UserSelected == 3:
        print("end")