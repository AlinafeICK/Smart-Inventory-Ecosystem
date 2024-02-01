from flask import Blueprint

Sys_Admin = Blueprint('Sys_Admin', __name__)

from app.Sys_Admin import routes