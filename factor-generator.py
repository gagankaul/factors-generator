#Welcome to the Factor Generator App

print("Welcome to the Factor Generator App")

state = True

while state:

    number = int(input("\nEnter a number to determine all factors of that number: "))

    factors_list = []

    for i in range(1,number+1):
        if number % i == 0:
            factors_list.append(i)
    
    print(f"\nFactors of {number} are:")
    for factor in factors_list:
        print(factor)

    print(f"\nIn Summary: ")
    list_length = int(len(factors_list) / 2)

    for i in range(list_length):
        print(f"{factors_list[i]} * {factors_list[-i-1]} = {number}")

    #Alternative method using while loop
    # index1 = 0
    # index2 = -1
    # count = 1
    # while count <= list_length:
    #     print(f"{factors_list[index1]} * {factors_list[index2]} = {number}")
    #     index1 += 1
    #     index2 -= 1
    #     count += 1
    
    choice = input("\nRun again (y/n): ").lower().strip()
    if choice == "y":
        continue
    else:
        state = False
        print("Thank you for using the program. Have a great day!")