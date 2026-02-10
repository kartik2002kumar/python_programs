a,b=20,30
def sum():
    global a,b
    b=30
    print(a,b)
    print(a+b)

print(a+b)
print(a,b)
sum()
a=40
sum()
print(a)
