import matplotlib.pyplot as plt
import numpy as np
X = np.array([[0, 1, 2, 4]]).T  # 都转换成列向量
y = np.array([[0, 1, 2, 4]]).T
theta1 = np.array([[0, 0]]).T  # 三个不同的theta_1值
theta2 = np.array([[0, 0.5]]).T
theta3 = np.array([[0, 1]]).T
X_size = X.shape
X_0 = np.ones((X_size[0],1))  # 添加x_0
X_with_x0 = np.concatenate((X_0, X), axis=1)
h1 = np.dot(X_with_x0, theta1)
h2 = np.dot(X_with_x0, theta2)
h3 = np.dot(X_with_x0, theta3)
plt.plot(X, y, 'rx', label='y')
plt.plot(X, h1, 'r', label='h1, theta_1=0')
plt.plot(X, h2, 'g', label='h2, theta_1=0.5')
plt.plot(X, h3, 'b', label='h3, theta_1=1')
plt.xlabel('X')
plt.ylabel('y/h')
plt.axis([-0.1, 4.5, -0.1, 4.5])
plt.legend(loc='upper left')
plt.savefig('liner_gression_error.png', dpi=200)
plt.show()
def calcu_cost(theta, X, y):
    m = X.shape[0]  # sample size
    X_0 = np.ones((m,1))
    X_with_x0 = np.concatenate((X_0, X), axis=1)
    h = np.dot(X_with_x0, theta)
    return(np.dot((h-y).T, (h-y))/(2*m))

X = np.array([[0, 1, 2, 4]]).T
y = np.array([[0, 1, 2, 4]]).T
theta_0 = np.zeros((101, 1))
theta_1 = np.array([np.linspace(-2, 4, 101)]).T
theta = np.concatenate((theta_0, theta_1), axis=1)  # 101组不同的参数
J_list = []
for i in range(101):
    current_theta = theta[i:i+1].T
    cost = calcu_cost(current_theta, X, y)
    J_list.append(cost[0,0])
plt.plot(theta_1, J_list)
plt.xlabel('theta_1')
plt.ylabel('J(theta)')
plt.savefig('cost_theta.png', dpi=200)
plt.show()