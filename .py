from math import function


equation = input("what equation would you like me to analize")
x1 = int(input("on what interval? start value:"))
x2 = int(input("on what interval? end value:"))

func = function(equation)

interval = []

for i in range(x1,x2+1):
    if i == x2:
        interval.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            interval.append(i+m)

'''f = []
part = []

for m in equation:
    if m != "+" or "-":
        part.append(m)
    elif m == "-" or m == ":
        f.append(part)
        part = []'''

f1  = lambda h: ((h-(-(-h)))/(2*h))

for m in interval:
    print(f1(m))
