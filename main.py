try:
    import os
    # A simple calculator
    print("Welcome to Calculator")
    def main():
        while True:
            choice = input("Press \n 1 to Add \n 2 to Sub \n 3 to Multiple \n 4 to divide \n :")
            num1 = input("Enter first no : ")
            num2 = input("Enter second no : ")
            ops = ['+','-','*','/']
            operate(ops[int(choice)],num1, num2)
            loop_check = input("Enter 1 to Try Again : ")
            if loop_check != '1':
                break
    
    def operate(operator,first,second):
        exec(f"global var1; var1 = {first}{operator}{second}")
        print(var1)
    main()
except:
    print("Error, try again\n")
    main()
