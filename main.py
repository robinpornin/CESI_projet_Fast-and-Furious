"""
Projet Fast & Furious – Simulation de trajectoires
Auteur : Robin Pornin
Formation : CESI Nice – Cycle préparatoire ingénieur
Description :
Simulation numérique de différentes phases de conduite
(plan incliné, looping, saut, piste plate) en utilisant
les lois de la mécanique newtonienne et la résolution
d’équations différentielles avec odeint.
"""





print("-" * 122)
print("")

'''
PARTIE 1 : PLAN INCLINE ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)

# déclaration des voitures : P.O.O. (programmation orientée objet)
class Voiture:
    def __init__(self, nom_ , m_ , am_ , L_ , l_ , h_ , Cx_ , Cz_ , mu_ ):
        self.nom      = nom_  
        self.masse    = m_     
        self.accel    = am_     
        self.longueur = L_
        self.largeur  = l_
        self.hauteur  = h_
        self.cx       = Cx_
        self.cz       = Cz_
        self.cf       = mu_
 
# variable            nom                 masse am   long  larg  haut  cx    cz   µ
dodge      = Voiture("Dodge Charger"    , 1760, 5.1, 5.28, 1.95, 1.35, 0.38, 0.3, 0.1)
supra      = Voiture("Toyota Supra"     , 1615, 5  , 4.51, 1.81, 1.27, 0.29, 0.3, 0.1)
chevrolet  = Voiture("Chevrolet Camaro" , 1498, 5.3, 4.72, 1.88, 1.35, 0.35, 0.3, 0.1)
mazda      = Voiture("Mazda RX-7"       , 1385, 5.2, 4.3 , 1.75, 1.23, 0.28, 0.3, 0.1)
skyline    = Voiture("Nissan Skyline"   , 1540, 5.8, 4.6 , 1.79, 1.36, 0.34, 0.3, 0.1)
mitsubishi = Voiture("Mitsubishi Lancer", 1600, 5  , 4.51, 1.81, 1.48, 0.28, 0.3, 0.1)

garage = [dodge, supra, chevrolet, mazda, skyline, mitsubishi]   # liste des voitures nommée "garage"
i = int(input(f"Choix voiture : \n tapez 1 pour la {garage[0].nom} \n tapez 2 pour la {garage[1].nom} \n tapez 3 pour la {garage[2].nom} \n tapez 4 pour la {garage[3].nom} \n tapez 5 pour la {garage[4].nom} \n tapez 6 pour la {garage[5].nom}\n >>> ")) - 1
print("")
print(f"Voiture choisie : {garage[i].nom}")
print("")

# gadgets
jupe  = int(input("Jupe avant ? : OUI = 1 ; NON = 0 \n>>> "))
ailes = int(input("Ailes ? : OUI = 1 ; NON = 0 \n>>> "))
nos   = int(input("Pour la pente : NOS = 1 ; pas de NOS = 0 \n>>> ")) 


# caractéristiques voitures
m  = garage[i].masse + 30*ailes + 15*jupe           # Masse.........................(kg)
am = garage[i].accel + (nos*0.3*garage[i].accel)    # Accélération moyenne..........(m/s²)
L  = garage[i].longueur                             # Longueur de la voiture........(m)
l  = garage[i].largeur                              # Largeur de la voiture.........(m)
h  = garage[i].hauteur                              # Hauteur de la voiture.........(m)
S_x  = l * h                                        # Surface frontale..............(m²)
S_z  = l * L + (ailes * 0.8)                        # Surface sous la voiture.......(m²)
C_x = garage[i].cx - (jupe*0.05*garage[i].cx)       # Coefficient de traînée........(sans unité)
C_z = garage[i].cz + (ailes*0.1*garage[i].cz)       # Coefficient de portance.......(sans unité)
mu  = garage[i].cf                                  # Coefficient de frottement.....(sans unité)

rho = 1.225                                         # Densité de l'air (kg/m^3)
g = 9.81                                            # Intensité de pesanteur (m/s^2)

alpha = np.radians(3.69)                            # Angle alpha de la pente (rad)


def equadiff_1(y1, t):
    v = y1[0]  # vitesse
    x = y1[1]  # position
    ax =  ((-0.5*rho * C_x * S_x) / m) * v**2 + am - mu * g * np.cos(alpha) + g * np.sin(alpha)
    return [ax, v]


t = np.linspace(0, 4, 10000)  # 4 secondes avec 10000 points (+ de points = + de précision)

# conditions initiales :
v0 = 0     
x0 = 0     
y0 = [v0, x0]

solution = odeint(equadiff_1, y0, t)
vitesse  = solution[:, 0]  # première colonne du tableau numpy renvoyé par ODEINT
position = solution[:, 1]  # deuxième colonne du tableau numpy renvoyé par ODEINT

def n1():
    for i in range(len(position)):
        if position[i] >= 30.984 and position[i] <= 31.0 :
            return i
        
vitesse_bas_pente = vitesse[n1()]
temps_bas_pente   = t[n1()]
chrono            = temps_bas_pente

print("")
print("")
print("ETAPE 1 : PLAN INCLINE")
print("")
print("Vitesse en bas de la pente : ", round((vitesse_bas_pente), 3), "m/s. ; \nsoit :", round((vitesse_bas_pente*3.6), 3), "km/h.")
print("Temps en bas de la pente : ", round((temps_bas_pente), 3), "s." )
print("")
print("")


# Graphique de la vitesse
plt.subplot(2, 1, 1)
plt.plot(t, vitesse, label='Vitesse (m/s)', color='blue')
plt.xlabel('Temps (s)')
plt.ylabel('Vitesse (m/s)')
plt.title('Evolution de la vitesse de la voiture dans la pente')
plt.grid(True)
plt.legend()









'''
PARTIE 2 : LOOPING ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

