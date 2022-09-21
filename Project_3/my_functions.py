import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def normalize(data):
    mu = []
    std = []
    aux_data = data.copy()
    target_column = data.shape[1] - 1
    
    for i in range(0,data.shape[1]-1):
        mu.append(np.mean(aux_data[:,i]))
        std.append(np.std(aux_data[:, i]))
        aux_data[:,i] = ((aux_data[:,i] - np.mean(aux_data[:,i]))/np.std(aux_data[:, i]))
    
    return aux_data[:, :target_column], aux_data[:, target_column], mu, std

def cost_function(x, y, theta):
    return ((np.matmul(x, theta)-y).T@(np.matmul(x, theta)-y))/(y.shape[0])

def gradient_descent(x, y, theta, learning_rate=0.1, num_epochs=10):
    m = x.shape[0]
    J_all = []
    
    for _ in range(num_epochs):
        h_x = np.matmul(x, theta)
        cost_ = (-2/m)*(x.T@(h_x - y))
        theta -= (learning_rate)*cost_
        J_all.append(cost_function(x, y, theta))
        
    return theta, J_all 

def plot_cost(J_all, num_epochs):
    plt.xlabel('Epochs')
    plt.ylabel('Cost')
    plt.plot(num_epochs, J_all, 'm', linewidth = "5")
    plt.show()

def test(theta, x, mu, std):

    y = []
    x = x.copy()

    for k in range(0, len(x)):

        for q in range(0, len(mu)):
            x[k, q] = (x[k, q] - mu[q])/std[q]
    
        for h in range(0, len(theta)):
            if h == 0:
                aux = theta[h].copy()
            else:
                aux += (theta[h]*x[k, h-1]).copy()
        y.append(aux)
        
    return y