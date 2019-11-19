V_max = 1
PV_max = 1
P_max = 1
T_max = 1
D = 1
F = 1
N = 1
t = 1
L = 1


def get_f1_rotary(pressure, velocity):
    
    if ( velocity < 0 or velocity >= 100 ) or ( pressure > 3600 or pressure < 0 ):
        return False
    
    f1 = 0
    if pressure < 720:
        if velocity <= 3.3:
            f1 = 1.0
        elif velocity <= 33:
            slope = (1.3 - 1.0) / (33 - 3.3)
            f1 = slope * (velocity - 3.3) + 1.0 
        elif valocity <= 100:
            slope = (1.8 - 1.3) / (100.0 - 33.0)
            f1 = slope * (velocity - 33.0) + 1.3
    elif pressure < 3600:
        if velocity <= 3.3:
            f1 = 1.5
        elif velocity <= 33:
            slope = (2.0 - 1.5) / (33 - 3.3)
            f1 = slope * (velocity - 3.3) + 1.5 
        elif valocity <= 100:
            slope = (2.7 - 2.0) / (100.0 - 33.0)
            f1 = slope * (velocity - 33.0) + 2.0

    return f1


def get_f2(temperature, foreign_matter):
    
    if temperature > 210 :
        return False

    return f2