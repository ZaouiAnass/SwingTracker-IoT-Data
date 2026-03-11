#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.8  # Accélération due à la gravité (m/s²)
rho_air = 1.225  # Densité de l'air (kg/m³)
coef_trainee = 0.47  # Coefficient de traînée de la balle de baseball
rayon_balle = 0.0366  # Rayon de la balle de baseball (m)
masse_balle = 0.145  # Masse de la balle de baseball (kg)
A = np.pi * rayon_balle**2  # Section transversale de la balle
vitesse_frappe = 54.72  # Vitesse de frappe (m/s)
vitesse_initiale = 42.47  # Vitesse initiale avant impact (m/s)
hauteur_initiale = 1.2  # Hauteur initiale de la balle (m)

# Résolution des équations différentielles
def force_trainee(vitesse):
    """Calcul de la force de traînée"""
    return 0.5 * rho_air * coef_trainee * A * vitesse**2

def equations_motion(t, y, masse_balle):
    """Définition des équations différentielles du mouvement"""
    vitesse = np.sqrt(y[2]**2 + y[3]**2)
    force_drag = force_trainee(vitesse)
    theta = np.arctan2(y[3], y[2])
    force_x = -force_drag * np.cos(theta)
    force_y = -force_drag * np.sin(theta) - masse_balle * g
    dxdt = y[2]
    dydt = y[3]
    dvxdt = force_x / masse_balle
    dvydt = force_y / masse_balle
    return [dxdt, dydt, dvxdt, dvydt]

def projectile(vitesse_frappe, angle_frappe):
    """Calcul de la trajectoire du projectile pour un angle donné"""
    vitesse_initiale_x = vitesse_frappe * np.cos(np.radians(angle_frappe))
    vitesse_initiale_y = vitesse_frappe * np.sin(np.radians(angle_frappe))
    conditions_initiales = [0, hauteur_initiale, vitesse_initiale_x, vitesse_initiale_y]  # x0, y0, vx0, vy0
    
    solution = np.array([conditions_initiales])
    dt = 0.01  # Pas de temps
    for t in np.arange(0, 10, dt):
        k1 = np.array(equations_motion(t, solution[-1], masse_balle)) * dt
        k2 = np.array(equations_motion(t + dt/2, solution[-1] + k1/2, masse_balle)) * dt
        k3 = np.array(equations_motion(t + dt/2, solution[-1] + k2/2, masse_balle)) * dt
        k4 = np.array(equations_motion(t + dt, solution[-1] + k3, masse_balle)) * dt
        solution = np.append(solution, [solution[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6], axis=0)
        if solution[-1][1] < 0:
            break
    
    return solution

# Angles de frappe à analyser
angles_frappe = [15, 25, 30, 35, 45]

# Calcul des trajectoires
trajectoires = {angle: projectile(vitesse_frappe, angle) for angle in angles_frappe}

# Affichage des trajectoires
plt.figure(figsize=(10, 6))

for angle, traj in trajectoires.items():
    plt.plot(traj[:, 0], traj[:, 1], label=f'{angle}°')

plt.title('Trajectoires de la balle pour différents angles de frappe')
plt.xlabel('Distance (m)')
plt.ylabel('Hauteur (m)')
plt.legend()
plt.grid(True)
plt.show()


# In[16]:


import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 0.86  # Length of the bat in meters
a = 0.72   # Distance from the encastrement to the point of force application in meters
d = 0.06  # Diameter in meters
E = 10e9  # Young's modulus in Pascals
F = 1300   # Force in Newtons (example value)
y = d / 2 # Distance from the neutral axis to the outer fiber in meters

# Moment of inertia for a circular section
I = (np.pi * d**4) / 64

# Functions to calculate Ty, Mfz, epsilon, and sigma
def Ty(x):
    return np.where(x <= a, -F, 0)

def Mfz(x):
    return np.where(x <= a, -(a - x) * F, 0)

def epsilon(x):
    return Mfz(x) * y / (E * I)

def sigma(x):
    return (Mfz(x) * y / I)*(10*(10**9)) 

# Generate x values
x_values = np.linspace(0, L, 500)

# Calculate Ty, Mfz, epsilon, and sigma
Ty_values = Ty(x_values)
Mfz_values = Mfz(x_values)
epsilon_values = epsilon(x_values)
sigma_values = sigma(x_values)

# Plotting the results
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(x_values, Ty_values, label="Ty(x)")
plt.xlabel('x (m)')
plt.ylabel('Ty (N)')
plt.title('L’effort tangentiel tranchant  Ty(x)')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x_values, Mfz_values, label="Mfz(x)")
plt.xlabel('x (m)')
plt.ylabel('Mfz (Nm)')
plt.title('Moment Fléchissant Mfz(x)')
plt.grid(True)
plt.legend()



plt.subplot(2, 2, 4)
plt.plot(x_values, sigma_values, label="σ(x)")
plt.xlabel('x (m)')
plt.ylabel('Contrainte σ (MPa)')
plt.title('Contrainte σ(x)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




