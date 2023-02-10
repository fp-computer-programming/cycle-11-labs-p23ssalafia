#Author Sean Salafia 2/1/23

'''
a. at least one function must use a dictionary (can be as the argument) DONE
b. you must use at least 3 different lists (DONE)
c. you must use a for loop, a while loop, and enumerate
d. you must use at least 5 built in functions (like lower()).
e. you must get user input at least twice   (1)
f. your functions all must return at the end.
g. at least 5 of the functions must be over 15 (logical) lines of code in length)   (DONE)
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
            str(grades)
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
#Lab 10-5

def add_foods(food):
    six_letter_foods = []
    not_foods = []
    short_foods = []
    for index,variables in enumerate(food):
        try:
            food_string = str(variables)
            if len(food_string) >= 8:
                six_letter_foods.append(food_string)
            else:
                short_foods.append(food_string)
        except TypeError:
            not_foods.append(food_string)
        except IndexError:
            short_foods.append(food_string)

    return("Six Letter Foods: ", six_letter_foods,"Not Foods :", not_foods,"Short Foods: ", short_foods)

#----------------------------------------------------------------------------------------------------------------------------------------
#Lab 10-4

def indexed_names(names):
    indexed_names = []     #Creates open list to be modified
    for index,name in enumerate(names):
        indexed_names.append("{}: {}".format(index,name))   #(Searched up) Format fucntion combines the two strings into one for the list to be appended 
        continue    # Loops back to the beginning to complete checking the whole list input
    return indexed_names



#----------------------------------------------------------------------------------------------------------------------------------------
#Lab 6-3
def colors_list():
    list_of_colors = ["red", "orange", "yellow", "green"] 
    print (list_of_colors)
    #Extend the list by using the extend method to add to the list. Print list.
    list_of_colors.extend (["blue", "indigo", "violet"])
    print (list_of_colors)
    #Add sky blue to the end of the list by appending and printing.
    list_of_colors.append ("sky blue")
    print (list_of_colors)
    #Add magenta to the 3rd index position
    list_of_colors.insert (3,"magneta")
    print (list_of_colors)
    #Copy the list of colors
    copy_of_list_of_colors = list_of_colors[:]
    print (list_of_colors)
    print (copy_of_list_of_colors)
    #Remove one element from the copy of the list
    copy_of_list_of_colors.remove ("red")
    print(copy_of_list_of_colors)
    copy_of_list_of_colors.remove ("green")
    print(copy_of_list_of_colors)
    return()


#----------------------------------------------------------------------------------------------------------------------------------------
# Lab 8-4
def cumulative_sum(x):
    #where the sum will be counted
    total = 0
    #starting value for the while loop
    start_count = 0
    while start_count < int(x):
        start_count += 1
        total += start_count
    return total



#----------------------------------------------------------------------------------------------------------------------------------------
#10-2
def multiples_of_3():
    n = []      #Creates open list

    while True:             #While true
        input_number = int(input("Input number here: "))    #User inputs #
        if input_number == -1:      #If it is -1, code breaks
            break
        elif input_number % 3 == 0:     #If It is divisible by 3, appends list to add the number
            n.append(input_number)
        else:                       #Else, do the continue function which takes it back to the top letting the user restart the loop.
            continue

    print("Multiples of 3: ", n)        #Prints multiples of 3
    return()


#----------------------------------------------------------------------------------------------------------------------------------------
#8-6
def factorial(num):
    count = 1
    for n in range(1, num+1):
        count *= n
    return count

#----------------------------------------------------------------------------------------------------------------------------------------
#Lab 8-4
def cumulative_sum(x):
    #where the sum will be counted
    total = 0
    #starting value for the while loop
    start_count = 0
    while start_count < int(x):
        start_count += 1
        total += start_count
    return total



#----------------------------------------------------------------------------------------------------------------------------------------
#Lab 8-1
def invite_to_party(names):
    for name in names:
        print("Hi " + name + ", I'd like to invite you to my party! Please let me know if you can make it.")
    return names