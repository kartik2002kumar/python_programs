class A:
    def __init__(self):
        print("Constructor A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor B")

class C(B):
    def __init__(self):
        super().__init__()
        print("Constructor C")

obj = C()