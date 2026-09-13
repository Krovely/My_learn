import string
import keyword
elements = input('-> ')
bull_name_el = True
if elements == '':
    bull_name_el = False
elif elements in keyword.kwlist or elements[0].isdigit() or (set(elements) == {'_'} and len(elements) > 1):
    bull_name_el = False
else:
    for i in elements:
        if i.isupper() or i in string.punctuation.replace('_','') or i.isspace():
            bull_name_el = False
            break
print(bull_name_el)