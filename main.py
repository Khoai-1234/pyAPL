import numpy
class pyAPL:
    def add(number1,number2):
        if number2 == '':
            # Conjugate
            return numpy.conj(number1)
        else:
            # Add
            return numpy.add(number1,number2)
    def minus(number1,number2):
        if number2 == '':
            # Negate
            return -number1
        else:
            # Minus
            return number1 - number2
    def time (number1,number2):
        if number2 == '':
            # Sign
            return numpy.sign(number1)
        else:
            # Time
            return numpy.multiply(number1,number2)
    def divide(number1,number2):
        if number2 == '':
            # Reciprocal
            return numpy.reciprocal(number1)
        else:
            # Divide
            return number1 / number2
    def residue(number1,number2):
        if number2 == '':
            # Absolute
            return numpy.absolute(number1)
        else:
            # Residue( Modulo)
            return numpy.fmod(number1,number2)
    def power(number1,number2):
        if number2 == '':
            # Exponential
            return numpy.exp(number1)
        else:
            # Power
            return numpy.power(number1,number2)
    def logarithm(number1,number2):
        if number2 == '':
            # Natural Logarithm
            return numpy.log(numpy.e,number1)
        else:
            return numpy.log(number1,number2)
    def min(number1,number2):
        if number2 == '':
            # Floor
            return numpy.floor(number1)
        else:
            # Minium
            return numpy.min(number1,number2)
    def max(number1,number2):
        if number2 == '':
            # Ceiling
            return numpy.ceil(number1)
        else:
            # Maxium
            return numpy.max(number1,number2)
