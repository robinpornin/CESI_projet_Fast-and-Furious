# Projet Fast & Furious – Simulation de trajectoires en Python

## 📌 Présentation
Projet académique fictif réalisé dans le cadre de la formation au CESI.  
L’objectif est de **simuler numériquement les trajectoires de différentes voitures** sur une piste complexe, en s’appuyant sur **les lois fondamentales de la mécanique de Newton**.

Ce projet met en œuvre des outils mathématiques et informatiques pour modéliser le mouvement de véhicules en dynamique.

---

## 🚗 Véhicules simulés
Les voitures sont modélisées à l’aide de la **programmation orientée objet (POO)** :

- Dodge Charger  
- Toyota Supra  
- Chevrolet Camaro  
- Mazda RX-7  
- Nissan Skyline  
- Mitsubishi Lancer  

Chaque véhicule est représenté par une classe avec ses propres paramètres physiques.

---

## 🧩 Déroulement de la simulation
Le programme simule une piste composée de plusieurs phases :

1. **Plan incliné**
   - Calcul de la vitesse et du temps en bas de pente
   - Prise en compte des frottements et de l’aérodynamique

2. **Looping**
   - Calcul de la vitesse minimale d’entrée
   - Vérification de la faisabilité physique du looping

3. **Saut de ravin**
   - Simulation balistique avec forces aérodynamiques
   - Étude de la portée et de la vitesse à l’atterrissage

4. **Piste plate**
   - Phase finale d’accélération et fin de parcours
   - Calcul du temps total du parcours

---

## ⚙️ Fonctionnement
- Modélisation des équations du mouvement à partir des lois de Newton  
- Résolution d’équations différentielles non linéaires  
- Simulation temporelle des trajectoires et vitesses  
- Visualisation graphique des résultats  

---

## 🧠 Technologies et bibliothèques utilisées
- **Python**
- **ODEINT** (Ordinary Differential Equation INTegrator)  
  → Résolution numérique d’équations différentielles non linéaires
- **Matplotlib**  
  → Tracé des trajectoires et des courbes d’évolution des vitesses
- **Programmation orientée objet (POO)**

---

## 🎯 Compétences développées
- Modélisation physique et mathématique
- Résolution numérique d’équations différentielles
- Programmation Python avancée
- Programmation orientée objet
- Visualisation de données scientifiques

---

## ⚠️ Remarque
Ce projet est **purement fictif** et à vocation pédagogique.  
Les véhicules et leurs performances ne reflètent pas des données réelles.
