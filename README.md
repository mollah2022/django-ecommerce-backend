# Django Ecommerce Backend API

A complete Ecommerce Backend API built with Django and Django REST Framework (DRF).

This project provides RESTful APIs for user management, product management, cart management, and order processing.

---

## 🚀 Features

### User Management
- Custom User Model
- User Registration
- User Authentication
- Token Authentication
- User Profile Management

### Product Management
- Product CRUD Operations
- Product Image Upload
- Product Listing API
- Product Details API

### Cart Management
- Add products to cart
- Update cart quantity
- Remove products from cart
- View user cart

### Order Management
- Create Orders
- Order Items Management
- View User Orders
- Order Status Management


---

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- SQLite Database
- Pillow
- Django Filter
- Django CORS Headers


---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/mollah2022/django-ecommerce-backend.git
```

### 2. Navigate to Project Directory

```bash
cd django-ecommerce-backend
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate Virtual Environment

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Server will run:

```
http://127.0.0.1:8000/
```


---

## 📂 Project Structure

```
django-ecommerce-backend/

│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── user_api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── product_api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── cart/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
│
├── order/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
│
├── requirements.txt
├── manage.py
└── README.md
```


---

## 🔐 Authentication

This project uses Django REST Framework Token Authentication.

Authentication Header:

```bash
Authorization: Token <your_token>
```

Users need authentication to access protected APIs.


---

## 📌 API Modules

### User API

Features:

- User Registration
- User Login
- User Profile
- Authentication


### Product API

Features:

- Create Product
- Get All Products
- Get Product Details
- Update Product
- Delete Product
- Product Image Upload


### Cart API

Features:

- Add Product To Cart
- View Cart Items
- Update Cart Quantity
- Remove Cart Item


### Order API

Features:

- Create Order
- View User Orders
- Order Details
- Order Status Management


---

## 📦 Requirements

Main dependencies:

```
Django
djangorestframework
django-filter
django-cors-headers
Pillow
```


---

## 👨‍💻 Author

**Sajib Ahmed**

GitHub:

https://github.com/mollah2022