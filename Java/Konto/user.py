print("Hello! Here you can create a new user account.")
print("Please enter what you want to do:")
counter = 0
run = True
while run:
    print("1. Create a new user account\n2. Change the password of an existing user account\n3. Exit")
    check = input()
    match check:
        case "1":
            print("Please enter the username you want to create:")
            username = input()
            print("Please enter the password you want to create:")
            password = input()
            print("Please enter the password again:")
            password2 = input()
        case "2":
            print("Please enter the username you want to change the password for:")
            username = input()
            print("Please enter the new password you want to create:")
            password = input()
            print("Please enter the new password again:")
            password2 = input()
        case "3":
            print("Exiting...")
            run = False
        case _:
            counter += 1
            if counter > 3:
                print("You have entered an invalid option too many times. Exiting...")
                run = False
            else:
                print("You have entered an invalid option.")
