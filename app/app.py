import sys
from flask import Flask, render_template, redirect, request
from sheet_as_db import sheet 
from werkzeug.exceptions import HTTPException

# create serve
app = Flask(__name__)

# controlador de errores
@app.errorhandler(Exception)
def error_handle(e):
  if isinstance(e, HTTPException):
    return e
  elif (request.path == '/list'):
    return {"description": "internal_error"}, 500
  return render_template('error_page.html', e='No se pudo conectar con la hoja de cálculo'), 500

@app.errorhandler(404)
def error_not_found(e):
  return redirect('/')

# ruta home
@app.route('/')
def index():
  data = sheet.get_all_records()
  return render_template('index.html', data=data)

# endpoint get all
@app.get('/list')
def get_list():
  get_list = sheet.get_all_records()
  return get_list

# renderizado de errores
@app.route('/error_page')
def error_page():
  return render_template('error_page.html', e='No se pudo conectar con la hoja de cálculo'), 500

if (__name__ == '__main__'):
  if (sys.argv.__contains__('debug=True')):
    app.run(debug=True)
  else:
    app.run()