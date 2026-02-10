m,n=100,200
def inner():
    p,q=10,20
    print(p+q)
    def outer():
        nonlocal q
        q=19
        print(q+p)
    print(p,q)
    outer()
    print(p+q)
print(m,n)
inner()
