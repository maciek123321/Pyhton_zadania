from math import sqrt

class Complexx(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complexx(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complexx(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complexx(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
    def __abs__(self, other):
        return sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        return f"{self.real}{'+' + str(self.imag) if self.imag >= 0  else str(self.imag)}i"

