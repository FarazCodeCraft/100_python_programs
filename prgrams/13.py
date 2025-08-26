interval_start = int(input("Enter start of interval: "))
interval_end = int(input("Enter end of interval: "))    
for num in range(interval_start, interval_end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)