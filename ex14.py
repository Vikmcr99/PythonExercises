import cmath
import math

ang=float(input('Digite um angulo:'))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang= math.tan(math.radians(ang))
print('O seno é {:.2f}, o cosseno é {:.2f}, e a tangente é: {:.2f}'.format(sen, cos, tang))