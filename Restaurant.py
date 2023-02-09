# Chrishen Tissera
# CS175L
# Restaruant program v2

keep_going = "Yes"

A="Joe's Gourmet Burger"
B="Main Street Pizza Company"
C="Corner Café"
D="Mama's Fine Italian"
E="The Chef's Kitchen"

true = 'Yes'
false = 'No'

while keep_going == "Yes":
    Q_1 = input("Is anyone in your party a vegetarian? ")
    print("   ")
    Q_2 = input("Is anyone in your party a vegan? ")
    print("   ")
    Q_3 = input("Is anyone in your party gluten-free? ")
    print("   ")
    if Q_1==false and Q_2==false and Q_3==false:
        print("Here are your restaurant choices:")
        print("  ",A)
        print("  ",B)
        print("  ",C)
        print("  ",D)
        print("  ",E)
    elif Q_1==true and Q_2==false and Q_3==true:
        print("Here are your restaurant choices:")
        print("  ",B)
        print("  ",C)
        print("  ",E)
    elif Q_1==true and Q_2==false and Q_3==false:
        print("Here are your restaurant choices:")
        print("  ",D)
        print("  ",B)
        print("  ",C)
        print("  ",E)
    elif Q_1==true and Q_2==true and Q_3==true:
        print("Here are your restaurant choices:")
        print("  ",C)
        print("  ",E)
    elif Q_1==true and Q_2==true and Q_3==false:
        print("Here are your restaurant choices:")
        print("  ",C)
        print("  ",E)
    else:
        print('ERROR: Make sure user inputs are only "Yes" or "No".')
    print("   ")

    keep_going = input("Enter 'Yes' if you would like to do another restaurant search (enter 'No' to end): ")

    if keep_going == "No":
        print("Thank You For Using Restaurant Code V2, Have a Nice Day!")
    










    


    
