from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_caching import Cache
import requests
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
cache = Cache(app, config={'CACHE_TYPE': 'simple'})  # Flask-Caching does not support Redis directly
pouchdb_url = 'http://localhost:5984/inventory'  # Change this URL to your PouchDB server URL

class RequisitionForm(FlaskForm):
    item_name = StringField('Item Name')
    quantity = StringField('Quantity')
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/make_requisition', methods=['GET', 'POST'])
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

@app.route('/get_quotation')
@cache.cached(timeout=60)
def get_quotation():
    # Retrieve pending requisitions from PouchDB
    requisitions = get_pending_requisitions()
    
    return jsonify({'./templates/requisitions': requisitions})

def save_requisition(item_name, quantity):
    # Save requisition to PouchDB
    data = {'item_name': item_name, 'quantity': quantity, 'status': 'pending'}
    response = requests.post(f'{pouchdb_url}', json=data)
    response.raise_for_status()

def get_pending_requisitions():
    # Retrieve pending requisitions from PouchDB
    response = requests.get(f'{pouchdb_url}/_design/inventory/_view/pending', params={'reduce': 'false'})
    response.raise_for_status()
    return response.json()['rows']

def predict_stock(item_name, quantity):
    # Placeholder for a machine learning model (use your trained model here)
    # This is a simple linear regression model for demonstration purposes
    historical_data = get_historical_data(item_name)

    item_data = [entry['value']['stock'] for entry in historical_data if entry['value']['item_name'] == item_name]
    if not item_data:
        return quantity  # Return quantity as is if no historical data is available

    X = np.array([[entry['value']['quantity']] for entry in historical_data])
    y = np.array([entry['value']['stock'] for entry in historical_data])

    model = LinearRegression()
    model.fit(X, y)

    predicted_stock = model.predict([[quantity]])[0]
    return max(0, int(predicted_stock))

def recommend_reorder(predicted_stock):
    # Placeholder for a reorder recommendation algorithm (use your logic here)
    # This is a simple recommendation for demonstration purposes
    return max(0, int(predicted_stock * 1.2))  # Adjust as needed

def get_historical_data(item_name):
    # Retrieve historical data from PouchDB
    response = requests.get(f'{pouchdb_url}/_design/inventory/_view/historical', params={'key': f'"{item_name}"', 'reduce': 'false'})
    response.raise_for_status()
    return response.json()['rows']

if __name__ == '__main__':
    app.run(debug=True)
