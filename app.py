"""x=3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)

day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

x = "test"
print(f"hello {x}")

temp = 200000000
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')"""
"""
def odd_even(g) :
    if g % 2 == 0:
        print("even")
    else:
        print("odd")
odd_even(60)


def ser(s):
    def bill(b):
        if s == ("bad"):
            def tip (x):
                    print (b * x)
            tip(0)
        elif s == ("okay"):
            def tip (x):
                    print(b * x)
            tip(0.15)
        elif s == ("good"):
            def tip (x):
                print(b * x)
            tip(0.20)
        elif s == ("great"):
            def tip (x):
                print(b * x)
            tip(0.25)
    bill(10)
ser("good")
"""   """
def factor(x):
    for i in range(x):
        if (6%x) == 0:
            print(f"{x} is factor")
        factor(x+1)
factor(1)"""

def gfactor(x):
    for i in range(x):
        if (6%x) == 0 and (8%x) == 0:
            print(f"{x} is greatest common factor")
        gfactor(x+1)
gfactor(1)




