def calculator():
    operation = input('''
    Please type in the match operation you would like complete:
    + for addition"
    - for sustraction
    * for multiplicacion
    / for division
    ''')



    number_1 = int(input())
    number_2 = int(input())

    #addition
    if operation == "+":
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    #sustraction
    elif operation == "-":
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    #multiplication
    elif operation == "*":
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    #division
    elif operation == "/":
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print("Not a valid operation")


def again():
    calc_again = input('''
    Do you want to calculate again?
    please type Y for Yes or N for No.
    ''')
    if calc_again.upper == "Y":
        calculate()
    elif cal_again.upper == "N":
        print("See you later")
    else:
        again()
