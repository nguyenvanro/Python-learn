from math import sqrt

while True:
    number1 = input("Input Number a: ")
    if number1.isnumeric() == False:
        print("LỖi ")
    number2 = input("Input Number b: ")
    if number2.isnumeric() == False :
        print("LỖI ")
    elif number1 == number2:
        print("Lỗi a = b ")
    else:
        j=[range(int(number1), int(number2))]
        for i in range(int(number1), int(number2)):
            if (i%3==0) and (sqrt(i)* sqrt(i) != i):
                j.append(str(i))
        print(list(j))
        break
    
