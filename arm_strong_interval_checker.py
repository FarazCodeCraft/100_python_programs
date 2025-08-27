# num_start = int(input("Enter a start number: "))
# num_end = int(input("Enter a end number: "))
# for i in range(num_start, num_end + 1):
#     len_num = len(str(i))
#     sum = 0
#     for j in str(i):
#         sum += int(j) ** len_num
#     if sum == i:
#         print(f"{i} is an Armstrong number")



num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
for i in range(int(num1), int(num2) + 1):
    len_num = len(str(i))
    sum = 0
    for j in str(i):
        sum += int(j) ** len_num
    if sum == i:
        print(f"{i} is an Armstrong number")







