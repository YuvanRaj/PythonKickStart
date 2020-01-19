'''
Created on Jan 18, 2020

@author: Yuvaraj
'''
import math
num = int(input("Enter a number: "))
invalue=num
reveed=0
digit=None
count = (int) (math.log10(num) + 1);
while num != 0:
    reveed = reveed+ math.pow((num % 10), count);   
    num=num//10

if invalue == reveed:
    print("adam number");
else:
    print("not adam number")