print("ETAPE 2 : LOOPING")
print("")
nos   = int(input("Pour le loop : NOS = 1 ; pas de NOS = 0 \n>>> "))

# caracteristiques voitures
m  = garage[i].masse + 30*ailes + 15*jupe           # Masse.........................(kg)
am = garage[i].accel + (nos*0.3*garage[i].accel)    # Accélération moyenne..........(m/s²)
L  = garage[i].longueur                             # Longueur de la voiture........(m)
l  = garage[i].largeur                              # Largeur de la voiture.........(m)
h  = garage[i].hauteur                              # Hauteur de la voiture.........(m)
S_x  = l * h                                        # Surface frontale..............(m²)
S_z  = l * L + (ailes * 0.8)                        # Surface sous la voiture.......(m²)
C_x = garage[i].cx - (jupe*0.05*garage[i].cx)       # Coefficient de traînée........(sans unité)
C_z = garage[i].cz + (ailes*0.1*garage[i].cz)       # Coefficient de portance.......(sans unité)
mu  = garage[i].cf                                  # Coefficient de frottement.....(sans unité)

rho = 1.225                                         # Densité de l'air (kg/m^3)
g = 9.81                                            # Intensité de pesanteur (m/s^2)
R = 6                                               # Rayon du looping (m)

# fonction pour calculer les frottements
def frottements(theta, v, rho, S_x, C_x, m, mu):
    F_aero = 0.5 * rho * S_x * C_x * (v ** 2)       # frottements air
    F_sol = mu * m * g * np.cos(theta)              # frottements sol
    return F_aero + F_sol

# fonction pour calculer les pertes d'énergie
def perte_energie(v, R, rho, S_x, C_x, m, mu, n_points=1000):
    theta_values = np.linspace(0, 1 * np.pi, n_points)
    delta_theta = theta_values[1] - theta_values[0]
    delta_E = sum(frottements(theta, v, rho, S_x, C_x, m, mu) * R * delta_theta for theta in theta_values)
    return delta_E

# calcul de la vitesse minimale d'entrée
def vitesse_minimale_entree(R, g, rho, S_x, C_x, m, mu):
    v_sommet = np.sqrt(g * R)
    delta_E = perte_energie(v_sommet, R, rho, S_x, C_x, m, mu)
    E_sommet = 0.5 * m * v_sommet ** 2 + m * g * 2 * R
    E_entree = E_sommet + delta_E
    v_entree = np.sqrt((2 * E_entree) / m)
    return v_entree


v_min_entree = vitesse_minimale_entree(R, g, rho, S_x, C_x, m, mu)
print(f"Vitesse minimale pour {garage[i].nom} : {round(v_min_entree, 2)} m/s")


def equadiff_2(y, t):
    theta, v = y  
    dtheta_dt = v / R
    a_t = (  -g * np.sin(theta) + am - (  (0.5*rho*C_x*S_x) / m  ) * ((dtheta_dt*R)**2)   - mu *(((-R*(dtheta_dt**2))/m) - g*np.cos(theta)) )   / (R)
    dv_dt = a_t
    return [dtheta_dt, dv_dt]

