#exercise 1.1
pi = 3.14159
r = 5
v = 4/3*pi*r**3
print ("the volume of a sphere with radius 5 is {:.2f}.".format(v))

#exercise 1.2
price = 24.95
books = 60
wholesale = price*books*.6+3+.75*(books-1)
print ("the totale wholesale cost for 60 copies is {:.2f}.".format(wholesale))

#exercise 1.3

start_time_hr = 6+52 / 60
easy_pace_hr = (8+15/60) / 60
tempo_hr = (7+12 / 60) / 60
running_time_hr = 2 * easy_pace_hr + 3 * tempo_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec = (breakfast_min - int(breakfast_min))*60

print ('Breakfast time is {:02d}:{:02d}:{:02d}.'.format(
        int(breakfast_hr),
        int(breakfast_min),
        int(breakfast_sec)))

#exercise 1.4
increase = (89-82) / 82 * 100
print("the percentage of the increase is {:04.1f}%.".format(increase))