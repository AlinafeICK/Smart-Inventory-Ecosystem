from flask import render_template, request
from app.Sys_Admin import Sys_Admin

@Sys_Admin.route('/Sys_Admin')
def index():
    return render_template('Sys_Admin/index.html')