#significant
print("1 + ")
print("2 -")
print("3 *")
print("4 /")
print("5 %")
#inputs
choice = input("select your choice ")
number_1 = float(input("put your number : " ))
number_2 = float(input("put your number : " ))
#output
if choice == "1":
    print("=", str(number_1+number_2))
elif choice == "2":
    print("=",str(number_1-number_2))
elif choice == "3":
    print( "=",str(number_1*number_2))
elif choice == "4":
    if number_2 == 0:
        print("error")
    else:
        print( "=",str(number_1/number_2))
elif choice == "5":
    if number_2 == 0:
        print("error")
    else:
        print("=" ,str(number_1%number_2))

