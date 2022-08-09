
class A:
    def __init__(self, a):
        self.a = a

    def show(self):
        print(self.a)


class B:
    def __init__(self, a):
        self.a = a

    def show(self):
        print(self.a.a)


a = A(1)
b = B(a)
a.show()
b.show()
a.a = 2
a.show()
b.show()

