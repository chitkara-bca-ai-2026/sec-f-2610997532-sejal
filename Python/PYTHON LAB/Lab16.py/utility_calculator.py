print("===========================================================")
print("            ENTERPRISE MODULAR UTILITY CALCULATOR          ")
print("===========================================================")
history=[]
def add(a,b):
        return a+b
def subtract(a,b):
     return a-b
def multiply(a,b):
     return a*b
def divide(a,b):
     if b==0:
          return None
     else:
          return a/b
def modulus(a,b):
     return a%b     
        
while True:
    print("Select an opertaion:")
    print("1. Addition(+)")
    print("2. Subtrcation(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Modules / Remainder(%)")
    print("6. Power / Exponenetation(Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")


    
    choice=int(input("Enter Your Choice:"))
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    if choice==1:
            a=int(input("Enter the value of a:"))
            b=int(input("Enter the value of b:"))
            def ask_input():
                return (a,b)
            a,b=ask_input()
            print("a+b=",add(a,b))
    elif choice==2:
        def ask_input():
            return(a,b)
        a,b=ask_input()
        print("a-b=",subtract(a,b))
    elif choice==3:
        def ask_input():
            return(a,b)
        a,b=ask_input()
        print("a*b=",multiply(a,b))
    elif choice==4:
        def ask_input():
            return(a,b)
        a,b=ask_input()
        print("a/b=",divide(a,b))
    elif choice==5:
        def ask_input():
            return(a,b)
        a,b=ask_input()
        print("a%b=",modulus(a,b))
              
                 

        
         