for i in range(1,101):
    if i%3==0:
        print("Fizz")
    elif str(i).find("3")!=-1:
        print("FizzBuzz")
    else:
        print(i)
