from googleapiclient.discovery import build
from google.oauth2 import service_account

# Ruta al archivo de credenciales
credentials_file = '/home/carlos/Trabajo/Charla/charla-utn/charladevops-9715a69aa772.json'

# Crea las credenciales desde el archivo JSON
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=['https://www.googleapis.com/auth/presentations'])

# ID de la presentación que deseas obtener
presentation_id = '1IGjvPuGkxWFvG31ulh5ZmUJ-Z6JnDV9PV4hLQxZ2Zf0'

# Crea el servicio de Google Slides
slides_service = build('slides', 'v1', credentials=credentials)

try:
    # Obtiene la información de la presentación
    presentation = slides_service.presentations().get(presentationId=presentation_id).execute()

    # Imprime la información de la presentación
    print(f'Título de la presentación: {presentation["title"]}')
    print(f'Número de diapositivas: {len(presentation["slides"])}')

except Exception as e:
    print(f'Error al obtener información de la presentación: {str(e)}')
