for i in range(1,101):
    if int(i)%3==0:
        print("Fizz")
    elif int(i)%5==0:
        print("Buzz")
    elif int(i)%3==0 and int(i)%5==0:
        print("FizzBuzz")
    else:
        print(str(i))
