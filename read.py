with open("Weathervalues.txt","r") as file:
  T=int(file.readline().strip())
  H=int(file.readline().strip())
  W=int(file.readline().strip())
WR= (0.5*T*T)-(0.2*H)+(0.1*W)-15
print(WR)
if WR > 300:
  print("Sunny")
elif 200<WR<=300:
  print("Cloudy")
else:
  print("Rainy")
