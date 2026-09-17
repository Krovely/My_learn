number_ = int(input('--> '))
#number_ = 999 #-> 2 
#number_ = 1000 #-> 0
#number_ = 423 #-> 8
#number_ = 33 #-> 9
#number_ = 25 #-> 0
#number_ = 1 #-> 1 
for i in range (100):
    if number_ <= 9:
        break
    res = 1
    for digit in str(number_):
        res *= int(digit)
    number_ = res
print(number_)
