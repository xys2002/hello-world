#<Yunsheng Xu 2021-10-6>
#This program is written for finding multiples of 3 and 5 from 1 to 100
def method(number):
    num=int(number)
    num_3=int(num/3)
    num_5=int(num/5)
    print(num,num_3,num_5)
    if num==num_3*3:           #only 3,only 5,3 and 5,none 
        if num==num_5*5:
            print("FizzBuzz")
        else:
            print("Fizz")
    if num==num_5*5 and num!=num_3*3:           
        print("Buzz")
    else:
        print("")
for i in range(1,101):
    method(i)
