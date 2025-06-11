def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def main():
    print("welcome to calc!")
    a=int(input("Enter the first number :"))
    b=int(input("Enter the second number :"))
    print(f"add :{add(a,b)}")
    print(f"sub :{sub(a,b)}")
    print(f"mul :{mul(a,b)}")
    print(f"div :{div(a,b)}")

if __name__ =="__main__":
    main()
