def evenOdd(number):
    if number%2 == 0:
        print('Even Number')
    else:
        print('Odd Number')
        
        
def factorial(number):
    f = 1
    for i in range(1,number+1):
        f = f * i
    print(f)