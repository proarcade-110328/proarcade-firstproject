print("This is an simple calculater.")
print("Enter any numbers. Don't enter Alphabets.")
firstnumber = input("First, What is your first number?")
if isinstance(firstnumber, (int,float)) == 0:
    print(firstnumber + " is your first number.")
else: print("This is not a number.")