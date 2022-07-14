def decision(probability):
  import random
  return random.random() < probability

def colselect(A, k, row=False, eps=1):
  import numpy as np
  c = (k*np.log(k))/(eps*eps)
  m,n = A.shape[0],A.shape[1]
  u,s,vh = np.linalg.svd(A, full_matrices=False)
  vh = vh[:k,:]
  probs = (1/k)*(vh**2).sum(axis=0)
  probs = [min(1,c*p) for p in probs]
  idxs = [decision(p) for p in probs]
  cols = A[:,idxs]
  included_idx = [i for i in range(n) if idxs[i]]
  if row:
    return cols.T, included_idx
  return cols, included_idx

def cur_decompose(A, k , e=1, return_idx=False):
  from numpy.linalg import pinv as inv
  m,n = A.shape[0],A.shape[1]
  if k > min(m,n):
    return [], [], []
  C, included_cols = colselect(A, k, False, eps=e)
  R, included_rows = colselect (A.T, k, True, eps=e)
  U = inv(C)@A@inv(R)
  if return_idx:
    return C, U, R, included_cols, included_rows
  return C, U, R

def give_error(A,B):
  import numpy as np
  num = ((np.array(A)-np.array(B))**2).sum()
  den = ((np.array(A))**2).sum()
  val = np.sqrt(num/den)
  return val