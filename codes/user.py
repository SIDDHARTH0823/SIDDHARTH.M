T=int(input("Enter the value of temperature in Celcius"))
H=int(input("Enter the value of humidity in percentage"))
W=int(input("Enter the windspeed in km/hr"))
WR= (0.5*T*T)-(0.2*H)+(0.1*W)-15
print(WR)
if WR > 300:
 print("Sunny")
elif 200<WR<=300:
 print("Cloudy")
else:
 print("Rainy")