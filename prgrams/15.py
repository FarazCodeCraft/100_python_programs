# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# reult = factorial(5)
# print("Factorial is:", reult)


# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print("Factorial is:", factorial)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)         #    5 * 4 * 3 * 2 * 1 = 120
result = factorial(5)   
print("Factorial is:", result)
