inventory = {}

while True:
    print("\n1.Add Product")
    print("2.Display Products")
    print("3.Search Product")
    print("4.Delete Product")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pid = input("Product ID: ")
        name = input("Product Name: ")
        qty = int(input("Quantity: "))
        inventory[pid] = {"name": name, "qty": qty}
        print("Product Added!")

    elif choice == "2":
        for pid, data in inventory.items():
            print(pid, data["name"], data["qty"])

    elif choice == "3":
        pid = input("Enter Product ID: ")
        if pid in inventory:
            print(inventory[pid])
        else:
            print("Product Not Found!")

    elif choice == "4":
        pid = input("Enter Product ID: ")
        if pid in inventory:
            del inventory[pid]
            print("Product Deleted!")
        else:
            print("Product Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
