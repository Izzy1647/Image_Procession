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