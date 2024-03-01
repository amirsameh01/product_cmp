
# Product Compare

Product Compare is a Django project that allows users to compare products and save favorites.

## Features

-   Browse and compare products
-   Create an account to save favorites
-   Manage favorites
-   Admin panel to manage products

## Usage

### Browsing Products

-   Homepage displays all products
-   Compare features across products

### Managing Favorites (requires login)

-   Create an account
-   Click "Add to Favorites" on any product to save to your favorites
-   View list of favorited products in the favorite tab
-   click "Remove from Favorites" to remove products from favorites

### Admin Features

-   Create admin user with  `python manage.py createsuperuser`
-   Access admin panel at  `/admin`
-   Manage products, product types, attributes, and values

To add new products follow these step in order:

1.  Add attributes under Attribute Definitions table
2.  Add product types under Product Types table
3.  Add products under Products table
4.  Assign attributes to products using Product Attributes table

## Project Setup

1.  Clone repo
2.  Setup project

    #do this once
    python3 -m venv .venv
    
    source .venv/bin/activate  #On Windows use `.venv\Scripts\activate`
    
    #do this once
    pip install -r requirements.txt
    
    #run migrations
python manage.py makemigrations
    python manage.py migrate

6.  Create admin user

    python manage.py createsuperuser
   

8.  Run development server  `python manage.py runserver`
