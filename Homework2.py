from ast import literal_eval
coords = [literal_eval(coord) for coord in input("Please write your coordinates in the 0,0 1,2 format:").split()]
print("You have selected:", coords) 
index=0
length=len(coords)
xler=zip(*coords)
xler2=list(xler)
numerator=sum(list(xler2)[0])/len(list(xler2)[0])
denumerator=sum(list(xler2)[1])/len(list(xler2)[1])
mass=[(numerator,denumerator)]
print("The center of mass is:",mass)
import math
mesafeler=[]
while index < length:
    start=coords[index]
    #end=coords[index+1]
    x1=start[0]
    #x2=end[0]
    y1=start[1]
    #y2=end[1]
    distance= math.sqrt(abs(numerator-x1)+abs(denumerator-y1))
    mesafeler.append(distance)
    index=index+1
farklar=zip(coords,mesafeler)
fark=list(farklar)
Max=max(fark, key=lambda x:x[1])
print("The farthest coordinates and the distance is:", Max)
print("The closest coordinates and the distance is:", min(fark, key=lambda y:y[1]))
#This code works with 3 and more coordinates yet doesn't work with 2 coordinates.     
  
  

