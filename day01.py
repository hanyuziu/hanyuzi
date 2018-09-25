'''
#di yi ti
celsius = eval(raw_input('>>'))
fahrenheit = (9.0 / 5.0) * celsius + 32
print(fahrenheit)



#di er ti
radius,length = eval(raw_input('>>'))
area = radius * radius * 3.1415926
volume = area * length
print(area,volume)




#di san ti
feet = eval(raw_input('>>'))
meters = feet * 0.305
print(meters)



#di si ti
M,initialTemperature,finalTemperature = eval(raw_input('>>'))
Q =M * (finalTemperature - initialTemperature) * 4148
print(Q)



#di wu ti
balance,interest = eval(raw_input('>>'))
rate = balance * (interest / 1200)
print(rate)




#di liu ti
v0,v1,t = eval(raw_input('>>'))
a = (v1 - v0) / t
print(a)



#di qi ti
a = eval(raw_input('>>'))
a1 = a * (1 + 0.00417)
a2 = (a + a1) * (1 + 0.00417)
a3 = (a + a2) * (1 + 0.00417)
a4 = (a + a3) * (1 + 0.00417)
a5 = (a + a4) * (1 + 0.00417)
value = (a + a5) * (1 + 0.00417)
print(value)
'''


#di ba ti
a = eval(raw_input('>>'))
sum = ((a% 10) + ((a // 10) % 10) + (a // 100))
print(sum)
