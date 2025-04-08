print("Cart_Management")
print("What Operation would you like to perform?")
print("1.Add_to_Cart\n2.Remove_from_Cart\n3.Empty_Cart\n4.Show_Cart\n5.Exit")
cart=[] 
while True:
    try:
        n=int(input("Enter your choice between 1-5: "))
        if n==5:
            print("Exit is success")
            break
        if 0<n<=4:
            if n==1:
                a=input("Enter the product name to add in your cart: ")
                cart.append(a)
                print(f"{a} is added to your cart successfully")
                print(cart)
            elif n==2:
                if cart:
                    c=input("Enter the product name to remove it from your cart: ")
                    if c in cart:
                        cart.remove(c)
                        print(f"{c} has been removed from your cart successfully!")
                    else:
                        print(f"{c} is not in cart")
                else:
                    print("Cart should contain products to remove!!")
            elif n==3:
                if cart:
                    d=input("Do you really want to empty cart?\nNote all products will be deleted if \"YES\" is selected as an input\nChoose wisely : yes/no: ")
                    if d=="yes":
                        cart.clear()
                        print("Whole cart is empty!")
                    elif d=="no":
                        print("Relax,your cart is not empty!")
                    else:
                        print("yes or no are the only inputs accepted")
                else:
                    print("Your cart is already empty!")
            elif n==4:
                if cart:
                    print("Below is your cart")
                    print(cart)
                else:
                    print("Your cart is empty")
                    print(cart)
        else:
            print("Your input should be between 1-5")
    except ValueError:
        print("Only int values are accepted,try again")
                    
                    
                    
