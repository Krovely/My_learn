elements = [12,3,4,10]
#elements = [1]
#elements = []
#elements = [11,0,1,2,3,4,5,6,7,8,9,10]
#elements = [1,'2',0,'',]
try_elements =[]
print(elements)
if elements == try_elements:
    print(elements)
else:
    l_elements = len(elements)
    first_last_element = elements[0]
    elements.insert(l_elements,first_last_element)
    elements.remove(first_last_element)
    print(elements)