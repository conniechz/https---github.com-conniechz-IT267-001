from area import Area

b = float(input('Enter Base : '))
h = float(input('Enter High : '))

aobj = Area()
aobj.base = b
aobj.high = h
print(f'Area = {aobj.compute_area()}')