import string
sec_ = True
while sec_ is True:
    sec_ = int(input('ENTER_sec --> '))
    if sec_ < 0 or sec_ > 8640000:
        sec_ = True
#sec_ = 0 #-> 0 днів, 00:00:00
#sec_ = 224930 #-> 2 дні, 14:28:50
#sec_ = 466289 #-> 5 днів, 09:31:29
#sec_ = 950400 #-> 11 днів, 00:00:00
#sec_ = 1209600 #-> 14 днів, 00:00:00
#sec_ = 1900800 #- > 22 дні, 00:00:00
#sec_ = 8639999 #-> 99 днів, 23:59:59
#sec_ = 22493 #-> 0 днів, 06:14:53
#sec_ = 7948799 #-> 91 день, 23:59:59
min_ = sec_//60
sec_ = sec_%60
print('sec - ',sec_)
print('min - ',min_)
h=min_//60
min_end=min_%60
print('\n')
print(f'{min_}min in format h_min ==> {h}h {min_end}min')
days=h//24
h=h%24
print()
print(f'{days} days {h}:{min_end}:{sec_}')
if days % 10 == 1 and days % 100 != 11 :
    days = str(days)+' день'
    print(days)
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    days = str(days)+' дні'
    print(days)
else:
    days = str(days)+' днів'
    print(days)
sec_ = str(sec_).zfill(2)
min_end = str(min_end).zfill(2)
h    = str(h).zfill(2)
tim_d_h_m_s = string.Template('$d $h:$m:$s')
res_ = tim_d_h_m_s.substitute(d = days ,h = h ,m = min_end , s = sec_)
print(res_)