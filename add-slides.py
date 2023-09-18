import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo JSON con las credenciales de la cuenta de servicio
credentials_file = '/home/carlos/Trabajo/Charla/charla-utn/charladevops-9715a69aa772.json'

# Crea un servicio para acceder a la API de Google Slides
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=['https://www.googleapis.com/auth/presentations'])
slides_service = build('slides', 'v1', credentials=credentials)

# ID de la presentación existente que contiene la diapositiva modelo
presentation_id = '1IGjvPuGkxWFvG31ulh5ZmUJ-Z6JnDV9PV4hLQxZ2Zf0'

# ID de la diapositiva modelo que deseas duplicar
model_slide_id = 'SLIDES_API1042560283_0'

# Define el contenido de las 15 nuevas diapositivas en orden inverso
slides_content = [
    #10
    {
        'title': "Desafíos Comunes y Soluciones",
        'subtitle': "Enumeración de desafíos comunes y cómo abordarlos.",
        'content': ""
    },
    #9
    {
        'title': "Caso de Estudio - Implementación Exitosa",
        'subtitle': "Ejemplo real de una empresa que implementó DevOps en AWS con éxito.",
        'content': ""
    },
    #8
    {
        'title': "Entrega Continua en AWS",
        'subtitle': "Descripción de cómo lograr la entrega continua en la nube de AWS.",
        'content': ""
    },
    #7
    {
        'title': "Automatización de la Infraestructura en AWS",
        'subtitle': "Importancia de la automatización y herramientas disponibles en AWS.",
        'content': ""
    },
    #6
    {
        'title': "Prácticas Ágiles en DevOps",
        'subtitle': "Explicación de cómo las prácticas ágiles se integran en DevOps.",
        'content': ""
    },
    #5
    {
        'title': "AWS como Plataforma para DevOps",
        'subtitle': "Ventajas de AWS en el contexto de DevOps.",
        'content': ""
    },
    #4
    {
        'title': "Beneficios de DevOps",
        'subtitle': "Enumeración de los beneficios, como la mejora de la colaboración, la entrega más rápida y la reducción de errores.",
        'content': ""
    },
    #3
    {
        'title': "¿Qué es DevOps?",
        'subtitle': "Definición de DevOps y sus principios básicos.",
        'content': ""
    },
    #2
    {
        'title': "Cultura y Colaboración en DevOps",
        'subtitle': "Cómo fomentar la colaboración entre equipos de desarrollo y operaciones. | Importancia de la comunicación constante y la resolución colaborativa de problemas",
        'content': ""
    },
    #1
    {
        'title': "Introducción a DevOps y AWS",
        'subtitle': " Visión general de los principios y valores de DevOps. | Breve repaso de los servicios y soluciones de AWS relevantes para DevOps.",
        'content': "En esta sección introductoria, exploraremos los fundamentos de DevOps y su integración con el ecosistema de Amazon Web Services (AWS). Comprenderemos los principios y valores clave de DevOps, que promueven la colaboración, la automatización y la entrega continua. Además, se presentarán de manera concisa los servicios y soluciones de AWS que juegan un papel fundamental en la implementación exitosa de DevOps en la nube, estableciendo así la base para el resto de la charla."
    },
]


# Recorre las diapositivas existentes y duplica la diapositiva modelo
for index, slide_data in enumerate(slides_content, start=1):
    slide_title = slide_data['title']
    slide_subtitle = slide_data['subtitle']
    slide_content = slide_data['content']

    # Duplica la diapositiva modelo
    requests = [
        {
            'duplicateObject': {
                'objectId': model_slide_id,
            }
        }
    ]
    duplicate_slide = slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': requests}).execute()
    new_slide_id = duplicate_slide['replies'][0]['duplicateObject']['objectId']

    # Reemplaza el título de la nueva diapositiva
    requests = [
        {
            'replaceAllText': {
                'replaceText': slide_title,
                'pageObjectIds': [new_slide_id],  # ID de la nueva diapositiva duplicada
                'containsText': {
                    'text': '{{TITULO_DIAPPOSITIVA}}',  # Texto de marcador de posición
                    'matchCase': True,
                }
            }
        }
    ]
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': requests}).execute()

    # Reemplaza el subtítulo de la nueva diapositiva
    requests = [
        {
            'replaceAllText': {
                'replaceText': slide_subtitle,
                'pageObjectIds': [new_slide_id],  # ID de la nueva diapositiva duplicada
                'containsText': {
                    'text': '{{SUBTITULO_DIAPPOSITIVA}}',  # Texto de marcador de posición
                    'matchCase': True,
                }
            }
        }
    ]
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': requests}).execute()

    # Reemplaza el contenido de la nueva diapositiva
    requests = [
        {
            'replaceAllText': {
                'replaceText': slide_content,
                'pageObjectIds': [new_slide_id],  # ID de la nueva diapositiva duplicada
                'containsText': {
                    'text': '{{CONTENIDO_DIAPPOSITIVA}}',  # Texto de marcador de posición
                    'matchCase': True,
                }
            }
        }
    ]
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': requests}).execute()

print(f'Se ha actualizado la presentación con las 15 diapositivas en la presentación ID: {presentation_id}')
