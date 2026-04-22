# Write a program to swap two variables without using a third variable.
def swap(a,b):
    a,b=b,a
    return a,b

print(swap(1,2))

# Create a program that takes user input for name and age, then prints a formatted message using f-strings.
def str_formatting(name,age):
    print(f"my name is {name} and my age is {age}")

name=input("enter a name:")
age=int(input("enter the age: "))
str_formatting(name,age)

#Write a program to check if a number is even or odd using modulo operator.
def even_odd(num):
    if num%2==0:
        print("No is even")
    else:
        print("NO. is odd")

num=int(input("enter a number:"))
print(even_odd(num))

# Convert temperature from Celsius to Fahrenheit and vice versa.
def c_f(num):
    a=(num*1.8)+32
    return f"from celsius to fahrenheit {a}F"

def f_c(num):
    a=(num-32)//1.8
    return f"convert Fahrenheit to Celsius {a}C"

c=input("enter the to convert c_f or f_c:")
num=int(input("enter the no.:"))
if c=="c_f":
    print(c_f(num))
else:
    print(f_c(num))

#Check if a given string is a palindrome (case-insensitive).
def palindrome(st,n):
    for i in range(0,n//2):
        if st[i]!=st[n-i-1]:
          return False
    return True

st=input("enter a string:")
n=len(st)
print(palindrome(st,n))

# Count the frequency of each character in a string using a dictionary.
def freq_char(st):
   dic={}
   for k in st:
      if k in dic:
        dic[k]+=1
      else:
         dic[k]=1
     
    
   return dic

st="diyaaa"
print(freq_char(st))

#Write a program to format a string using all three formatting methods (%, .format(), f-strings).
def formate_by_modulus(name,age):
    print(f"my name is %s and my age is %d"%(name ,age))

def formate_by_method(name,age):
    print("my name is {name1} and my age is {age1}".format(name1=name,age1=age))

def f_string(name,age):
    print(f"my name is {name} and my age is {age}")

formate_by_modulus("Diya",21)
formate_by_method("Diya",21)
f_string("Diya",21)

#Write a program to check if a year is a leap year.
def leap_year(year): 
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
               return False
            
        return True
    return False

    
        
            



#Check if two strings are anagrams of each other.
def anagrams(str1,str2):
    if len(str1)==len(str2):
        if sorted(str1)==sorted(str2):
            return True
    return False
    
print(anagrams("geeks","kseeg"))
print(anagrams("listen","list"))

#Create a CLI calculator that performs basic arithmetic operations based on user input with input validation.
def calculator(num1,op,num2):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif  op=="*":
        return num1*num2
    elif op=="%":
        return num1%num2
    elif op=="/":
        if num2!=0:
           return num1/num2
        else:
            print("cannot divide a no. be zero")

    elif op=="//":
        if num2!=0:
          return num1//num2
        else:
            print("cannot divide a no. be zero")
    else:
        return "NO operator has been selected."
    
num1=int(input("enter the first number :"))
op=input("enter the operator to be performed: ")
num2=int(input("enter the second number :"))
print(calculator(num1,op,num2))


        
    
      
   


