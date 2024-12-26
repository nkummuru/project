#import random
from random import randint,choice,sample

random_list = []

for i in range(10):
    random_list.append(randint(0,1000))

#random_list2 = choice(range(1000),k=6)
random_list3 = sample(range(1000),k=6)

print(random_list,end="\n")
#print(random_list2,end="\n")
print(random_list3,end="\n")