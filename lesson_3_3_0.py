elements = [1, 2, 3, 4, 5, 6]
#elements = [1, 2, 3] 
#elements = [1, 2, 3, 4, 5]
#elements = [1]
#elements = []
elements.reverse()
el_1 = elements[0:len(elements)//2] 
el_2 = elements[len(elements)//2:len(elements)]
el_1.reverse()
el_2.reverse()
elements = [el_2,el_1]
print(elements)