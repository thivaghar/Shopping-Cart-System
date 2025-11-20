from flask import Flask, request, redirect, flash, render_template
import mysql.connector
from decimal import Decimal

app = Flask(__name__)
app.secret_key = "123"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "clg"
}

# Initialize database
def init_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(100),
            price DECIMAL(10,2),
            quantity INT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Calculate total and discount
def calculate_total(items):
    
    total = sum(Decimal(item[2]) * Decimal(item[3]) for item in items)
    NetTotal=total
    discount = Decimal('0.0')
    if total > Decimal('100.0'):
        discount = total * Decimal('0.10')
        total -= discount
    return float(total), float(discount),float(NetTotal)

# Read - Show all items
@app.route("/")
def index():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT * FROM cart")
    items = cur.fetchall()
    conn.close()

    total, discount,NetTotal = calculate_total(items)
    return render_template("index.html", items=items, total=total,NetTotal =NetTotal , discount=discount)

# Create - Add new item
@app.route("/add", methods=["POST"])
def add_item():
    name = request.form["product_name"]
    price = float(request.form["price"])
    qty = int(request.form["quantity"])

    if qty <= 0:
        flash("Quantity must be positive!")
        return redirect("/")
    
    if price<= 0:
        flash("price must be positive!")
        return redirect("/")

    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("INSERT INTO cart (product_name, price, quantity) VALUES (%s, %s, %s)", (name, price, qty))
    conn.commit()
    conn.close()
    flash("Item added!")
    return redirect("/")

# Update 
@app.route("/update/<int:item_id>", methods=["GET", "POST"])
def update_item(item_id):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["product_name"]
        price = float(request.form["price"])
        qty = int(request.form["quantity"])
        if qty <= 0:
            flash("Quantity must be positive!")
            return redirect("/")
        cur.execute("UPDATE cart SET product_name=%s, price=%s, quantity=%s WHERE id=%s", (name, price, qty, item_id))
        conn.commit()
        conn.close()
        flash("Item updated!")
        return redirect("/")

    cur.execute("SELECT * FROM cart WHERE id=%s", (item_id,))
    item = cur.fetchone()
    conn.close()
    return render_template("update.html", item=item)

# Delete 
@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("DELETE FROM cart WHERE id=%s", (item_id,))
    conn.commit()
    conn.close()
    flash("Item deleted!")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
