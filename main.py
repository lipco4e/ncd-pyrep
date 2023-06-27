def add(a, b):
    sum = a + b
    print("The sum of ", a, "+", b, "is =", sum)

def comsoon():
    print ("Feature coming soon, thank you for understanding me!")

#main loop

name = input("Enter your name please ")
while True:
       #choice = 0
    print("")
    print("Hello", name, "\n")
    print("How can i help you? ", "\n")

    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        comsoon()
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        comsoon()
    elif choice == "d" or choice == "D":
        print("Division" )
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        comsoon()
    elif choice == "e" or choice == "E":
        print("program ended")
        quit()
