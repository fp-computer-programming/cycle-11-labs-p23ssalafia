#Author: Sean Salafia 1/31/23

grades = {'Midyear Project Presention':93,'Midyear Project Proposal':100,'Midyear Project Code':94.2,'Mid Year Project Reflection':100} #Creates dictionary

print(grades.values())  #Prints all grades received

print('---------------------------------------------------------------------------------------------------------------------------')


for values in grades: 
    print(values)       #Prints the names of all the assignments


print('---------------------------------------------------------------------------------------------------------------------------')
print('Scores above 70:')
for keys,values in grades.items():  #If a value is more than 70, prints the assignment and score
    if values >= 70:
        print(keys,values)

print('---------------------------------------------------------------------------------------------------------------------------')
print('Scores below 50: ')
for keys,values in grades.items():      #If a value is less that 50, prints the Assignment and score
    if values <=50:
        print(keys,values)