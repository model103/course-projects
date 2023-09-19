import numpy as np
import matplotlib.pyplot as plt

'''X = np.array([[1, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 1, 1, 1, 1, 1]])
'''

'''X = np.rand(100, 2)
print()

Y = np.array([-1, 1, 1, -1])

W = (np.random.random(6) - 0.5) * 2

print(W)
'''

X_temp = np.random.rand(100, 3)
temp = np.array([[2, 0, 0], [0, 0, 1], [0, 0, 0]])
X = np.dot(X_temp, temp)

Y = np.zeros(100)
for i in range(100):
    X[i][2] = 1
    if (X[i][0]+2*X[i][1]-2) > 0:
        Y[i] = 1
    else:Y[i] = -1

W = (np.random.random((3)) - 0.5) * 2
#print(W)
# 学习率
lr = 0.11

n = 0

o = 0


def update():
    global X, Y, W, lr, n
    n += 1
    o = np.sign(np.dot(X, W.T))
    W_C = lr * ((Y-o.T).dot(X))
    W = W + W_C
    print(W)
    error = np.linalg.norm(Y - o.T, 2)
    return error


'''def predict(X):
    global W
    y = np.sign(np.dot(X, W.T))
    return y
'''

'''def calculate(x, root):
    a = W[5]
    b = W[2] + x * W[4]
    c = W[0] + x * W[1] + x * x * W[3]
    if root == 1:
        return (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
    if root == 2:
        return (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
'''

for i in range(100):
    error = update()
    print(error)
    #print(W)
    #print(n)
     #o = np.sign(np.dot(X,W.T))
    if (o == Y.T).all():
        print('finish')
        break

''''for e in X:
    print(predict(e))

x1 = [0, 1]
y1 = [1, 0]
x2 = [0, 1]
y2 = [0, 1]
xdata = np.linspace(0, 5)

k = -W[1] / W[2]
d = -W[0] / W[2]

plt.figure()
plt.plot(xdata, calculate(xdata, 1), 'r')
plt.plot(xdata, calculate(xdata, 2), 'r')
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'yo')
plt.show()
'''