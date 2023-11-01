# Django REST Framework E-commerce Website

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This is a Django REST Framework-based e-commerce website project.

## Project Overview

This project serves as an e-commerce website with a RESTful API for managing products, categories, users, and orders. The website offers the following features:

- Feature 1: Create Products, Categories, Brands.
- Feature 2: Testing the Models, API endpoints.
- ...

## Getting Started

To set up and run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Demo-23home/DRF_Ecommmerce-Webstie.git
   cd DRF_Ecommerce-Website

2.Create a virtual environment and install dependencies:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

3.Apply migrations and create a superuser:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4.Start the development server:
```
python manage.py runserver
```

5.Access the admin panel at http://localhost:8000/admin/ and the API endpoints at http://localhost:8000/api/.

6.Testing
This project includes comprehensive testing for models and API endpoints. To run the tests, use the following command:
```
pytest
```

7.API Endpoints
Here's an example of how to document an endpoint:

List Products
URL: /api/products/

HTTP Method: GET

Description: list all products.

Contributing
If you'd like to contribute to this project, please follow our contribution guidelines.

License
This project is licensed under the MIT License.
