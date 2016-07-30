import numpy as np
import matplotlib.pyplot as plt
import math

#Sim of deorbit for CubeSat mission
def altToRho(h):
	
	if h > 250000:
		T = -131.21 + 0.00299*h
		p = 2.488 * ((T+273.1)/216.6)**(-11.388)
	if 11000 < h < 25000:
		T = -56.46
		p = 22.65 * math.e**(1.73-0.000157*h)
	if h < 11000:
		T = 15.04 - .00649*h
		p = 101.29 * ((T+273.1)/288.08)**(5.256)
	rho = p/(.2869 * (T+273.1))
alt = np.linspace(0,1000000)
rho = [altToRho(h) for h in alt]
plt.plot(alt,rho)
plt.show()
