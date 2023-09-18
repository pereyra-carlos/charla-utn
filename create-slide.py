import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo JSON con las credenciales de la cuenta de servicio
credentials_file = 'charladevops-9715a69aa772.json'

# Crea un servicio para acceder a la API de Google Slides
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=['https://www.googleapis.com/auth/presentations'])
slides_service = build('slides', 'v1', credentials=credentials)

# Crea una nueva presentación en blanco
presentation = slides_service.presentations().create().execute()

# ID de la presentación recién creada
presentation_id = presentation['presentationId']

# Crea una página en blanco
requests = [
    {
        'createSlide': {
            'slideLayoutReference': {
                'predefinedLayout': 'BLANK'
            }
        }
    }
]

slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': requests}).execute()

print(f'Presentación creada con éxito. ID: {presentation_id}')