# conditions initiales
theta_0 = 0               
v_0 = vitesse_bas_pente   
y0 = [theta_0, v_0]


t = np.linspace(0, 3, 10000)  


solution = odeint(equadiff_2, y0, t)
theta_sol = solution[:, 0]  # position angulaire
v_sol     = solution[:, 1]  # vitesse

theta_deg = np.degrees(theta_sol)

# Affichage des résultats
plt.figure(figsize=(12, 6))

# Graphique de la vitesse
plt.subplot(2, 1, 1)
plt.plot(t, v_sol, label='Vitesse (m/s)', color='blue')
plt.xlabel('Temps (s)')
plt.ylabel('Vitesse (m/s)')
plt.title('Evolution de la vitesse de la voiture dans le looping')
plt.grid(True)
plt.legend()

# Graphique de la position angulaire
plt.subplot(2, 1, 2)
plt.plot(t, theta_deg, label='Position angulaire (degrés)', color='green')
plt.xlabel('Temps (s)')
plt.ylabel('Angle (degrés)')
plt.title('Evolution de la position de la voiture dans le looping')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print("Vitesse début looping = ", round(v_0, 3), "m/s.")
def n2():
    for n in range(len(theta_deg)) :
        if theta_deg[n] >= 360.0 :
            return n
    return -1




if n2() == -1 or (vitesse_bas_pente<v_min_entree):
    print(n2())
    print("/!\ LOOPING NON REALISABLE : \nVitesse requise : ", v_min_entree, "m/s.\nVitesse initiale : ", v_0, "m/s.")
    print("x" * 122)
    print("")
else :
    #print(theta_deg[n2()])
    vitesse_fin_looping = v_sol[n2()]
    temps_fin_looping = t[n2()]
    chrono += temps_fin_looping
    print("Vitesse fin looping =", round(vitesse_fin_looping, 3), "m/s.")
    print("Temps pour faire le looping =", round(temps_fin_looping, 3), "s.")
    print("")
    print("")
    















'''
PARTIE 3 : SAUT DE RAVIN ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

print("ETAPE 3 : SAUT DE RAVIN") 
print("")

# caractéristiques voitures

m  = garage[i].masse + 30*ailes + 15*jupe           # Masse.........................(kg)
am = garage[i].accel + (nos*0.3*garage[i].accel)    # Accélération moyenne..........(m/s²)
L  = garage[i].longueur                             # Longueur de la voiture........(m)
l  = garage[i].largeur                              # Largeur de la voiture.........(m)
h  = garage[i].hauteur                              # Hauteur de la voiture.........(m)
S_x  = l * h                                        # Surface frontale..............(m²)
S_z  = l * L + (ailes * 0.8)                        # Surface sous la voiture.......(m²)
C_x = garage[i].cx - (jupe*0.05*garage[i].cx)       # Coefficient de traînée........(sans unité)
C_z = garage[i].cz + (ailes*0.1*garage[i].cz)       # Coefficient de portance.......(sans unité)
mu  = garage[i].cf                                  # Coefficient de frottement.....(sans unité)

rho = 1.225                                         # Densité de l'air (kg/m^3)
g = 9.81                                            # Intensité de pesanteur (m/s^2)

def equadiff_3(y, t):
    x, vx, y_pos, vy = y
    v_norme = np.sqrt(vx**2 + vy**2)  
    ax = (-0.5* rho * S_x * C_x * v_norme * vx - 0.5*rho * S_z * C_z * v_norme* vy) / (m)
    ay = (-0.5 *rho * S_x * C_x * v_norme * vy + 0.5*rho * S_z * C_z * v_norme* vx) / (m) - g
    return [vx, ax, vy, ay]

# conditions initiales :
x0  = 0.0 
vx0 = vitesse_fin_looping   
y0  = 1.0 
vy0 = 0.0 
conditions_initiales = [x0, vx0, y0, vy0]

# temps pour la simulation
t = np.linspace(0, 0.8, 10000)  # Simulation sur 0.8 seconde avec 10000 points


solution = odeint(equadiff_3, conditions_initiales, t)

# extraire les solutions
x  = solution[:, 0]
y  = solution[:, 2]
vx = solution[:, 1]
vy = solution[:, 3]

def n3():
    for n in range(len(x)) :
        if round(x[n], 3) >= 9 and round(y[n], 2) == 0.00 :
            return n
    return -1
print(n3())
v_min_saut = 19.600000000000012
print(f"Vitesse minimale pour {garage[i].nom} : {round(v_min_saut, 3)} m/s")
if vitesse_fin_looping < v_min_saut :
    print(n3())
    print("SAUT NON REALISABLE")
    print("La voiture n'est pas allée assez loin.")
    print("x" * 122)
    
else :
    
    pos_fin_saut = x[n3()]
    vitesse_fin_saut = vx[n3()]
    temps_fin_saut = t[n3()]
    chrono += temps_fin_saut
    
    print("Position x fin" , round(x[n3()], 2), "m.")
    print("Position y fin",  round(y[n3()], 2), "m.")
    print("Vitesse à l'aterrissage =", round(vitesse_fin_saut, 3), "m/s.")
     

plt.figure(figsize=(12, 6))

# Graphique de la trajectoire

plt.plot(x, y, label='Trajectoire', color='black')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Evolution de la position de la voiture dans le saut')
plt.axvline(9, color = 'red' , linestyle = '--')
plt.axhline(0, color = 'red' , linestyle = '--')
plt.grid(True)
plt.legend()
plt.show()


plt.figure(figsize=(12, 6))

# Graphique de la vitesse

plt.plot(t, vx, label='Vitesse (m/s)', color='blue')
plt.xlabel('Temps (s)')
plt.ylabel('Vitesse (m/s)')
plt.title('Evolution de la vitesse de la voiture dans le saut')
plt.grid(True)
plt.legend()













'''
PARTIE 4 : FIN DE PISTE ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


