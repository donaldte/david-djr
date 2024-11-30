Projet de Gestion Hôtelière et de Réservation en Ligne API

Description
Ce projet consiste en une application de gestion hôtelière et de réservation en ligne. Il permet aux utilisateurs de rechercher des hôtels, réserver des chambres, consulter les avis, gérer les équipements, et plus encore. L'API est construite avec Django REST Framework (DRF) et utilise PostgreSQL comme base de données.

Technologies utilisées:
Backend : Django REST Framework
Base de données : PostgreSQL
Authentification : JSON Web Tokens (JWT)
Environnement de développement : Python 3.8+, venv
Gestion des dépendances : pip, requirements.txt


Api pour recuperer la liste des hotels
Api pour recuperer les hotels par villes par nom par pays
Api operation de CRUD sur un hotel specifique
Api pour recuperer les chambres disponibles d'un hotel ( filtrer par types de chambre , par disponibilite par prix
Api operation CRUD chambre
Api pour reserver une chambre
Api pour recuperer toutes les reservations d'un utilisateur
Api CRUD d'une reservation
Api connexion (Avec JWT) , register d'un utilisateur 
Api pour modifier le profil d'un utilisateur
Api pour recuperer les information du profil d'un utilisateur
Api de deconnexion
Api CRUD avis hotel
Api pour recuperer les details d'une transaction
Api pour creer une transaction
Gestion des transactions de paiement et des historiques.

1 Cloner le dépôt
git clone

2 Créer et activer un environnement virtuel : python3 -m venv venv apres avoir cree l'environement virtuel :     # Sur Windows, utilisez venv\Scripts\activate
3 Installer les dépendances : pip install -r requirements.txt
4 Configurer la base de données PostgreSQL
5 Appliquer les migrations de la base de données : Python manage.py makemigrations et ensuite python manage.py migrate
6 Créer un superutilisateur (admin) : python manage.py createsuperuser
7 Démarrer le serveur de développement : python manage.py runserver  : Vous pouvez acceder vie l'adresse http://127.0.0.1:8000/
8 Tests  unitaire : python manage.py test

Licence

