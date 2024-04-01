class Calculator:
    # def __init__(self, num1, num2):
    #     self.num1=num1
    #     self.num2=num2

    def add(self,*args,**kwargs):
        # self.num1=args[0]
        # print(self.num1)
        n=int(input("Enter how  many numbers:"))
        print("Enter numbers to add:\n")
        total=0
        for x in range(0,n):
            a=int(input("Enter number:"))
            total+=a
        return total
   
    def sub(self,*args):
        n=int(input("Enter how many numbers:"))
        print("Enter numbers to subtract:\n")
        total=int(input("Enter number:"))
        for i in range(1,n):
            a=int(input("Enter number:"))
            total-=a
        return total
    
    def mul(self,*args):
        n=int(input("Enter how  many numbers:"))
        print("Enter numbers to multiply:\n")
        total=1
        for x in range(0,n):
            a=int(input("Enter number:"))
            total*=a
        return total    

    def div(self,*args):
        try:
            n=int(input("Enter how many numbers:"))
            print("Enter numbers to divide:\n")
            total=int(input("Enter number:"))
            for i in range(1,n):
                a=int(input("Enter number:"))
                total/=a
            return total
        except:
            print("**cannot divide by zero**")

    
cal=Calculator()

b=0
while(b!=5):
    print("\n**MENU**")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    c=int(input("Choose your option: "))
    if c==1:
        print("Result=",cal.add())
    elif c==2:
        print("Result=",cal.sub())
    elif c==3:
        print("Result=",cal.mul())
    elif c==4:
        print("Result=",cal.div())
    elif c==5:
        print("End of program!!")
        break
    else:
        print("Choose numbers 1/2/3/4/5")