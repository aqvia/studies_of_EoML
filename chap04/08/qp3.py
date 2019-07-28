import numpy as np
import cvxopt

## Minimize f(x,y) = x^2 + xy + y^2 + 2x + 4y
## Subject to 2x + 3y <= 3

P = cvxopt.matrix(np.array([[2,1],[1,2]], dtype=np.float64))
q = cvxopt.matrix(np.array([2,4], dtype=np.float64))
G = cvxopt.matrix(np.array([[2,3]], dtype=np.float64))
h = cvxopt.matrix(np.array([3], dtype=np.float64))

sol = cvxopt.solvers.qp(P, q, G=G, h=h)

print(np.array(sol["x"]))
print(np.array(sol["primal objective"]))