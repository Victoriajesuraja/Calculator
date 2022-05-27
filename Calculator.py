#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program make a simple calculator


# In[2]:


# This function adds two numbers
def add(x, y):
    return x + y


# In[3]:


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# In[4]:


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# In[5]:


# This function divides two numbers
def divide(x, y):
    return x / y


# In[6]:


# This function exponentiates two numbers
def exponential(x, y):
    return x ** y


# In[7]:


print("Select operation.")


# In[8]:


print("1.Add")


# In[9]:


print("2.Subtract")


# In[10]:


print("3.Multiply")


# In[11]:


print("4.Divide")


# In[12]:


print("5.Exponential")


# In[ ]:


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "**", num2, "=", exponential(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[ ]:





# In[ ]:





# In[ ]:




