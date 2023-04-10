from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')
# Gagan Indukala Krishna Murthy - gi36 - April 6th

@employee.route("/search", methods=["GET"])
# Function for searching and listing employees
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    # Gagan Indukala Krishna Murthy - gi36 - April 6th
    query = """ SELECT A.id, first_name, last_name, email, company_id, 
                IF(name is not null, name,'N/A') as company_name 
                FROM IS601_MP3_Employees A
                LEFT JOIN IS601_MP3_Companies B on A.company_id=B.id
                WHERE 1=1"""
    args = [] # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # Gagan Indukala Krishna Murthy - gi36 - April 6th
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # TODO search-3 append like filter for first_name if provided
    # TODO search-4 append like filter for last_name if provided
    # TODO search-5 append like filter for email if provided
    # TODO search-6 append equality filter for company_id if provided
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    # Gagan Indukala Krishna Murthy - gi36 - April 6th
    filters = [("fn", "first_name"), ("ln", "last_name"), ("email", "email")]
    for filter_arg,filter in filters:
        if request.args.get(filter_arg):
            query += f" and {filter} like %s"
            args.append(f"%{request.args.get(filter_arg)}%")
    if request.args.get("company"):
        query += f" and company_id = %s"
        args.append(request.args.get('company'))
    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns \
            and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY {request.args.get('column')} {request.args.get('order')}"
    # Gagan Indukala Krishna Murthy - gi36 - April 6th
    query += f" LIMIT %s"
    ql = int(request.args.get('limit', 10))
    if ql < 1 or ql > 100:
        flash("limit value should be in the range of 1-100; Defaulting to 10")
        args.append(10)
    else:
        args.append(ql)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        # Gagan Indukala Krishna Murthy - gi36 - April 6th
        print(e)
        flash(f"Unexpected error while trying to search employee: {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    # Gagan Indukala Krishna Murthy - gi36 - April 6th
    allowed_columns = [(col,col) for col in allowed_columns]
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
# Gagan Indukala Krishna Murthy - gi36 - April 6th
# Function for adding employees 
def add():
    input = request.form
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # TODO add-5a verify email is in the correct format
        # Gagan Indukala Krishna Murthy - gi36 - April 9th
        form_value = {}
        has_error = False # use this to control whether or not an insert occurs

        form_value["first_name"] = input.getlist("first_name")
        form_value["last_name"] = input.getlist("last_name")
        form_value["company"] = request.form.get("company") or None
        form_value["email"] = input.getlist("email")

        for k,v in form_value.items():
            if k != "company" and not v:
                flash(f"{k} is a mandatory field", "danger")
                has_error = True
            # elif k == "company" and not v:
            #     form_value[k] = None

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name, last_name, company_id, email)
                VALUES (%s, %s, %s, %s)
                """, *form_value.values()
                ) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record successfully", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(f"Unexpected error while trying to search employee: {e}", "danger")
    return render_template("add_employee.html", input=input)

@employee.route("/edit", methods=["GET", "POST"])
# Gagan Indukala Krishna Murthy - gi36 - April 6th
# Function for editing employees 
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # Gagan Indukala Krishna Murthy - gi36 - April 6th
    input = request.form
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Company ID is not available ", "danger")
        redirect('/employee/search')
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company (may be None)
            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            # Gagan Indukala Krishna Murthy - gi36 - April 10th
            form_value={}
            has_error = False # use this to control whether or not an insert occurs
            
            form_value["first_name"] = input.get('first_name')
            form_value["last_name"] = input.get('last_name')
            form_value["company"] = request.form.get("company") or None
            form_value["email"] = input.get('email')
            form_value["id"] = id

            for k,v in form_value.items():
                if k != "company" and not v:
                    flash(f"{k} is a mandatory field", "danger")
                    has_error = True
            
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    # Gagan Indukala Krishna Murthy - gi36 - April 10th
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees 
                    SET first_name=%s, last_name=%s, company_id=%s, email=%s
                    WHERE id=%s
                    """, *form_value.values())
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    # Gagan Indukala Krishna Murthy - gi36 - April 10th
                    print(e)
                    flash(f"Unexpected error while trying to search employee: {e}", "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            # Gagan Indukala Krishna Murthy - gi36 - April 10th
            result = DB.selectOne("""
            SELECT * FROM IS601_MP3_Employees A
            LEFT JOIN IS601_MP3_Companies B on A.company_id=B.id
            WHERE A.id = %s
            """, id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            # Gagan Indukala Krishna Murthy - gi36 - April 10th
            print(e)
            flash(f"Unexpected error while trying to search employee: {e}", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row, company=row.get("company_id"))

@employee.route("/delete", methods=["GET"])
def delete():
    # Function for deleting employees 
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    # Gagan Indukala Krishna Murthy - gi36 - April 6th
    if request.method == "GET":
        emp_id = request.args.get("id")
        if not emp_id:
            flash("Employee ID is missing", "danger")
            return render_template("list_employees.html")
        try:
            result = DB.delete("""
            DELETE FROM IS601_MP3_Employees
            WHERE id = %s
            """, emp_id)
            if result.status:
                flash("Successfully deleted employee", "success")
        except Exception as e:
            flash(f"Unexpected error while trying to delete the employee: {e}", "danger")
        new_args = dict(request.args)
        del new_args["id"]
    return redirect(url_for("employee.search", **new_args))
    # Gagan Indukala Krishna Murthy - gi36 - April 6th