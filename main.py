import cmath
import numpy
class pyAPL:
    def add(number1,number2):
        if number2 == '':
            return numpy.conj(number1)
        else:
            return numpy.add(number1,number2)
    def minus(number1,number2):
        if number2 == '':
            return -number1
        else:
            return number1 - number2
