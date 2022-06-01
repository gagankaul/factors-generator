#Welcome to the Factor Generator App

print("Welcome to the Factor Generator App")

state = True

while state:

    number = int(input("\nEnter a number to determine all factors of that number: "))

    divisor = 1
    factors_list = []

    while divisor <= number:
        if number % divisor == 0:
            factors_list.append(divisor)
        divisor += 1
    
    print(f"\nFactors of {number} are:")
    for factor in factors_list:
        print(factor)

    print(f"\nIn Summary: ")
    combo_length = int(len(factors_list) / 2)
    index1 = 0
    index2 = -1
    count = 1
    while count <= combo_length:
        print(f"{factors_list[index1]} * {factors_list[index2]} = {number}")
        index1 += 1
        index2 -= 1
        count += 1
    
    choice = input("\nRun again (y/n): ").lower().strip()
    if choice == "y":
        continue
    else:
        state = False

