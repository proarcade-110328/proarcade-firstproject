print("This is an simple calculator.")
print("Enter any numbers. Don't enter Alphabets.")
def fnumberaction():
    while True:
        firstnumber = input("What is your first number?")
        try:
            firstnumber = float(firstnumber)
            return firstnumber
        except ValueError:
            print(f"'{firstnumber}' is NOT a number!\n")
def snumberaction():
    while True:
        secondnumber = input("What is your second number?")
        try:
            secondnumber = float(secondnumber)
            return secondnumber
        except ValueError:
            print(f"'{secondnumber}' is NOT a number!\n")
def arithaction(firstnumber, secondnumber):
    while True:
        math = input("What kind of calculation do you want to do?")
        if math == "+":
            answer = firstnumber + secondnumber
        elif math == "-":
            answer = firstnumber - secondnumber
        elif math == "*":
            answer = firstnumber * secondnumber
        elif math == "/" and secondnumber != 0:
            answer = firstnumber / secondnumber
        elif math == "/" and secondnumber == 0:
            print("You can't do this since your second number is 0.\n")
            continue
        else:
            print("You can't do math with that.\n")
            continue
        print(answer)
        return answer
while True:
    firstnumber = fnumberaction()
    secondnumber = snumberaction()
    answer = arithaction(firstnumber, secondnumber)
    again = input("Do you want to do another? (y/n)").lower()
    if again != "y":
        print("GoodBye!")
        break