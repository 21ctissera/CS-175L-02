# Chrishen Tissera
# CS175L
# Restaruant program
A="Joe's Gourmet Burger"
B="Main Street Pizza Company"
C="Corner Café"
D="Mama's Fine Italian"
E="The Chef's Kitchen"

true = 'Yes'
false = 'No'

Q_1 = input("Is anyone in your party a vegetarian? ")
print("   ")
Q_2 = input("Is anyone in your party a vegan? ")
print("   ")
Q_3 = input("Is anyone in your party gluten-free? ")
print("   ")
if Q_1==false and Q_2==false and Q_3==false:
    print("Here are your restaurant choices:")
    print("  ",A)
elif Q_1==true and Q_2==false and Q_3==true:
    print("Here are your restaurant choices:")
    print("  ",B)    
elif Q_1==true and Q_2==false and Q_3==false:
    print("Here are your restaurant choices:")
    print("  ",D)
elif Q_1==true and Q_2==true and Q_3==true:
    print("Here are your restaurant choices:")
    print("  ",C)
    print("  ",E)
else:
    print('ERROR: Make sure user inputs are only "Yes" or "No".')










    


    
