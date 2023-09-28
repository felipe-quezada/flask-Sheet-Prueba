import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

#autentificando google sheets api
credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', SCOPE)
client = gspread.authorize(credentials)

#inicializando hoja de calculo
sheet = client.open('Flask Sheets').sheet1