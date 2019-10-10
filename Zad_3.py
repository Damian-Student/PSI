from datetime import datetime

print('{}  {}'.format('beforSpace', 'afterDoubleSpace'))
print('{:>24}'.format('24_chars'))
print('{:.5}'.format('JustFive!'))
print('{second} {last}'.format(first='Shall', second="Not", last='Pass!'))
dt = datetime(2001, 2, 3, 4, 5)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))
