'''
Created on Jan 5, 2020

@author: Yuvaraj
'''

num=259
print(num)
reveed=0
digit=None
while num != 0:
    digit = num%10
    reveed = reveed*10+digit
    num=num//10

print(reveed) 
    