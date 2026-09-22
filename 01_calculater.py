while True :

    number_1 = int(input("Enter Number 1 : "))
    number_2 = int(input("Enter Number 2 : "))


    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")

    choice = int(input("Select your choice to perform : "))

    if choice == 1 : 
        print("Addition is :", number_1 + number_2)

    elif choice == 2 :
        print("Subtraction is :", number_1 - number_2)

    elif choice == 3 :
        print("Multiplication is :", number_1 * number_2)

    elif choice == 4 :
        if number_2 == 0:
            print("WRONG , Can't divide by 0 ")
        else :
             print("Division is :", number_1 / number_2)    

    else :
        print("ERROR ! Wrong choice is entered , Please enter from 1 - 4 ")    
        continue    

    while True:
            again = input("Want To Calculate Again? (yes / no): ").lower()
    
            if again == "yes" :
                break
 
              
            elif again == "no":
                print("CALCULATION STOPPED...!")
                exit()
    
            else:
                print("ERROR: Please enter only yes or no") 
            