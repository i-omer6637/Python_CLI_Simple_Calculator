try:
    import os
    
    # A simple calculator
    print("Welcome to Calculator")
    def main():
        while True:
            choice = input("Press \n 1 to Add \n 2 to Sub \n 3 to Multiple \n 4 to divide \n :")
            num1 = input("Enter first no : ")
            num2 = input("Enter second no : ")
            match int(choice):
                case 1:
                    operate("+",num1, num2)
                case 2:
                    operate("-",num1, num2)
                case 3:
                    operate("*",num1, num2)
                case 4:
                    operate("/",num1, num2)
                case _:
                    print("Invalid Option")
            
            loop_check = input("Press 1 to Try Again : ")
            os.system('cls')
            if(int(loop_check) != 1):
                break
    
    def operate(operator,first,second):
        string = f"global var1; var1 = {first}{operator}{second}"
        exec(string)
        print(var1)
    
    main()
except:
    print("Error, try again\n")
    main()
