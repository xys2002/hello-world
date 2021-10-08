#<Yunsheng Xu 2020-10-06>
#This program displays the estimation of pi
import random


def estimate_pi(precision):
    #init vars
    p=int(precision)
    hit=0
    total=0
    PI=0          #hit/total*4
    x=random.random()
    y=random.random()

    for total in range(1,1000000):
         x=random.random()
         y=random.random()
         if x*x+y*y-x-y<=-0.25: #(x-0.5)^2+(y-0.5)^2<=0.25
             hit=hit+1

         PI=hit/total*4

    PI=round(PI,p)
    print(PI)



p=input("precision:")
estimate_pi(p)