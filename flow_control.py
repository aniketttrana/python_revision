# if 
a=10
b=3
if b>a: print("b is greater than a")
else: print("a is greater than b")

a=10
b=20
c=30
if(a>b) & (a>c): print("A is greatest")
elif(b>a) & (b>c): print("B is greatest")
else : print("C is greatest")

###############  IF IN TUPLES ################
tup1=('a','b','c')
if 'a' in tup1 : print("PRESENT")
else: print("Not Present")

###############  IF IN List ################
l1=['a','b','c']
if l1[1]=='b': l1[1]='z'
print(l1)

##############  If with dictionary ########
d1={'k':10 ,'k2':20}
if d1['k2']==20 : d1['k2']=d1['k2']+100
print(d1)

