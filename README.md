# 🛒 Shopping Cart System (Flask)

A simple and efficient **Shopping Cart System** built using **Python and Flask**. This project demonstrates the core functionality of an e-commerce application, including product listing, cart management, and total price calculation.

---

## 📌 Project Overview

This project simulates a basic **online shopping experience** where users can:

- Browse products  
- Add items to their cart  
- Update quantities  
- Remove items  
- View total cost dynamically  

It is designed to strengthen backend development skills using **Flask** and fundamental web concepts.

---

## 🚀 Features

- 🛍️ Product listing page  
- ➕ Add items to cart  
- 🔄 Update product quantity  
- ❌ Remove items from cart  
- 💰 Automatic total price calculation  
- 🌐 Lightweight Flask web application  

---

## 🛠️ Technologies Used

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS (Jinja2 Templates)  
- **Database:** SQLite / In-memory (based on implementation)  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```
Shopping Cart System/
│── app.py
│── templates/
│   ├── index.html
│   ├── cart.html
│── static/
│   ├── css/
│   ├── images/
│── models/ (optional)
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/thivaghar/Shopping-Cart-System.git
cd Shopping-Cart-System/Shopping\ Cart\ System
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

http://127.0.0.1:5000/

---

## 💡 How It Works

1. Products are displayed on the homepage  
2. Users can add items to the cart  
3. Cart stores selected items (session-based or backend logic)  
4. Users can update or remove items  
5. Total price is calculated dynamically  

---

## 🎯 Learning Objectives

- Build web applications using **Flask**  
- Understand **routing, templates, and sessions**  
- Implement **cart logic and state management**  
- Work with **frontend + backend integration**  

---

## 🔮 Future Improvements

- User authentication (login/signup)  
- Database integration (MySQL/PostgreSQL)  
- Payment gateway integration  
- REST API version of the cart system  
