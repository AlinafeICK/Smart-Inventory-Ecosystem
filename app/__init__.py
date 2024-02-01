""" Maib entry point of App"""

from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


#Blueprint register
    
    from app.Gov_Employee.routes import Gov_Employee
    app.register_blueprint(Gov_Employee)
    from app.Evaluator.routes import Evaluator
    app.register_blueprint(Evaluator)
    from app.Sys_Admin.routes import Sys_Admin
    app.register_blueprint(Sys_Admin)
    
    return app


"""from App.Evaluator.routes import Evaluator"""
"""from App.Sys_Admin.routes import Sys_Admin"""
"""from App.Warehouse_Operator.routes import Warehouse_Operator"""