import json
import gspread
from decouple import config
from oauth2client.service_account import ServiceAccountCredentials

try: 
  
  KEY =  json.loads(config('KEY'))
  
  SCOPE=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

  #autentificando google sheets api
  credentials = ServiceAccountCredentials._from_parsed_json_keyfile(KEY,SCOPE)
  client = gspread.authorize(credentials)
  
  #inicializando hoja de calculo
  sheet = client.open('Flask Sheets').sheet1
  
except Exception as err:
  print(f"""
        
        << {err} >>
        
        """)