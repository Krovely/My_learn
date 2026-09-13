import string
elements = input('--> ')
elements_0 = ''
for i in elements:
    if i not in string.punctuation:
        elements_0 += i
el_words = elements_0.split()
usless_0 = '#'
for i in el_words:
    usless_0 += i.capitalize()
if len(usless_0)>140:
    usless_0 = usless_0[:140]
print(usless_0)