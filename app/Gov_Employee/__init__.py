from flask import Blueprint

Gov_Employee = Blueprint('Gov_Employee', __name__)

from app.Gov_Employee import routes