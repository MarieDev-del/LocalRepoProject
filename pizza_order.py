#pizza order program

#small size pizza = 100Rs
#medium size pizza = 200Rs
#large size pizza = 300Rs

#pepperoni for small pizza = 30Rs
#pepperoni for medium or large pizza = 50Rs
#extra cheese for any size pizza = 20Rs

size = input("Choose a size you want,(S/M/L)? ")
bill = 0 

if size == 'S' or size == 's':
    bill += 100 
    print("Small pizza is 100Rs")
elif size == 'M' or size == 'm':
    bill += 200 
    print("Medium size is 200Rs")
else:
    bill += 300 
    print("large pizza is 300Rs")


add_pepperoni = input("Do you want pepperoni,yes/No? ")

if add_pepperoni == 'Yes' or add_pepperoni == 'yes':
    if size == 'S' or size == 's':
        bill += 30 
        print("Pepperoni for small pizza cost 30Rs")
    else:
        bill += 50 
        print(f"Pepperoni for {size} is 50Rs")

extra_cheese = input("Do you want extra cheese,Yes/No? ")

if extra_cheese == 'Yes' or extra_cheese == 'yes':
    bill += 20
    print("Extra cheese is 20 Rs")

print(f"Your final bill is {bill}Rs ")

