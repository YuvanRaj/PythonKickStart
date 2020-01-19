'''
Created on Jan 19, 2020

@author: Yuvaraj
'''

print("Iteration method 1")
list =[1,2,3,4,5]

for i in list:
    print(i)
    
print("Iteration method 2")
length=len(list)
for i in range(length):
    print(list[i])
    
print("Iteration method 3")
j=0
while j < length:
    print(list[j])
    j += 1