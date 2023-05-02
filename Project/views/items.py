from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from sql.db import DB
from flask_login import login_required, current_user
import traceback as tb
shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')

def get_item_count():
    query = "SELECT IFNULL(SUM(quantity),0) as total FROM IS601_S_Cart WHERE user_id = %s"
    result = DB.selectOne(query, current_user.get_id())
    if result.status and result.row:
        return int(result.row["total"])
    return 0    

@shop.route("/newrelease")
@login_required
def new_release():
    return render_template("new_release.html")

# Gagan Indukala Krishna Murthy - gi36 - 20th April
@shop.route("/shop", methods=["GET","POST"])
@login_required
def shop_list():
    # Gagan Indukala Krishna Murthy - gi36 - 20th April
    query = """SELECT id, name, description, stock, unit_price, image
               FROM IS601_S_Items WHERE visibility = 1"""
    args = []
    rows={}
    allowed_columns = ["name", "description", "unit_price"]
    for filter in allowed_columns[:-1]:
        if request.args.get(filter):
            query += f" and {filter} like %s"
            args.append(f"%{request.args.get(filter)}%")
    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns \
            and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY {request.args.get('column')} {request.args.get('order')}"
    query += f" LIMIT %s"
    ql = int(request.args.get('limit', 25))
    if ql < 1 or ql > 100:
        flash("limit value should be in the range of 1-100; Defaulting to 25")
        args.append(25)
    else:
        args.append(ql)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(tb.format_exc())
        flash("There was a problem loading items", "danger")
    return render_template("shop.html", rows=rows, allowed_columns=allowed_columns)

    # Gagan Indukala Krishna Murthy - gi36 - 20th April
@shop.route("/shop/item", methods=["GET","POST"])
@login_required
def shop_item():
        # Gagan Indukala Krishna Murthy - gi36 - 20th April
    try:
        id = request.form.get("id") or request.args.get("id") or None
        result = DB.selectOne("SELECT id, name, description, stock, unit_price, image FROM IS601_S_Items WHERE id = %s", id)
        if result.status and result.row:
            rows = result.row
    except Exception as e:
        print("Error fetching item", e)
        flash("Item not found", "danger")
        rows = []
    return render_template("view_item.html", rows=rows if rows else {})

    # Gagan Indukala Krishna Murthy - gi36 - 20th April
