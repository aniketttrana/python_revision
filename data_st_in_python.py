# Tuple , list , Dictioary , Set
# Tuple= ordered collection  of heterogenius items we can store in ()

# They are immutable (they cant change)
tup=(1,2,'a',True)
print(tup)
print(type(tup))
# <class 'tuple'>

# [0],[-1][1:3] ,len(tup1) These all thing behaves like string in it
# tup[0]="a"  we cant do that(we cant change)

tup1=(1,2,3)
tup2=(4,5,6)
print(tup1+tup2)
print(tup2+tup1)

# to repeat the elements
a=("aniket",1)
print(a*3)
b=(1,2,3,4,4)
print(min(b))
print(max(b))


# ##################  LISTS ######################

# list are mutable (We can change it)
#               []

listt=[1,2,'a',True]
print(listt)
print(type(listt))
# <class 'list'>
# [0],[-1],[1,3] ,listt*3, listt1+listt2  we can perform same operation as that  of tuples

listt.pop() #last element got pop out
print(listt)
listt[0]="ani"
print(listt)
listt.append("rana") # to add element at last
print(listt)

# insert via index
listt.insert(0,"jaiho")
print(listt)
 
A=["aniket","hop","dude"]
A.sort()
print(A)
# sort in alphabeticall order
A.reverse()
print(A)


# ##################  Dictionary ######################
#  Unordereed collection of key-value pairs wnclosed with {}
# It is mutable (We can change it)

Fruits={"Apple":10,
        "Orange":20}

print(type(Fruits))
# <class 'dict'>

print(Fruits.keys())

print(Fruits.values())

print(Fruits)

# to add at last
Fruits['Cucumber']=99
print(Fruits)

# to modify the value
Fruits['Apple']=0
print(Fruits)

# how to concatinate in one dictionary
fruit1={"a":10,"b":20}
fruit2={"c":30,"d":40}
fruit1.update(fruit2)

print(fruit1)

# how to pop
fruit1.pop("a")
print(fruit1)

# ##################  SET ######################

# It is a unordered and unindexed collection of elements enclosed with {}

s1={1,"a",True,"aniket"}
# True output 1 is not being printed bcoz it does not store duplicates
# Dublicates are not allowed in set
print(s1)
# it return output in any order

# add elements anywhere
s1.add("add")
print(s1)
        # to add multiple
s1.update([1,2,3,4])  

# to remove the element
s1.remove("aniket")
print(s1)

# UNION AND INTERSECTION
uni={1,2,3,4,"a"}
uni1={2,3,"b"}
res=uni.union(uni1)
print(res)

int=uni.intersection(uni1)
print(int)