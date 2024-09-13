# I want chosse  to do the second simplay way for fibonacci calculated

'''Fibonacci saqeunce :
saqeunce of number where a number is the sum of the 2 numbers that came before it:
The saqeunce 'first digits are 0 and 1.
index:    1, 2, 3, 4, 5, 6, 7, 8, 9 ....
fibonacci:0, 1, 1, 2, 3, 5, 8, 13, 21 ...

Note: The zero is someteims not montioned '''

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

print(fibonacci(int(input('place enter a number:'))))              #pro
for x in range(int(input('place enter a number:'))):                #pro
    print(fibonacci(x))

# I wonto builden a Fabonacci formula:
print('which number do you want to calculate in Fibonacci, Enter here:')

# We have a function in math called Fibonacci: we can use this function to calculate different numbers.
#the function as already defined under , hier 1.618034 is fibancci´s constant

def f(x):
    y = (pow(1.618034, x)-pow((1-1.618034), x))/2.2360679774997896964091736687313
    return y

y = f(int(input('plase enter a  nummber for fibonacci calculated :')))
print(round(y))
c = int(input('plase enter a number for  series fibonacci calculated:'))
for x in range(c):
    print(round(f(x)))

print('The first calculated is end it')







