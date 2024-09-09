#loading the necessary packages
from scipy import stats #for hypothesis testing
import numpy as np #for calculations and simulation

#function that calculates the loss differential
def calculation_loss_differential(size):
    dataset1 = np.random.standard_t(df = 4, size = size)
    dataset2 = np.random.standard_t(df = 4, size = size)
    differential = dataset1-dataset2 
    return differential

#function null_hypothesis
def null_hypothesis(size, alpha, H_0):
    if stats.ttest_1samp(calculation_loss_differential(size), H_0)[1] < alpha:
        return False
    else:
        return True

def simulation_function(size, alpha, H_0, repetitions):
    amount_alpha_error = 0
    amount_correct = 0
    for i in range(repetitions):
        result = null_hypothesis(size, alpha, H_0)
        if result == False:
            amount_alpha_error +=1
        else:
            amount_correct +=1
    return (amount_alpha_error/repetitions)*100, size

print("Type 1 error rate:", (simulation_function(size=8, alpha=0.1, H_0 = 0, repetitions=10000)), "%")