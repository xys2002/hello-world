#<Yunsheng Xu 2021-10-5>
#This program is to tell the number which user input is odd or even
def method(number):
    num=int(number)
    num_1=int(num/2)
    print(num,num_1)    #check if it is going on well
    if num!=num_1*2:
        print("odd")
    else:
        print("even")
Input=input("input:")
method(Input)
    