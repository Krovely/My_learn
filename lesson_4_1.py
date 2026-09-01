elements = [0, 1, 0, 12, 3]
elements = [0] 
elements = [1, 0, 13, 0, 0, 0, 5]
elements = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
indx = 0
for i in elements:
    if i == 0:
        indx = indx + 1
for i in range(indx):
    elements.append(0)
    elements.remove(0)
print (elements)
print (indx)