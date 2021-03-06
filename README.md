## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Déploiement

Pour ce projet nous utilisons un pipeline CircleCI qui se charge de préparer notre application en plusieurs étapes:
  * Récupération du code depuis la branche `master`
  * Création d'un environnement virtuel
  * Installation des dépendances
  * Lancement des tests via `pytest`
  * Installation de `Heroku CLI`
  * Ajout des variables d'environnements sur heroku
  * Création de l'image et envoie vers le répertoire de container
  * Envoie de l'image vers Heroku

Il vous faudra donc créer un compte sur le site [Heroku](https://www.heroku.com/). et créér une application, pensez à modifier le nom de l'application dans le fichier de configuration `.circleci/config.yml`

Ensuite connectez-vous à votre compte CircleCI, crééz un pipeline et séléctionnez la branche `master` pour le déploiement.
Ajoutez les variables d'environnements suivantes au projet que vous venez de créér:

```yaml
SECRET_KEY=<your-secret-key>
DEBUG=True
ALLOWED_HOSTS='localhost,0.0.0.0,127.0.0.1,<your-app>.herokuapp.com'
DSN='<your-sentry-dsn-key'
```

Vous pouvez maintenant déployer votre application en utilisant circleCI, il vous suffira de pousser du code vers votre branche `master` pour que le pipeline déclenche automatiquement les étapes précédentes.