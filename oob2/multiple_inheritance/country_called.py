from country import Country

#create countries
#Thailand lat = 13.7649136 , 100.5360959
#population = 70,078,203
#area = 513,120
#temp = 32 C

c1 = Country('Thailand',513120,70078203)
c1.setcordinate(13.7649136,100.5360959)
c1.setcelsuls(32)
c1.showdetail()

c2 = Country('Japan',377,930)
c2.setcordinate(35.652832,139.839478)
c2.setcelsuls(34)
c2.showdetail()

c3 = Country('North America',42,549,000)
c3.setcordinate(48.1667,100.1667)
c3.setcelsuls(26)
c3.showdetail()