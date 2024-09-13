'''you can use the function below to express all prime numbers in python list.
and also with max and min function you can express max and min numbers in a python list.
and wir using if and for loop here'''

numbers = [10, 15, 3, 7, 9, 11, 13, 17, 20]
print(max(numbers))
print(min(numbers))
numbers.remove(9)
print(numbers)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def non_prime_numbers(numbers):
    return [num for num in numbers if not is_prime(num)]

# Example usage
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
non_primes = non_prime_numbers(numbers)
print("Here below is the list without prime numbers")
print(non_primes)  # Output: [4, 6, 8, 9, 10]
non_primes.insert(1, 2)
print(non_primes)

# Example for list item sum
for i in range(0, len(numbers)):
    total = total + numbers[i]
print("sum of all elements in given  list", total)


numbers = [1, 2, 3, 4, 5]
print(numbers[2])
print(numbers[4])
'''value methode for add integer in pyton list '''
# Value
first_list = list([1, 2, 3, 4, 5, 6, 7, 88, 99, 100])
second_list = list()
for integer in first_list:
    if integer % 2 == 0:
        second_list.append(integer)
    else:
        second_list.append(integer + 1)

print('Hier is only even numbers set:',second_list)
'''Hier wir use reference'''
#Reference
for integer in range(len(first_list)):
    first_list[integer] = first_list[integer] + 1
print('i wont one add in first list for alles integer:',first_list)





