#Author Sean Salafia 2/1/23

'''
a. at least one function must use a dictionary (can be as the argument) DONE
b. you must use at least 3 different lists (1)
c. you must use a for loop, a while loop, and enumerate
d. you must use at least 5 built in functions (like lower()).
e. you must get user input at least twice   (1)
f. your functions all must return at the end.
g. at least 5 of the functions must be over 15 (logical) lines of code in length)   (1,2)
4. In the lab_12-7.py file, call (print) at least 4 of the functions. You may
choose any method to do this.
'''




#----------------------------------------------------------------------------------------------------------------------------------------
#Lab 11-2
def grades_code():
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
    return()
#----------------------------------------------------------------------------------------------------------------------------------------
#Lab 6-6
#user inputs unique words
def inputs_into_list():
    a = input("Input a unique word: ")
    b = input("Input a unique word: ")
    c = input("Input a unique word: ")
    d = input("Input a unique word: ")
    e = input("Input a unique word: ")
    #convert those inputs into a list
    x = [a, b, c, d, e]
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    len_d = len(d)
    len_e = len(e)

    y = [len_a, len_b, len_c, len_d, len_e]
    print (y)
    return()


#----------------------------------------------------------------------------------------------------------------------------------------
#Lab 10-6 

def add_nums(numbers):
    num_list = []
    try:
        user_input = input("Input a list of numbers: ")
        num_list.append(numbers)
    except TypeError:
        print("Error Encountered. Please enter a valid number.")
    except IndexError:
        print("Error Encountered. Please enter a valid number.")
    finally:
        print("The number list is: " + num_list)
        print("Your final input was: " + user_input)
    return()
print(add_nums[1,2,3,4,5])



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#



#----------------------------------------------------------------------------------------------------------------------------------------
#