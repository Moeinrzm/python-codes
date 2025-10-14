class Calculator:

    def sum(self,num1,num2):
        return num1+num2
    def divide(self,num1,num2):
        if num2==0:
            return ("Error,Division to zero")
        return num1/num2
    def subtract (self,num1,num2):
        return num1-num2
    def Multiply(self,num1,num2):
        return num1*num2

def main():
    calculator=Calculator()
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")    
    print("5. enter to exit ")
        
    while 1:
        choice=input("Enter choice (1/2/3/4,5)")
        if choice=='5':
            print("program closed")
            break
        try:
            num1=float(input("enter first number"))
            num2=float(input("enter second number"))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue 

        if choice == '1':
            result = calculator.sum(num1, num2)
            print(f"The result is: {result}")
        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print(f"The result is: {result}")
        elif choice == '3':
            result = calculator.Multiply(num1, num2)
            print(f"The result is: {result}")
        elif choice == '4':
            result = calculator.divide(num1, num2)
            print(f"The result is: {result}")
        else:
            print("Invalid choice!")



main()
        
