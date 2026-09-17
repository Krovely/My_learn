import string
elements = input('--> ')
first_el , last_el  = elements.split('-')
first_el_indx = string.ascii_letters.index(first_el)
last_el_indx  = string.ascii_letters.index(last_el )
res_el = string.ascii_letters[first_el_indx : last_el_indx + 1]
print(res_el)
