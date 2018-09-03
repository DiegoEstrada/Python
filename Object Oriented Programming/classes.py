class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

class Complex:
	def __init__(self,realpart,imagpart):
		self.r = realpart
		self.i = imagpart
		print("Complex number created")


print(MyClass.i)
print(MyClass.f)
print(MyClass.f("")+"\n")

x = Complex(3,-4.5)
print("Real part",x.r)
print("Imaginary part",x.i)

