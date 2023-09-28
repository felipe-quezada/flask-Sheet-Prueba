from flask import Flask, render_template
from sheet_as_db import sheet

# create serve
app = Flask(__name__)

# ruta home
@app.route('/')
def index():
  return render_template('index.html')

# envia toda la hoja de calculo
@app.route('/list')
def get_list():
  get_list = sheet.get_all_records()
  return get_list

if (__name__ == '__main__'):
  app.run(debug=True)