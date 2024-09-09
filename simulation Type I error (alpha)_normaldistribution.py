#loading the necessary packages
from scipy import stats #for hypothesis testing
import numpy as np #for calculations and simulation

#function that calculates the loss differential
def calculation_loss_differential(mu, sigma, size):
    dataset1 = np.random.normal(mu, sigma, size)
    dataset2 = np.random.normal(mu, sigma, size)
    differential = dataset1-dataset2 
    return differential

#function null_hypothesis
def null_hypothesis(mu, sigma, size, alpha, H_0):
    if stats.ttest_1samp(calculation_loss_differential(mu, sigma, size), H_0)[1] < alpha:
        return False
    else:
        return True

def simulation_function(mu, sigma, size, alpha, H_0, repetitions):
    amount_alpha_error = 0
    amount_correct = 0
    for i in range(repetitions):
        result = null_hypothesis(mu, sigma, size, alpha, H_0)
        if result == False:
            amount_alpha_error +=1
        else:
            amount_correct +=1
    return (amount_alpha_error/repetitions)*100, size

print("Type 1 error rate:", (simulation_function(mu=0, sigma=np.sqrt(1), size=8, alpha=0.05, H_0 = 0, repetitions=10000)), "%")