#loading the necessary packages
from scipy import stats #for hypothesis testing
import numpy as np #for calculations and simulation
from csv import writer #for adding data to a csv file

#parameters
mu1 = [0, 0]#expected value of one sample, mu1[1] is changed in def simulation_beta_error
cov = [[1, 0.9], [0.9, 1]]
size = 16 #sample size
alpha = 0.05 #significance level
H_0 = 0 
repetitions = 10000 #number of repetitions
theta_upper_bound = 3.6 #determines the maximum value up to which the 2nd random variable is shifted
data_name = "Power_curve_16_5%_cov09.csv" #name of the CSV file

#function that calculates the loss differential
def calculation_loss_differential(mu, cov, size):
    dataset = np.random.multivariate_normal(mu, cov, size)
    differential = dataset[:, 0] - dataset[:, 1] 
    return differential

#function null hypothesis
def null_hypothesis_theta(mu1, cov, size, alpha, H_0):
    if stats.ttest_1samp(calculation_loss_differential(mu1, cov, size), H_0)[1] < alpha:
        return False
    else:
        return True

#function for calculating the amount of beta errors for a specific theta
def simulation_function_theta(mu1, cov, size, alpha, H_0, repetitions):
    amount_beta_error = 0
    amount_correct = 0
    for i in range(repetitions):
        result = null_hypothesis_theta(mu1, cov, size, alpha, H_0)
        if result == False:
            amount_correct +=1
        else:
            amount_beta_error +=1
    return (amount_beta_error/repetitions)*100

#function for simulating the beta error for all thetas in a given range
def simulation_beta_error(mu1, cov, size, alpha, H_0, repetitions, theta_upper_bound, data_name):
    for mu2 in np.arange(0,theta_upper_bound,0.25):
        list_power = []
        if mu2 != 0:
            mu1 = [0, mu2]
            power = 100-float(simulation_function_theta(mu1, cov, size, alpha, H_0, repetitions))
            list_power.append(mu2)
            list_power.append(power)
        else:
            list_power.append(mu2)
            list_power.append(0)
        with open(data_name, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list_power)
            f_object.close()
    return "Finish"

print("Start")
print(simulation_beta_error(mu1, cov, size, alpha, H_0, repetitions, theta_upper_bound, data_name))