print("")
print("")
print("ETAPE 4 : PISTE PLATE ") 
print("")
nos   = int(input("Pour la fin : NOS = 1 ; pas de NOS = 0 \n >>> "))
ailes = 0

m  = garage[i].masse + 30*ailes + 15*jupe           # Masse.........................(kg)
am = garage[i].accel + (nos*0.3*garage[i].accel)    # Accélération moyenne..........(m/s²)
L  = garage[i].longueur                             # Longueur de la voiture........(m)
l  = garage[i].largeur                              # Largeur de la voiture.........(m)
h  = garage[i].hauteur                              # Hauteur de la voiture.........(m)
S_x  = l * h                                        # Surface frontale..............(m²)
S_z  = l * L + (ailes * 0.8)                        # Surface sous la voiture.......(m²)
C_x = garage[i].cx - (jupe*0.05*garage[i].cx)       # Coefficient de traînée........(sans unité)
C_z = garage[i].cz + (ailes*0.1*garage[i].cz)       # Coefficient de portance.......(sans unité)
mu  = garage[i].cf                                  # Coefficient de frottement.....(sans unité)

rho = 1.225                                         # Densité de l'air (kg/m^3)
g = 9.81                                            # Intensité de pesanteur (m/s^2)

def equadiff_4(y4, t):
    v = y4[0]  
    x = y4[1] 
    a_x = (-0.5*rho * S_x * C_x / (m)) * v**2 + am - mu * g
    return [a_x, v] 


t = np.linspace(0, 3, 10000)  # temps de 0 à 3 secondes avec 10000 points

# conditions initiales :
v0 = vitesse_fin_saut  # Vitesse initiale (m/s)    (vitesse à la fin du saut)
x0 = pos_fin_saut - 9  # Position initiale (m)     (position par rapport à 9 (9m du saut)) = pos_saut - 9
y0 = [v0, x0]

solution = odeint(equadiff_4, y0, t)

vitesse   = solution[:, 0]  
position  = solution[:, 1]  

def n4():
    for n in range(len(position)):
        if position[n] >= 10 :
            return n
chrono += t[n4()]

print("Position initiale sur la piste : ", round(x0, 2), "m.")
print("Temps piste plate", round(t[n4()], 4), "secondes.")
print("Temps final :", round(chrono, 3), "secondes.")

plt.figure(figsize=(12, 6))
# Graphique de la vitesse

plt.plot(t, vitesse, label='Vitesse (m/s)', color='blue')
plt.xlabel('Temps (s)')
plt.ylabel('Vitesse (m/s)')
plt.title('Evolution de la vitesse de la voiture dans la piste')
plt.grid(True)


print("-" * 122)
