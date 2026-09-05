elements = [0, 1, 7, 2, 4, 8]
elements = [1, 3, 5]
elements = [6]
elements = []
sum_el = 0
result_el = 0
if elements == []:
    result_el == 0
    print(result_el)
else:
    for i in range(0, len(elements), 2):
        sum_el += elements[i]
    end_el = elements.pop()
    result_el = sum_el*end_el
    print(result_el) 



