"""Joseph Nguyen PSID: 1779987"""
# zyLabs 5.19.1 #

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

first_service = input("Select first service:\n").capitalize()
second_service = input("Select second service:\n").capitalize()
print()

print("Davy's auto shop invoice\n")

price1 = 0
if first_service == "Oil change":
    price1 = 35
    print("Service 1:", first_service + ", $" + str(price1))
elif first_service == "Tire rotation":
    price1 = 19
    print("Service 1:", first_service + ", $" + str(price1))
elif first_service == "Car wash":
    price1 = 7
    print("Service 1:", first_service + ", $" + str(price1))
elif first_service == "Car wax":
    price1 = 12
    print("Service 1:", first_service + ", $" + str(price1))
elif first_service == "-":
    print("Service 1: No service")

price2 = 0
if second_service == "Oil change":
    price2 = 35
    print("Service 2:", second_service + ", $" + str(price2))
elif second_service == "Tire rotation":
    price2 = 19
    print("Service 2:", second_service + ", $" + str(price2))
elif second_service == "Car wash":
    price2 = 7
    print("Service 2:", second_service + ", $" + str(price2))
elif second_service == "Car wax":
    price2 = 12
    print("Service 2:", second_service + ", $" + str(price2))
elif second_service == "-":
    print("Service 2: No service")
print()
print("Total: $" + str(price1+price2))
