import numPy as np

def dot_product(a, b):
  sum = 0
  for i in range(a.shape[0]):
    sum = sum + ( a[i] * b[i] )

  return sum

dot_product(np.arange(4), np.arange(4))
