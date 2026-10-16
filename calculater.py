while True:
    print("\nCalculater")
    print("1.Sum(+)")
    print("2.Subtraction(-)")
    print("3. Multipliction(*)")
    print("4. Division(/)")
    print("5.Converting from Base 10 to Base 2")

    choice = input("Select the desire operation= ")

    if choice == "1":
        num1 = float(input("Enter the First number= "))
        num2 = float(input("Enter the Secend number= "))
        print("Resault=", num1 + num2)

    elif choice == "2":
        num1 = float(input("Enter the First number= "))
        num2 = float(input("Enter the Secend number= "))
        print("Resault=", num1 - num2)

    elif choice == "3":
        num1 = float(input("Enter the First number= "))
        num2 = float(input("Enter the Secend number= "))
        print("Resault=", num1 * num2)

    elif choice == "4":
        num1 = float(input("Enter the First number= "))
        num2 = float(input("Enter the Secend number= "))

        if num2 != 0:
            print("Resault=", num1 / num2)
        else:
            print("Division is not possible!")

    elif choice == "5":
        num = int(input("Enter the number in Base 10= "))
        binary = bin(num)[2:]
        print("Number in Base 2=", binary)

    else:
        print("The selection is invalid!")

    while True:
        again = input("Do you want to continue?")

        if again == "Yes" or again == "yes":
            break

        elif again == "No" or again == "no":
            print("The calculator has been closed.\nGood luck.\nHope to see you again!")
            exit()

        else:
            print("Invalid input! Please enter Yes or No.")