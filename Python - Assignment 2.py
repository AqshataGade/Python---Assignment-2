#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Exercise 1: Mailing Address
## Create a program that displays your name and complete mailing address formattedin the manner that you would usually see it on the outside of an envelope. 
## Your program does not need to read any input from the user.

name = "Aqshata"
address = "204, GitHub Apartment \nNear Jupyter Notebook \nPython Road (w)"
print("To: {},\nAddress: {}".format(name,address))


# In[2]:


## Exercise 2: Hello. 
#### Write a program that asks the user to enter his or her name. 
#### The program should respond with a message that says hello to the user, using his or her name.

user_name = input("Please Enter your name: ")
print("Hi ",user_name,", Thank you for joining the session.")


# In[10]:


## Exercise 3: Area of a Room
## Write a program that asks the user to enter the width and length of a room. Once the values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating-pointnumbers. 
## Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.
width = float(input("Please enter the width of room in feet: "))
length = float(input("Please enter the height of room in feet: "))
area = width*length
print("The area of room is", area,"square feet which has been calculated using the formula area = width * length")


# In[11]:


## Exercise 4: Area of a Field
## Create a program that reads the length and width of a farmer’s field from the user in feet. 
## Display the area of the field in acres. Hint: There are 43,560 square feet in an acre.

width = float(input("Please enter the width of room in feet: "))
length = float(input("Please enter the height of room in feet: "))
area = width*length
area_in_acre = round((area/43560),2)
print("The area of room is", area_in_acre,"acre which has been calculated using the formula area = (width * length)/43560")


# In[3]:


## Exercise 5: Bottle Deposits
## In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. 
## In one particular jurisdiction, drink containers holding one litreor less have a $0.10 deposit, and drink containers holding more than one litrehave a $0.25 deposit. 
## Write a program that reads the number of containers of each size from the user.
## Your program should continue by computing and displaying the refund that will be received for returning those containers. 
## Format the output so that it includes a dollar sign and always displays exactly two decimal places.

one_or_less = int(input("Please Enter the number of bottle which can contain maximum of a litre: "))
more_than_one = int(input("Please Enter the number of bottle which can contain more than one litre of water: "))
refund = round(((one_or_less * 0.10) + (more_than_one * 0.25)),2)
print("The refund generated is: $",refund)


# In[4]:


## Exercise 6: Tax and Tip
## The program that you create for this exercisevwill begin by reading the cost of a meal ordered at a restaurant from the user.
## Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing. 
## Compute the tip as 18 percent of the meal amount (without the tax). 
## The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. 
## Format the output so that allthe values are displayed using two decimal places.

cost_of_meal = round(float(input("Please enter the cost of meal you have ordered: ")),2)
tip_rate = 18
tax_rate = 10
tip = round((cost_of_meal * 0.18),2)
Local_tax = round((cost_of_meal * 0.10),2)
total_bill = round((cost_of_meal + tip + Local_tax),2)
print("Cost of meal: {} \nTip Amount: {} \nTax Amount: {} \nTotal Bill Amount: {}".format(cost_of_meal,tip,Local_tax,total_bill))


# In[8]:


## Exercise 7: Sum of the First n Positive Integers
## Write a program that reads a positive integer, n, from the user and then displays the sum of allthe integers from 1 to n. 
## The sum of the first n positive integers can be computed using the formula: sum = (n)(n + 1)/2

positive_no = int(input("Please enter the positive integer number: "))
sum_of_first_n = (positive_no) * (positive_no + 1)/2
print("The sum of first", positive_no, "is: ",sum_of_first_n)


# In[10]:


## Exercise 8:Widgets and Gizmos
## An online retailer sells two products: widgets and gizmos. 
## Each widget weighs 75 grams. 
## Each gizmo weighs 112 grams. 
## Write a program that reads the number of widgets and the number of gizmos in an order from the user. 
## Then your program should compute and display the total weight of the order.

widget = int(input("Please enter the number of orders for widgets: "))
gizmo = int(input("Please enter the number of orders for gizmo: "))
wt_widget = 75
wt_gizmo = 112
total_wt = (widget * wt_widget) + (gizmo * wt_gizmo)
print("Total weight is: ", total_wt, "grams")


# In[13]:


## Exercise 9:Compound Interest 
## Pretend that you have just opened a new savings account that earns 4 percent interest per year. 
## The interest that you earn is paid at the end of the year and is added to the balance of the savings account. 
## Write a program that begins by reading the amount of money deposited into the account from the user. 
## Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. 
## Display each amount so that it is rounded to 2 decimal places.

base_amount = float(input("Please enter the deposite amount: "))
interest_rate = 0.04
amount_1year = round((base_amount + (base_amount * interest_rate)),2)
amount_2year = round((amount_1year + (amount_1year * interest_rate)),2)
amount_3year = round((amount_2year + (amount_2year * interest_rate)),2)
print("The amount in bank after end of first year is: {} \nafter second year: {} \nafter third year: {}".format(amount_1year,amount_2year,amount_3year))


# In[16]:


## Exercise 10: Arithmetic
## Create a program that reads two integers, a and b, from the user. 
## Your program should compute and display: 
## • The sum of a and b 
## • The difference when b is subtracted from a 
## • The product of a and b 6 1 Introduction to Programming Exercises 
## • The quotient when a is divided by b • The remainder when a is dividedby b • The result of log10 a • The result of abHint: 
## You will probably find the log10 function in the math module helpful for computing the second last item in the list.

import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("The sum of a and b is:", a + b)
print("The difference when b is subtracted from a is: ", a - b)
print("The product of a and b is: ", a * b)
print("The quotient when a is dic=vided by b is: ", a / b)
print("The remainder when a is divided by b is: ", a % b)
print("Log of a is: ", math.log10(a))


# In[ ]:




