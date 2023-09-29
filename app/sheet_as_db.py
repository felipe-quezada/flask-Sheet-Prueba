import gspread
from oauth2client.service_account import ServiceAccountCredentials


try:
  KEY = {
  "type": "service_account",
  "project_id": "sheets-flask-project",
  "private_key_id": "9a852ead7b5024121bf78cd81712a6eb5b9640aa",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDkBDIZX8TdG0FH\n9tM/+k6Q/Ugm4zWoR7d2Jo50C5arjkjvFSQTUoyDIAEqRqNqrxnT+WX50MFSguAE\nMjigzk577qQwQ3gOxf/vN+eGC+T9389YKJ5HMKlAEzrw/2Y+YWSHjwDNgatOPQnh\nwRHd8er/gKqMaleHuFL2HfvA329urCyzF6JJZ6i2Q1u++bpr/x6EDk94MWfyStNM\nk1xXLUXnnMY8ZWMusBMp15LXMbJKl8p6Yv90nKYhUKSyB7Dg+FBHOu0yfEEt1VT5\nrQUkOD/99NWPQoEweYW2fmpJSxzxBDFMmhNl8ALwsSHTqfe21ImrJOzFQb8QJpdd\nXe5QKWMvAgMBAAECggEACwTq45AIbwO0rW96Y7f12QrsfuNHF2P+iT6xbrPqqvgc\nLTWxLHU2UNXt8ybpGdbuzBrcOJeZPXgRWb066waIA3Q+dLil/NdzwryfEJAoQl6b\nt2/LFQypzpdp/KCTG9ulZJReyQ+wVtPF/lDQILuNYZ33Cq8kSMJPJrwUi7cgkaa4\nFWAoF8SCy9wEPaNNH548rqlixCwwLirKBfh9zaxW9hZvPO5i7RAg7oZhZDvQS4dV\nYCyvH+pfcussH6R8PZ0yDev8r5LVkd1LyQFxj/7Cx0XIrWwkUgErNRJu/LE/oyoZ\n/0Z0TGnctyYCLTn9C5CEX7uRCEebWZ52AELrqN5f1QKBgQD5+vYtTJ0W4UiEKmrg\naO2sakuZxXtafgA6xPuqLDSQY7EBRcdxsLDrBVPoEH/KzSVsTaIEhZj7h9bghIsp\nc2BGbyCzyXwB1br4r1BMFNKy9Jc36+wRDIMnmLltvqXUVaQ/09WIeo9Au/OAn+0K\nM6L/uA88WDPVMYt3yCVfX7mjcwKBgQDpgdWZ59kdH/bVPLvI+ht8E+iOo6rGeImS\ny/WjTxPDNVKm/IxA1IwK82mGirrcS2BFE5/iI0+kurM+/GMlAqX7O0Nid3Dbql8D\nUDsUMz7MT04S2dFYrLaJJuRNlvrh1uZV/jUa4x7RgkPSDtN4fob+ceJCobr430Ef\nqMLSxaXqVQKBgQC05R+6HiPbR8FTKuLWa/f5+Z2ltBuUm3ONE7jOJ1kOV6XiNt2h\n7uvH1r4mQ7JGTnfTTMZ+oTLYai9bn26Y204DCi3PDHG5XjID/dGMjNEAATFgnU/h\n8n0CbWlZ+klEQ4ktSxzNu2rovFn0bUZ6SG2ewVH9KBKyJz02u9YXk0zh8wKBgDf7\nSJp9WzAAWc0Fon+sdqpom3iXBHpQq6rl+x4L91D1l7sxEO76BhkaAlKfL+1gpNPq\nwIoWrSFxIUgYeiyFVgXFT4Jr4ELJtb21nnRZVNTmrnEWh3oa7igzisiPSdabDt3O\n9CxeByVzdY8GvuxEaVjXNMeEvq6r15EfhJXDjOOBAoGAMGIhYIBGDLHnN0WIv6In\n+cOjBYLWRwgfFi0xMbbdbIPFyTPlFbYGdf58SqTiWx7yK4MMUBO3bl+mACfUrXTp\nEH+U3XnplxGWxj6B7webKpe9fsAD+q6pOS1kr4F3kXWvrYIxJpst/SSpaDzJhdEc\n3a8UM/rgZyX187n0cosvK1U=\n-----END PRIVATE KEY-----\n",
  "client_email": "project-sheets-flask@sheets-flask-project.iam.gserviceaccount.com",
  "client_id": "106415035607986385565",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/project-sheets-flask%40sheets-flask-project.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
  }

  SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

  #autentificando google sheets api
  credentials = ServiceAccountCredentials._from_parsed_json_keyfile(KEY,SCOPE)
  client = gspread.authorize(credentials)

  #inicializando hoja de calculo
  sheet = client.open('Flask Sheets').sheet1
  
except Exception as err:
  print(f"""
        
        << {err} >>
        
        """)