@shop.route("/cart", methods=["GET","POST"])
@login_required
def cart():
        # Gagan Indukala Krishna Murthy - gi36 - 20th April
    item_id = request.form.get("item_id")
    id = request.form.get("id", item_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            try:
                result = DB.selectOne("SELECT unit_price,name,stock from IS601_S_Items WHERE id = %s", id)
                print("result", result)
                if result.status and result.row:
                    unit_price = result.row["unit_price"]
                    name = result.row["name"]
                    stock = result.row["stock"]
                    if quantity > stock:
                        flash(f"{quantity} {name}s are not available; Please reduce the quantity", "danger")
                    else:
                        if item_id: 
                            result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            quantity = %(quantity)s,
                            unit_price = %(unit_price)s
                            WHERE item_id = %(id)s and user_id = %(user_id)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "unit_price":unit_price,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Updated quantity for {name} to {quantity}", "success")
                        else: 
                            result = DB.insertOne("""
                            INSERT INTO IS601_S_Cart (item_id, quantity, unit_price, user_id)
                            VALUES(%(id)s, %(quantity)s, %(unit_price)s, %(user_id)s)
                            ON DUPLICATE KEY UPDATE
                            quantity = quantity + %(quantity)s,
                            unit_price = %(unit_price)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "unit_price":unit_price,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Added {quantity} of {name} to cart", "success")
            except Exception as e:
                print("Error updating cart" ,e)
                flash("Error updating cart", "danger")
        else:
            try:
                result = DB.delete("DELETE FROM IS601_S_Cart where item_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted item from cart", "success")
            except Exception as e:
                print("Error deleting item", e)
                flash("Error deleting item from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, item_id, name, c.quantity, (c.quantity * c.unit_price) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Items i on c.item_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)   
# Gagan Indukala Krishna Murthy - gi36 - 20th April

@shop.route("/confirm_order", methods=["GET","POST"])
@login_required
def confirm_order():
# Gagan Indukala Krishna Murthy - gi36 - 20th April
    cart = []
    total = 0
    try:
        result = DB.selectAll("""SELECT c.id, item_id, name, c.quantity, i.stock, c.unit_price as cart_cost, i.unit_price as item_cost, (c.quantity * c.unit_price) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Items i on c.item_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            cart = result.rows
        has_error = False
        for item in cart:
            if item["quantity"] > item["stock"]:
                flash(f"Item {item['name']} doesn't have enough stock left", "warning")
                has_error = True
                if item["stock"] == 0:
                    result = DB.delete("DELETE FROM IS601_S_Cart where item_id = %s and user_id = %s", item["item_id"], current_user.get_id())
                    flash(f"Deleting item: {item['name']} from your cart", "warning")
                else:
                    result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            quantity = %(quantity)s,
                            WHERE item_id = %(id)s and user_id = %(user_id)s
                            """,{
                                "id":id,
                                "quantity": item["stock"],
                                "item_id":item["item_id"],
                                "user_id":item['user_id']
                            })
                    if result.status:
                        flash(f"Updated quantity for {item['name']} to {item['stock']}", "warning")
            if item["cart_cost"] != item["item_cost"]:
                flash(f"Item {item['name']}'s price has changed, please refresh cart", "warning")
                has_error = True
                result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            unit_price = %(cost)s,
                            WHERE item_id = %(id)s and user_id = %(user_id)s
                            """,{
                                "id":id,
                                "cost": item["item_cost"],
                                "item_id":item["item_id"],
                                "user_id":item['user_id']
                            })
                if result.status:
                    flash(f"Updated cost for {item['name']} to {item['item_cost']}")
            total += float(item["subtotal"] or 0) 
        if has_error:
            return redirect(url_for("shop.cart"))
    except Exception as e:
        print("Transaction exception", e)
        flash("Something went wrong", "danger")
        tb.print_exc()
        return redirect(url_for("shop.cart"))
    return render_template("pending_order.html", rows=cart, total=total)

@shop.route("/place_order", methods=["GET","POST"])
@login_required
def place_order():
    # Gagan Indukala Krishna Murthy - gi36 - 27th April
    total = float(request.form.get('total', 0))
    total = f"{total:.2f}"
    money_received = float(request.form.get("money_received", 0))
    if money_received and f"{money_received:.2f}" == total:
        flash("Payment received, proceeding to place order", "success")
    elif money_received:
        flash("Received payment is not equal to the total cost, aborting order", "danger")
        flash("Any amount debited will be refunded in 3-4 business days", "warning")
        return redirect(url_for("shop.cart"))
    else:
        flash("Payment Failed, Please try again")
        return redirect(url_for("shop.cart"))
    cart = []
    total = 0
    quantity = 0
    order = {}
    try:
        DB.getDB().autocommit = False 

        
        result = DB.selectAll("""SELECT c.id, item_id, name, c.quantity, i.stock, c.unit_price as cart_cost, i.unit_price as item_cost, (c.quantity * c.unit_price) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Items i on c.item_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            cart = result.rows
        has_error = False
        for item in cart:
            if item["quantity"] > item["stock"]:
                flash(f"Item {item['name']} doesn't have enough stock left", "warning")
                has_error = True
            if item["cart_cost"] != item["item_cost"]:
                flash(f"Item {item['name']}'s price has changed, please refresh cart", "warning")
                has_error = True
            total += int(item["subtotal"] or 0)
            quantity += int(item["quantity"])
        
        order_id = -1
        if not has_error:
            result = DB.insertOne("""INSERT INTO IS601_S_Orders (first_name, last_name,
                                total_price, number_of_items, user_id, address, payment_method,
                                money_received)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", request.form.get('fname'), request.form.get('lname'),
                                    total, quantity, int(current_user.get_id()),
                                    request.form.get('address'),request.form.get('payment'),
                                    money_received)
            if not result.status:
                flash("Error generating order", "danger")
                DB.getDB().rollback()
                has_error = True
            else:
                order_id = int(DB.db.fetch_eof_status()["insert_id"])
                order["order_id"] = order_id
                order["total"] = total
                order["quantity"] = quantity
        if order_id > -1 and not has_error:
            result = DB.insertOne("""INSERT INTO IS601_S_OrderItems (quantity, unit_price, order_id, item_id, user_id)
            SELECT quantity, unit_price, %s, item_id, user_id FROM IS601_S_Cart c WHERE c.user_id = %s""",
            order_id, current_user.get_id())
            if not result.status:
                flash("Error recording order history", "danger")
                has_error = True
                DB.getDB().rollback()
        if not has_error:
            result = DB.update("""
            UPDATE IS601_S_Items 
                set stock = stock - (select IFNULL(quantity, 0) FROM IS601_S_Cart WHERE item_id = IS601_S_Items.id and user_id = %(uid)s),
                visibility = (select if(stock - (select IFNULL(quantity, 0) FROM IS601_S_Cart WHERE item_id = IS601_S_Items.id and user_id = %(uid)s)>0, 1, 0) 
                FROM IS601_S_Cart WHERE item_id = IS601_S_Items.id and user_id = %(uid)s) 
                WHERE id in (SELECT item_id from IS601_S_Cart where user_id = %(uid)s)
            """, {"uid":current_user.get_id()} )
            if not result.status:
                flash("Error updating stock", "danger")
                has_error = True
                DB.getDB().rollback()
        if not has_error:
            result = DB.delete("DELETE FROM IS601_S_Cart WHERE user_id = %s", current_user.get_id())
    
        if not has_error:
            DB.getDB().commit()
            flash("Purchase successful!", "success")
        else:
            return redirect(url_for("shop.cart"))
        order_info = [{"First_name": request.form.get('fname'),
                        "Last_name": request.form.get('lname'),
                        "Address": request.form.get('address'),
                        "Payment_Method": request.form.get('payment')
                        }]
    except Exception as e:
        print("Transaction exception", e)
        flash("Something went wrong", "danger")
        flash("Any amount debited will be refunded in 2-4 business days", "warning")
        tb.print_exc()
        return redirect(url_for("shop.cart"))
    return render_template("order_summary.html", rows=cart, order=order, order_info=order_info)
# Gagan Indukala Krishna Murthy - gi36 - 27th April

@shop.route("/payment", methods=["POST"])
@login_required
# Gagan Indukala Krishna Murthy - gi36 - 27th April
def payment():
    missing = False
    reqd_fields = ['fname', 'lname', 'address', 'payment']
    form_data = {}
    for field in reqd_fields:
        if not request.form.get(field):
            flash(f"Missing Required Field: {field}, Please Try again", "danger")
            missing = True
        else:
            form_data[field] = request.form.get(field)
    print(missing)
    if missing:
        return redirect(url_for("shop.confirm_order"))
    return render_template("payment.html", form=form_data)

@shop.route("/orders", methods=["GET"])
@login_required
# Gagan Indukala Krishna Murthy - gi36 - 27th April
def orders():
    rows = []
    try:
        result = DB.selectAll("""
        SELECT id, total_price, number_of_items, created FROM IS601_S_Orders WHERE user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
    return render_template("orders.html", rows=rows)

@shop.route("/order", methods=["GET", "POST"])
@login_required
def order():
    # Gagan Indukala Krishna Murthy - gi36 - 20th April
    rows = []
    total = 0
    id = request.args.get("id")
    print(f"check working {id}")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.orders"))
    try:
        # locking query to order_id and user_id so the user can see only their orders
        result = DB.selectAll("""
        SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal 
        FROM IS601_S_OrderItems oi 
        JOIN IS601_S_Items i on oi.item_id = i.id 
        WHERE order_id = %s ANd user_id = %s
        """, id, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
        result = DB.selectAll("""
        SELECT first_name, last_name, address, payment_method
        FROM IS601_S_Orders where id=%s
        """, id)
        if result.status and result.rows:
            order_info = result.rows
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
        rows = []
        total = None
        order_info = []
    print(rows)
    print(order_info)
    return render_template("order.html", rows=rows, total=total, order_info=order_info )
# Gagan Indukala Krishna Murthy - gi36 - 20th April