#loading the necessary packages
from scipy import stats #for hypothesis testing
import numpy as np #for calculations and simulation

#function that calculates the loss differential
def calculation_loss_differential(mu, cov, size):
    dataset = np.random.multivariate_normal(mu, cov, size)
    differential = dataset[:, 0] - dataset[:, 1] 
    return differential

#function null_hypothesis
def null_hypothesis(mu, cov, size, alpha, H_0):
    if stats.ttest_1samp(calculation_loss_differential(mu, cov, size), H_0)[1] < alpha:
        return False
    else:
        return True

def simulation_function(mu, cov, size, alpha, H_0, repetitions):
    amount_alpha_error = 0
    amount_correct = 0
    for i in range(repetitions):
        result = null_hypothesis(mu, cov, size, alpha, H_0)
        if result == False:
            amount_alpha_error +=1
        else:
            amount_correct +=1
    return (amount_alpha_error/repetitions)*100, size

print("Type 1 error rate:", (simulation_function(mu=[0, 0], cov=[[1, 0.9], [0.9, 1]], size=250, alpha=0.1, H_0 = 0, repetitions=10000)), "%")