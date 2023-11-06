# modularização de codigo

import aula33_m
from aula33_m import soma

print("este e o", __name__)
print(aula33_m.soma(2, 5))
print(soma(2, 3))