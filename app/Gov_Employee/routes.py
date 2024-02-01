from flask import render_template, request
from app.Gov_Employee import Gov_Employee
"""from flask_caching import Cache
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

cache = Cache(Gov_Employee, config={'CACHE_TYPE': 'simple'})"""

@Gov_Employee.route('/')
def index():
    return render_template('Gov_Employee/index.html')

"""@Gov_Employee.route('/make_requisition', methods=['GET', 'POST'])
def make_requisition():
    form = RequisitionForm()

    if form.validate_on_submit():
        item_name = form.item_name.data
        quantity = int(form.quantity.data)

        # Save requisition to PouchDB
        save_requisition(item_name, quantity)

        # Invalidate cache
        cache.clear()

        # Predict stock level and recommend reorder quantity
        predicted_stock = predict_stock(item_name, quantity)
        reorder_quantity = recommend_reorder(predicted_stock)

        return render_template('quotation.html', item_name=item_name, quantity=quantity,
                               predicted_stock=predicted_stock, reorder_quantity=reorder_quantity)

    return render_template('requisition.html', form=form)

@Gov_Employee.route('/get_quotation')
@cache.cached(timeout=60)
def get_quotation():
    # Retrieve pending requisitions from PouchDB
    requisitions = get_pending_requisitions()
    
    return jsonify({'./templates/requisitions': requisitions})

def save_requisition(item_name, quantity):
    # Save requisition to PouchDB
    data = {'item_name': item_name, 'quantity': quantity, 'status': 'pending'}
    response = requests.post(f'{pouchdb_url}', json=data)
    response.raise_for_status()"""