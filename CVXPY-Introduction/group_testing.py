import numpy as np
import cvxpy as cp

def generate_test(N=1000, S=10, M=100, K=10):
    """
    # Construct the problem
    N = 1000 # Population size
    S = 10 # Number of infected individuals
    M = 100 # Number of tests
    K = 10 # Number of splits of each sample
    """

    # Define x0
    ind0 = np.random.choice(N,S,0) # index subset 
    x0 = np.zeros(N) 
    x0[ind0] = np.random.rand(S)

    # Define A
    A = np.zeros((M,N))
    for i in np.arange(N):
        ind = np.random.choice(M,K,replace=False)
        A[ind,i] = 1

    y = A @ x0

    return y, A, x0