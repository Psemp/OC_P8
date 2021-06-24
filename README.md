# OC_P8
 *Créez une plateforme pour amateurs de Nutella*

1. ## Description de l'application

​	Ce projet est une application Web visant a utiliser les donnees d'Open Food Facts pour proposer une alternative plus saine aux produits du quotidien.
Le site propose aux utilisateurs de créer un compte pour accéder a des fonctions supplémentaires : les utilisateurs titulaires d'un compte peuvent enregistrer leurs produits favoris pour les retrouver plus tard.

​	La page de détail de chaque produit propose des informations sur l'aliment en question : le nutriscore, certaines données alimentaires pour 100g, les magasins ou le produit peut être trouvé, sa marque et une image du produit. Un lien vers Open Food Facts est également présent sur la page si l'utilisateur souhaite accéder a toutes les informations proposées par Open Food Facts (OFF).

​	L'application est construite en utilisant le Framework Django, en Python. La base de données recommandée pour utiliser l'application est PostgreSQL. Le site est construit grâce a bootstrap pour le CSS.

​	Le site est actuellement déployé sur Heroku a l'adresse : https://purbeurre-sempp.herokuapp.com/

2. ## Fonctionnement

- Prérequis : Python 3, PostgreSQL

- 1. Cloner le repo
  2. Créer un environnement virtuel puis installer les requirements (`pip install -r requirements.txt`)
  3. Modifier le fichier settings.py pour inclure vos identifiants SQL (preferez `DATABASE_URL` en production)
  4. Effectuer les migrations : Dans le dossier purbeurre (ou se trouve manage.py), effectuer : `python manage.py makemigrations` `puis python manage.py migrate`
  5. Une fois les migrations effectuées, créer un superuser avec `python manage.py createsuperuser`
  6. Récupérer les données OpenFoodFacts : `python manage.py get_categories` puis `python manage.py get_products` . Au besoin, les tables de produits et catégories peuvent être purgées avec la commande `python manage.py purge_db`
  7. Lancer le serveur local avec python manage.py runserver, effectuer les tests avec `python manage.py test` (Selenium, présent dans les requirements, est requis pour les tests)

  

3. ## Credits

   <u>Données alimentaires :</u> Open Food Facts (https://fr.openfoodfacts.org/)

   <u>Icones :</u> thenounproject.com (l'identité de chaque créateur est mentionné sur l'icone)

   <u>Template :</u> https://blackrockdigital.github.io/startbootstrap-creative/

   <u>Wallpaper :</u> Kawin Harasai https://unsplash.com/photos/k60JspcBwKE

