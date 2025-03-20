# **Little Lemon - Django Project**  

A Django-based web application with a **JavaScript and HTML frontend**, designed to manage restaurant bookings and menu items.  

> 🏆 **Capstone project for the Meta Backend Specialization on Coursera.**  

## 🚀 Features  
- 🍽 **Restaurant Menu Management**  
- 📅 **Table Booking System**  
- 🔗 **REST API Endpoints for Data Access**  
- ⚡ **Django Backend with DRF (Django REST Framework)**  

## 🛠 Technologies Used  
- **Django**  
- **Django REST Framework**  
- **JavaScript**  
- **HTML**  

## 📌 Installation & Setup  

Follow these steps to set up and run the project locally:  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/littlelemon.git
cd littlelemon
```

### **2️⃣ Create a Virtual Environment**  
```sh
python -m venv venv
```
Activate the virtual environment:  
- **Windows:**  
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```sh
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**  
```sh
pipenv install --ignore-pipfile
```

### **4️⃣ Apply Migrations**  
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser (Optional, for Admin Panel)**  
```sh
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### **6️⃣ Run the Development Server**  
```sh
python manage.py runserver
```
The application will be available at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**  

---

## 📌 Available Endpoints  

| **Endpoint** | **View** | **Description** |
|-------------|---------|----------------|
| `/restaurant/` | `restaurant.views.index` | Home |
| `/restaurant/booking/` | `rest_framework.routers.APIRootView` | API Root |
| `/restaurant/booking/tables/` | `restaurant.views.BookingViewSet` | Booking List |
| `/restaurant/booking/tables/<int:pk>/` | `restaurant.views.BookingViewSet` | Booking Detail |
| `/restaurant/menu/` | `restaurant.views.MenuItemView` | Menu Overview |
| `/restaurant/menu/<int:pk>/` | `restaurant.views.SingleMenuItemView` | Single Menu Item |
| `/restaurant/menu/menu/` | `restaurant.views.MenuItemView` | Full Menu |
| `/restaurant/menu/menu/<int:pk>/` | `restaurant.views.SingleMenuItemView` | Menu Item Detail |

---
