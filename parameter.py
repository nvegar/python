def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:  
        if num % 2 != 0: 
            total += num
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7,8,9]))

#1 + 3 + 5 + 7 + 9 = 25