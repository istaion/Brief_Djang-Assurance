# Projet Assur'AImant : développement web avec Django

![image](logo.jpg)


## Contexte Professionnel

L'équipe de développement full-stack **Unicorn Power** a décidé de répondre à un appel à d'offre pour développer un outil d'intelligence artificielle pour un assureur français, Assur'AImant. Le groupe opère historiquement sur le territoire français et a décidé de s'implanter aux États-Unis. L'application de Machine Learning permet d'estimer, en fonction de plusieurs paramètres, le montant de la redevance des futurs assurés.
Après avoir été sélectionné avec un premier POC sur Streamlit, l'équipe **Unicorn Power** propose une application web complète grâce au framework Django.


## Objectifs
- Développement d'une application Django complète et fonctionnelle
- Création d'une base de données SQLite pour stocker les informations utilisateurs
- Création d'un espace d'inscription et d'authentification
- Accès à un espace d'estimation du montant de la redevance des charges d'assurance

---

## Fonctionnalités Implémentées

### 1. Application de prédictions
- **Prédiction pour les utilisateurs** :
  - Estimation du montant en fonction des données entrées.
  - Possibilité de modifier les informations.
  - Affichage du résultat.

- **Prédiction pour les courtiers** :
  - Possibilité de réaliser des estimations sur tous les adhérents.
  - Historique des prédictions et possibilité de filtre.
  - Choix du modèle de prédiction.


### 2. Application users
- **Class Customers** :
  - Inscription.
  - Aperçu profil.
  - Modification.

- **Class Staff** :
  - Aperçu profil.
  - Modification.

### 3. Application meetings
- Visualisation du planning de rdv.
- Réservation des  créneaux.
- Restrictions (impossibilité de réserver deux fois le même créneau).

### 4. Application infos
- Une page `News` pour présenter les dernières actualités.
- Une page `About us`pour présenter l'entreprise.
- Une page `Privacy Policy`.
- Une page `Contact` permettant de contacter l'entreprise via un formulaire.

### 5. Application theme
- Gestion du front via django-tailwind


---



## Structure du Projet

| Fichier/Dossier              | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| [DJANGASSURANCE/Djang_Assurance](Djang_assurance)             | Dossier principal du projet. Contient les settings et les chemins                                               |
| [DJANGASSURANCE/app/](DJANGASSURANCE/app)      | Contient les applications pour faire les prédictions pour les users et le staff                     |
| [DJANGASSURANCE/infos](DJANGASSURANCE/infos) | Contient les templates pour toutes les pages informatives du site                           |
| [DJANGASSURANCE/meetings](DJANGASSURANCE/meetings)    | Contient les applications de gestions de réservations et de planning                      |
| [DJANGASSURANCE/staticfiles](DJANGASSURANCE/staticfiles)      | Contient l'ensemble des medias, des classes css et du js.           |
| [DJANGASSURANCE/theme](DJANGASSURANCE/theme)   | Gestion du front, contient le template de base HTML, le header et le footer    |
| [DJANGASSURANCE/user](DJANGASSURANCE/user)  | Gestion des classes Users et Staff, Inscription et Connexion         |
| [DJANGASSURANCE/db.sqlite3](DJANGASSURANCE/db.sqlite3)     | Base de données contenant toutes les tables user, staff, meetings, availability, contacts et prédictions                                      |
| [requirements.txt](requirements.txt)           | Liste des dépendances Python nécessaires pour le projet.                   |
| [manage.py](manage.py)                | Fichier de configuration et éxecution de                    |
| [bricospider.csv](bricospider.csv)           | Export des données brutes scrappées au format CSV.                                                           |
| [.gitignore](.gitignore)              | Liste des fichiers et dossiers à ignorer par Git (cache, migrations, etc.).      |


---

## Installation et Utilisation

### Prérequis
- Python 3.8+


### Étapes d’installation

Clonez le dépôt Git :

   ```bash
   git clone <git@github.com:RaoufAddeche/Brief_Djang-Assurance.git>
   ```

## Instructions

### Installez les dépendances :
```bash
pip install -r requirements.txt
```

### Lancer le serveur

```bash
cd Djang_Assurance

python manage.py runserver
```

