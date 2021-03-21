# PyShop
Simple Crud Django Ecommerce App

## Install django in machine
`  pip install django==[VERSION] `
`  pip install django==3.1 `

## Start Django
` django-admin startproject [PROJECT-NAME] .[PERIOD CURRENT FOLDER] `
` django-admin startproject pyshop . `

## Run the project
` python manage.py runserver `

## Generate New sub apps and reistereed in settings
`  python manage.py startapp products `

## MAke migration
`  python manage.py makemigrations ` // endure they are registered in settings for apps
`  python manage.py migrate ` // runs the migration the existing migrations to db

## Admin
- Usually creates its own admin panel
- Register the models to the admin via the admin.py [admin.site.register(Offer)]
- To create super user
` python manage.py createsuperuser ` // admin@pyshop.com {admin} - 123456

### Customiing admin view
- Use admin.py file in the app class ProductAdmin(admin.ModelAdmin):

## Template view
``` Product.objects.all() # returns all
    Product.objects.filter() # retuns where eg out of stock
    Product.objects.get() # retuns single product
    Product.objects.save() # saves record 
```
- Create folder templates in the app
- ` {{ product.name }} ` render in html [echo]
- ` {% for product in products %} ` code written in templates
- objects are passed to templates in view.py through a dictionary
- Register templates global register them in settings under line 59