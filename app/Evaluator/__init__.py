from flask import Blueprint

Evaluator = Blueprint('Evaluator', __name__)

from app.Evaluator import routes