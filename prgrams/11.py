num = int(input("Enter a number: "))
if num < 2:
    print("it is not a prime number")
elif num > 2:
    for i in range(2, num):
        if num % i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")