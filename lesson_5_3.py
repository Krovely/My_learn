import string
elements = input('--> ')
elements_0 = ''
for i in elements:
    if i not in string.punctuation:
        elements_0 += i
el_words = elements_0.split()
res_el = '#'
for i in el_words:
    res_el += i.capitalize()
if len(res_el)>140:
    res_el = res_el[:140]
print(res_el)
