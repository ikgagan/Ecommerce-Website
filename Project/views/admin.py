import traceback as tb
from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from views.forms import ItemForm
from sql.db import DB
from roles.permissions import admin_permission
from flask_login import login_required, current_user
admin = Blueprint('admin', __name__, url_prefix='/',template_folder='templates')
# Gagan Indukala Krishna Murthy - gi36 - April 21th

@admin.route("/admin/item", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def item():
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    type = "Edit" if id else "Create"
    if form.validate_on_submit():
        if form.id.data: # it's an update
            try:
                result = DB.update("UPDATE IS601_S_Items set name = %s, description = %s, stock = %s, unit_price = %s, image=%s WHERE id = %s",
                form.name.data, form.description.data, form.stock.data, form.unit_price.data, form.image.data, form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating item", e)
                flash(f"Error updating item {form.name.data}", "danger")
        else: # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_S_Items (name, description, stock, unit_price, image) 
                VALUES (%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data, form.stock.data, form.unit_price.data, form.image.data)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = ItemForm() # clear form
            except Exception as e:
                print("Error creating item", e)
                flash(f"Error creating item {form.name.data}", "danger")
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, stock, unit_price, image FROM IS601_S_Items WHERE id = %s", id)
            if result.status and result.row:
                    form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
    return render_template("item.html", form=form, type=type)
    
@admin.route("/admin/view_item", methods=["GET","POST"])
# Gagan Indukala Krishna Murthy - gi36 - April 21th
@admin_permission.require(http_exception=403)
def view_item():
    rows={}
    try:
        id = request.args.get("id", None)
        result = DB.selectOne("SELECT id, name, description, stock, unit_price, image FROM IS601_S_Items WHERE id = %s", id)
        if result.status and result.row:
            rows = result.row
    except Exception as e:
        print("Error fetching item", e)
        flash("Item not found", "danger")
    return render_template("view_item.html", rows=rows if rows else {})

@admin.route("/admin/items/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    # Gagan Indukala Krishna Murthy - gi36 - April 21th
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_S_Items WHERE id = %s", id)
            if result.status:
                flash("Deleted item", "success")
        except Exception as e:
            print("Error deleting item",e)
            flash("Error deleting item", "danger")
    return redirect(url_for("admin.items"))


@admin.route("/admin/items", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def items():
    # Gagan Indukala Krishna Murthy - gi36 - April 21th
    rows = {}
    query = """SELECT id, name, description, stock, unit_price, image, visibility
               FROM IS601_S_Items LIMIT 25"""
    try:
        result = DB.selectAll(query)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(tb.format_exc())
        flash("There was a problem loading items", "danger")
    return render_template("admin_items.html", rows=rows)
# Gagan Indukala Krishna Murthy - gi36 - April 21th