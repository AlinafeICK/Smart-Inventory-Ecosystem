from flask import render_template, request
from app.Evaluator import Evaluator

@Evaluator.route('/Evaluator')
def index():
    return render_template('Evaluator/index.html')