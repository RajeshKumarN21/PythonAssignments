num = int(input("Enter a natural number "))
i=0
while i<num:
   # print("i=",i)
    i=i+1
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
