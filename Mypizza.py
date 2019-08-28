print("Input the length of the pizza: ", end=" ")
inputVal = input()
radius = float(inputVal)
Aofpizza = radius * radius
numberofpeople = int (Aofpizza/100)
if numberofpeople < 1:
print("The pizza can only serve one family member")
else:
print("The pizza can serve " + str
(numberofpeople) + " persons")