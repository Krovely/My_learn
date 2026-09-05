import random
elements = []
len_elmns = random.randint(3,10)
for i in range (len_elmns):
    el_ = random.randint(1,9)
    elements.append(el_)
print(elements)
elements = [elements[0],elements[2],elements[-2]]
print(elements)