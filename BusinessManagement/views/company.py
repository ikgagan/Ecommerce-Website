from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
from bs4 import BeautifulSoup
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
# function for lising and searching companies
# Gagan Indukala Krishna Murthy - gi36 - 5th April 
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    # Gagan Indukala Krishna Murthy - gi36 - 5th April 
    query = """SELECT id, name, address, city, country, state, zip, website,
            (SELECT count(*) from IS601_MP3_Employees A
            WHERE A.company_id = B.id) AS employees
            FROM IS601_MP3_Companies B
            WHERE 1=1"""
    args = [] # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # Gagan Indukala Krishna Murthy - gi36 - 5th April 
    filters = ["country", "state"]
    if request.args.get("name"):
        query += " and name like %s"
        args.append(f"%{request.args.get('name')}%")
    for filter in filters:
        if request.args.get(filter):
            query += f" and {filter} = %s"
            args.append(request.args.get(filter))
    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns \
            and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY {request.args.get('column')} {request.args.get('order')}"
    # TODO change this per the above requirements
    # Gagan Indukala Krishna Murthy - gi36 - 5th April 
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
        print(f"check error{e}")
        # TODO search-9 make message user friendly
        # Gagan Indukala Krishna Murthy - gi36 - 5th April 
        flash(f"Error occurred while trying to search company: {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [(col,col) for col in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
# Gagan Indukala Krishna Murthu - gi36- April 9th
# function for adding companies
def add():
    input = request.form
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # Gagan Indukala Krishna Murthu - gi36- April 9th
        form_value = {}
        has_error = False # use this to control whether or not an insert occurs

        form_value["name"] = input.getlist('name')
        form_value["address"] = input.getlist('address')
        form_value["city"] = input.getlist('city')
        form_value["country"] = request.form.get("country")
        form_value["state"] = request.form.get("state")
        form_value["zip_code"] = input.getlist('zip')
        form_value["website"] = input.getlist('website')

        for k,v in form_value.items():
            if k != "website" and not v:
                flash(f"{k} is a mandatory field", "danger")
                has_error = True
            elif k == "website" and not v:
                form_value[k] = None

        if not has_error:
            try:
                # Gagan Indukala Krishna Murthu - gi36- April 9th
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, country,
                state, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, *form_value.values()) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                # Gagan Indukala Krishna Murthu - gi36- April 9th
                flash(f"An unexpected error while trying to edit company: {e}", "danger")
    return render_template("add_company.html", input=input)

@company.route("/edit", methods=["GET", "POST"])
# function for editing companies
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # Gagan Indukala Krishna Murthu - gi36- April 9th 
    input = request.form
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Company ID is not available ", "danger")
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            # Gagan Indukala Krishna Murthu - gi36- April 9th 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            form_value={}
            has_error = False # use this to control whether or not an insert occurs
            # Gagan Indukala Krishna Murthu - gi36- April 9th 
            form_value["name"] = input.getlist('name')
            form_value["address"] = input.getlist('address')
            form_value["city"] = input.getlist('city')
            form_value["country"] = request.form.get("country")
            form_value["state"] = request.form.get("state")
            form_value["zip_code"] = input.getlist('zip')
            form_value["website"] = input.getlist('website')
            form_value["id"] = request.args.get('id')
            # Gagan Indukala Krishna Murthu - gi36- April 9th 
            for k,v in form_value.items():
                if k != "website" and not v[0]:
                    flash(f"{k} is a mandatory field", "danger")
                    has_error = True
                elif k == "website" and not v:
                    form_value[k] = None

            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    # Gagan Indukala Krishna Murthu - gi36- April 9th 
                    result = DB.update(
                    """
                    UPDATE IS601_MP3_Companies 
                    SET name=%s, address=%s, city=%s, country=%s, state=%s,
                    zip=%s, website=%s
                    WHERE id=%s
                    """, *form_value.values())
                    if result.status:
                        print("updated")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    # Gagan Indukala Krishna Murthu - gi36- April 9th 
                    import traceback as tb
                    print(tb.format_exc())
                    flash(f"An unexpected error while trying to edit company: {e}", "danger")
        row = None
        try:
            # TODO edit-11 fetch the updated data
            # Gagan Indukala Krishna Murthu - gi36- April 9th 
            result = DB.selectOne("""SELECT * FROM IS601_MP3_Companies WHERE id=%s""", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-12 make this user-friendly
            # Gagan Indukala Krishna Murthu - gi36- April 9th 
            flash(f"An unexpected error while trying to fetch the updated company: {e}", "danger")
    # TODO edit-13 pass the company data to the render template
    # Gagan Indukala Krishna Murthu - gi36- April 9th 
    return render_template("edit_company.html", row=row, country=row.get("country"), state=row.get("state"))

@company.route("/delete", methods=["GET"])
# function for deleting companies
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    # Ggagan Indukala Krishna Murthy - gi36- April 6th
    if request.method == "GET":
        cmp_id = request.args.get("id")
        if not cmp_id:
            flash("Company ID is missing", "danger")
            return render_template("list_companies.html", **request.args)
        try:
            constraint_fix = DB.update("""
            UPDATE IS601_MP3_Employees
            SET company_id = NULL
            WHERE company_id = %s
            """,cmp_id)

            result = DB.delete("""
            DELETE FROM IS601_MP3_Companies
            WHERE id = %s
            """, cmp_id)

            if constraint_fix.status and result.status:
                flash("Successfully deleted company", "success")
        except Exception as e:
            flash(f"Unexpected error while trying to delete the Company: {e}", "danger")
            return render_template("list_companies.html", **request.args)
        new_args = dict(request.args)
        del new_args["id"]
    return redirect(url_for('company.search', **new_args))
    # Ggagan Indukala Krishna Murthy - gi36- April 6th
    