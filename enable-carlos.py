import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo JSON con las credenciales de la cuenta de servicio
credentials_file = '/home/carlos/Trabajo/Charla/charla-utn/charladevops-9715a69aa772.json'

# Correo electrónico del usuario al que deseas dar permisos
user_email = 'cpereyra82@gmail.com'

# Crea un servicio para acceder a la API de Google Slides
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=credentials)

# ID de la presentación que deseas compartir
presentation_id = '1IGjvPuGkxWFvG31ulh5ZmUJ-Z6JnDV9PV4hLQxZ2Zf0'

# Configura los permisos de acceso (lectura y edición) para el usuario
permission = {
    'type': 'user',
    'role': 'writer',  # Puedes usar 'reader' para dar solo permisos de lectura
    'emailAddress': user_email
}

# Agrega los permisos a la presentación
drive_service.permissions().create(fileId=presentation_id, body=permission).execute()

print(f'Se han dado permisos a {user_email} para leer y editar la presentación.')
