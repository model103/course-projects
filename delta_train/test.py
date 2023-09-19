import numpy as np
import matplotlib.pyplot as plt

X_temp = np.random.rand(100, 3)
temp = np.array([[2, 0, 0], [0, 1, 0], [0, 0, 1]])
X = np.dot(X_temp, temp)
Y = np.zeros(100)

for i in range(100):
    X[i][2] = 1
    if (X[i][0]+2*X[i][1]-2) > 0:
        Y[i] = 1
    else:Y[i] = -1
#print(Y)
W = (np.random.random((3, 1)) - 0.5) * 2
#print(W)
error1 = np.array([[1,2], [3,4],[5,6]])
print(error1.shape[0])
error = np.linalg.norm(error1, 'fro')
#print(error)


