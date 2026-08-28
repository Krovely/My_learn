elements = [1, 2, 3, 4, 5, 6]
#elements = [1, 2, 3] 
#elements = [1, 2, 3, 4, 5]
#elements = [1]
#elements = []
try_elements = len(elements)%2
if elements == []:
    elements = [[],[]]
    print(elements)
elif try_elements == 0:
    len_ = len(elements)//2
    el_1 = elements [0:len_]
    el_2 = elements [len_:len(elements)]
    elements = [el_1,el_2]
    print(elements)
elif len(elements) == 1:
    elements.append([])
    print(elements)
else :
    len_ = len(elements)//2+1
    el_1 = elements[0:len_]
    el_2 = elements[len_:len(elements)]
    elements = [el_1,el_2]
    print(elements)
