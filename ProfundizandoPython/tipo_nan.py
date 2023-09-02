from decimal import Decimal
import math

# NaN Not a Number (No es un número)
# NaN no es sensible a mayúsculas/minúsculas
# NaN es un tipo de dato numérico indefinido
a = float('NaN')
# print(f'a: {a}')
# print(f'Es NaN (not a number)?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')