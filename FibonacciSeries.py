n = int(input("Enter the number of terms: "))

#initialize first 2 terms
n1, n2 = 0, 1
count = 0

if(n <= 0):
    print("Enter valid number of terms!")
elif(n == 1):
    print("Fibonacci Sequence: ",n1)
else:
    print("Fibonacci Sequence: ")
    while(count < n):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
