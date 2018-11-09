#from math import function

function = input("what equation would you like me to analize")
x1 = int(input("on what interval? start value:"))
x2 = int(input("on what interval? end value:"))
#step = input("what do you want the step to be")

#func = function(equation)

interval = []

for i in range(x1,x2+1):
    if i == x2:
        interval.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            interval.append(i+m)

a1 = []
for i in interval:
    a1.append(i+.01)

a2 = []
for i in interval:
    a2.append(i-.01)
    
ycoordlist=[]
for r in interval:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
    
print(ycoordlist)

ycoordlist1=[]
for r in a1:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist1.append(y)
    
print(ycoordlist)

ycoordlist2=[]
for r in a2:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist2.append(y)
    
print(ycoordlist)

'''f = []
part = []

for m in equation:
    if m != "+" or "-":
        part.append(m)
    elif m == "-" or m == ":
        f.append(part)
        part = []'''

#f1  = lambda a: (ycoorddict[(a+.01)]-ycoorddict[(a-.01)])/(2*.01)

for m in interval:
    deriv  = ((ycoordlist1[m])-(ycoordlist2[m]))/(2*0.01)
    print(deriv)