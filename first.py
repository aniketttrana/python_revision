# install python for windows
# we need IDE (Integrated developement environment) like vs code

print("I am learning Python")
# student is a variable (variable has name and address it is a container used to store values)
student="aniket"
student="rana"
print(student)
# datatypes in python
# int , float , boolean , strings, complex
a1=11
print(type(a1))   
# output= <class 'int'>
a1=1.1
print(type(a1))  
# <class 'float'>
a1=True
print(type(a1))  
# <class 'bool'>
a1="aniket"
print(type(a1))  
# <class 'str'>
a1=3+4j
print(type(a1))  
# <class 'complex'>

#############################
# Airthmetic Operators
# +,-,*,/
a=10
b=20
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Relational  Operators
# <,>,<,>,!=,==
a=10
b=20
print(a<b)
# True
print(a<=b)
# True
print(a==b)
# False
print(a!=b)
# True

# Logical  Operators
#     | , &
a=True
b=False
print(a &b)
# false
print(a |b)
# True
print(a &a)
# True

#####################################
# Component are the small things in python
# identifiers are the names given to variable,function,object

                    # identifiers rules

# no special character except _(underscore)
# case sensitive
# first letter cannot be digit

# Literals are constant in python 
# data in variable are literals
# for ex a="aniket"  here aniket is literal

#################################################
                # Python Strings

# Sequence of characters enclosed with single quota (''),double quota(" ") or triple quota('''  ''')

str1= 'aniket'
str2="rana"
# here we cant use line break
str3='''jai ho 
jai ho'''
print(str1,str2,str3)


#############(( Operation in Strings ))##############

str="aniket aniket is a boy"
print(str[0],str[-1])
# -1 from last
print(str[-3])

print(str)
print(str[1:5])
# contain both 1 ans 4
print(str.lower())
# aniket
print(str.upper())
# aniket
print(len(str))
# space included 

print(str.replace('a','r'))
# rniket
print(str.count("aniket"))
# 2  count no. of occurence of substring in string

print(str.find('aniket'))
# gives 1st occurnece index
print(str.split("a"))

