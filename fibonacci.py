num = int(input("Enter a number: "))    
a, b = 0, 1
print(f"Fibonacci sequence up to {num}:")
my_list = [a, b]
if num == 1:
    print(a)
else:
    # print(a)
    # print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b = c
        my_list.append(c)
    print(my_list)
        
        # print(i)
        # c = a + b
        # a = b
        # b = c
        # print(b)


# for i in range(2,10):
#     print(i)
