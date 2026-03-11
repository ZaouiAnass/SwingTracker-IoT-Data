# SwingTracker-IoT-Data
Batte de baseball intelligente (IoT) : acquisition de données capteurs en C++ (Arduino), simulation RDM/Balistique en Python et visualisation mobile pour l'amélioration des performances sportives.
# ⚾ SwingTracker - Système Embarqué & Analyse Biomécanique (IoT)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)

## 📝 Présentation du Projet
**SwingTracker** est une batte de baseball intelligente développée dans le cadre de mon projet d'ingénierie (TIPE). L'objectif est de mesurer en temps réel la force, la vitesse et l'angle d'impact d'une frappe. 

Ce projet pluridisciplinaire couvre toute la chaîne de valeur d'un produit IoT :
1. **Modélisation physique et mécanique (RDM) en Python.**
2. **Électronique embarquée et traitement du signal (Arduino/C++).**
3. **Application Mobile pour la visualisation des données.**

> 📄 **Retrouvez la présentation complète de l'étude dans le dossier `docs/SwingTracker TIPE CNC.pdf`**

## ⚙️ Architecture Matérielle (Code dans `/arduino_code`)
Le cœur du système repose sur une acquisition de données haute fréquence synchronisée par un microcontrôleur :

* **Microcontrôleur :** Arduino Uno.
* **Capteur de Force :** Jauge de contrainte (Loadcell CZL635) montée en Pont de Wheatstone, couplée à un amplificateur/convertisseur 24 bits **HX711**.
* **Capteur de Mouvement :** **MPU6050** (Accéléromètre et Gyroscope 6 axes) permettant l'intégration numérique de la vitesse et de l'angle.
* **Connectivité :** Module Bluetooth **HC-05** pour la transmission sans fil des données vers l'application.

## 📊 Modélisation et Traitement des Données (Code dans `/python_simulations`)
Avant la conception matérielle, une étude balistique et mécanique approfondie a été scriptée en Python (NumPy, Matplotlib) :

* **Étude Balistique (Projectile) :** Résolution des équations différentielles de la trajectoire en prenant en compte la force de traînée aérodynamique. Détermination de l'angle de frappe optimal (35°).
* **Résistance des Matériaux (RDM) :** Calcul de l'effort tranchant et du moment fléchissant appliqués sur la batte en bois d'érable. Utilisation de la loi de Hooke pour lier la déformation mesurée par la jauge à la force réelle d'impact.
* **Traitement du Signal :** Échantillonnage, filtrage passe-bas (4 Hz) et intégration numérique (Méthode des trapèzes) des données brutes de l'accéléromètre pour obtenir la vitesse de frappe en m/s.

## 📱 Application Mobile UI
Une interface utilisateur a été développée en No-code (Adalo) pour réceptionner et exploiter les données transmises via Bluetooth :
* Tableau de bord affichant les KPI en temps réel (Force en Newton, Vitesse en m/s, Angle en degrés).
* Système d'authentification sécurisé.
* Base de données relationnelle sauvegardant l'historique des frappes par utilisateur.
