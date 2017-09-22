name = input("What is your name?")
age = int(input("what is your age {0}?".format(name)))

if age > 18 and age < 31:
    print("huray, you can enjoy the holiday")
else:
    print("I am sorry, you are not allowed for this holiday")
