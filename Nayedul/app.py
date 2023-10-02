while True:
    # Print Helloworld
    print("Hello World\n")

    a = int(input("Enter a num: "))

    c=input("Enter the Operator: ")

    b=int(input("Enter a num: "))


    if c=='-':
        print(a-b)
    elif c=='+':
        print(a+b)
    elif c=='*':
        print(a*b)
    elif c=='/':
        print(a/b)
    elif c=='^':
        print(a**b)
    elif c=='//':
        print(a//b)
    elif c=='%':
        print(a%b)
    else:
        print("Operator Out Of Bound")
    print('\n')
    
