import math
a = 1
b = 2
eps = 0.0001
steps = 0
x0 = (a + b)/2
def f(x):
  return 1 / math.tan(x) - 0.5 * x
def df(x):
  return -1 / math.sin(x) ** 2 - 0.5
# Search for the maximum f'(x)=l 
i=a
l=1
di = abs((b-a)/1000)
while (i<b):
  n = df(i)
  if (abs(l)<abs(n)):
    l=n
  i+=di
x1 = f(a)
x2 = f(b)
q=1/l
if (x1*x2>0):
  print('There are no solutions on this interval')
else:
  xp = x0
  while (steps<100):
    xn = xp - q*f(xp)
    res = xn - xp
    xp = xn
    steps+=1
    if (abs(res)<eps):
      break
  print(f'{xp:.4f}')
  print(f'Number of steps {steps}')