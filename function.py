#Function is a block of code which perform a specific task
# start with defination

###########################
def hii():
    print("My name is Aniket Rana")
hii()
###########################
def add_10(x):
    print(x+10)
add_10(50)
###########################
def odd_even(x):
    if x%2==0:
        print(x, "is even")
    else:
        print(x, "is odd")
odd_even(10)

##########################
# lambda function(Anonymous function)

g=lambda x: x*x*x
print(g(5))

# lambda with filter
l1=[1,2,3,4,5,5,7]
final=list(filter(lambda x : (x%2!=0),l1))
print(final) # odd vale aagye

# lambda with map
l1=[1,2,3,4,5,6,7,8]
final=list(map(lambda x: x*2,l1))
print(final)

# lambda with reduce

from functools import reduce
final=reduce(lambda x,y:x+y ,l1)
print(final)

