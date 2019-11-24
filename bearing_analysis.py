import numpy as np
# import matplotlib.plt as plt 
from scipy.special import gamma, factorial




class bearing_system():
    a = 3.0
    
    def __init__(C_10, inner_diameter, outer_diameter, L_R, F_R, R, x_0, b, theta, num_bearings):
        self.C_10 = C_10
        self.inner_diameter = inner_diameter
        self.outer_diameter = outer_diameter
        self.L_R = L_R
        self.F_R = F_R
        self.R = R
        self.x_0 = x_0
        self.b = b
        self.theta
        self.num_bearings
        
    # L_D is the number of revolutions in three years for this component
    def return_largest_force(acceleration, F_D, L_D, a_f, R_D):
        R_A = R_D ** (1.0 / self.num_bearings)
        L_10 = self.L_R
        x_D = self.L_D / self.L_R
        F_limit = (self.C_10 / a_f) * ( ( ( self.x_0 + (self.theta - self.x_0) * (math.log(1 / R_A)) ** ( 1.0/b ) ) / ( x_D ) ) ** ( 1.0/a ) )
        if F_limit < F_D:
            return False
        else:
            return True
    

        






































catalog_rating_force = 1
rating_speed = 1
rating_life_in_hours = 1
a = 3 # ball bearings
# R = np.exp()

x_0 = 1.0
b = 1.0
theta = 1.0


R_manufacturer = 1.0
F_R = 1.0
l_R = 1.0
n_R = 1.0
L_R = l_R * n_R * 60
C_10 = 1.0
# We need to find 


# We use two bearings and they have the same design factors
# Lifetime of 30 complete cycles per day, 5 days a week for 3 years
time_it_takes_for_each_cycle = 10.0
L_D = 30 * 5 * 3 * time_it_takes_for_each_cycle


x_D = L_D / L_R
mu_x = x_0 + (theta - x_0) * gamma(1.0 + 1.0 / b)
sigma_x = (theta - x_0) * (gamma(1.0 + 2.0 / b) - gamma(1.0 + 1.0 / b) ** 2) ** 0.5


# functions 
R = 0.9
R_D = 0.99

def valid_setting(F_D, acceleration, Distance, F_R, ):






