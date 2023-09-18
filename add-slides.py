import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo JSON con las credenciales de la cuenta de servicio
credentials_file = 'charladevops-9715a69aa772.json'

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
        'title': "Beneficios Tangibles de la Implementación DevOps en AWS",
        'subtitle': "Casos de estudio y ejemplos de organizaciones que han implementado DevOps en AWS.|Mejora en la velocidad de entrega, calidad de software y colaboración entre equipos.",
        'content': "La implementación exitosa de DevOps en AWS conlleva una serie de beneficios tangibles para las organizaciones. Estos beneficios incluyen una mayor velocidad de entrega de software, una reducción en la cantidad de errores y una mejora en la calidad del software implementado. La colaboración efectiva entre equipos de desarrollo y operaciones conduce a una comunicación más eficiente y una resolución más rápida de problemas. Además, la automatización de tareas repetitivas y la integración continua de pruebas mejoran la eficiencia operativa. En última instancia, DevOps no solo impulsa una mayor satisfacción del cliente al ofrecer productos y servicios de mayor calidad más rápidamente, sino que también crea un entorno de trabajo más ágil y motivador para los equipos involucrados."
    },
    #9
    {
        'title': "Resiliencia y Recuperación ante Desastres en AWS",
        'subtitle': "Diseño de arquitecturas resistentes utilizando servicios de alta disponibilidad de AWS.|Estrategias para la recuperación ante desastres y la continuidad del negocio.",
        'content': "La resiliencia y la recuperación ante desastres son componentes críticos de cualquier estrategia de DevOps en AWS. Diseñar arquitecturas resistentes a fallos es esencial para garantizar la disponibilidad continua de las aplicaciones. AWS ofrece una variedad de servicios que ayudan en este aspecto, como Amazon RDS Multi-AZ, que proporciona replicación automática de bases de datos para una alta disponibilidad, y Amazon S3, que replica automáticamente datos en múltiples ubicaciones para la recuperación de datos. Además, la implementación de estrategias de copia de seguridad y la realización de pruebas regulares de recuperación ante desastres son prácticas esenciales para mantener la continuidad del negocio y proteger los datos críticos."
    },
    #8
    {
        'title': "Seguridad en el Ciclo de Vida de DevOps en AWS",
        'subtitle': "Incorporación de prácticas de seguridad en todas las etapas del desarrollo y despliegue.|Uso de AWS Identity and Access Management (IAM) para gestionar permisos.",
        'content': "La seguridad es una consideración fundamental en cualquier implementación de DevOps. En AWS, AWS Identity and Access Management (IAM) desempeña un papel crucial al permitir la gestión precisa de permisos y accesos a los recursos de la nube. En un enfoque DevOps, es esencial incorporar prácticas de seguridad en todas las etapas del ciclo de vida de desarrollo y despliegue. Esto incluye el escaneo de vulnerabilidades de código, la autenticación de usuarios y la gestión segura de secretos y credenciales. La seguridad no es un obstáculo en DevOps, sino una parte integral que garantiza la protección de los datos y la infraestructura en todo momento."
    },
    #7
    {
        'title': "Gestión de Configuración y Automatización de Tareas con AWS Systems Manager",
        'subtitle': "Cómo gestionar configuraciones de instancias y aplicar parches en AWS con Systems Manager.|Automatización de tareas de mantenimiento y administración.",
        'content': "AWS Systems Manager es una herramienta versátil que facilita la gestión de configuraciones y la automatización de tareas en entornos de AWS. Permite la configuración y el mantenimiento centralizados de instancias de EC2, lo que es crucial para mantener la coherencia y la seguridad en la infraestructura. Además, Systems Manager ofrece capacidades avanzadas de automatización para tareas de parcheo, implementación de aplicaciones y administración de flotas de instancias. Al aprovechar Systems Manager, los equipos de DevOps pueden automatizar tareas repetitivas y mejorar la eficiencia operativa."
    },
    #6
    {
        'title': "Monitorización y Observabilidad en AWS",
        'subtitle': "Utilización de Amazon CloudWatch para monitorizar métricas, registros y eventos.|Creación de paneles de control para visualizar el rendimiento de las aplicaciones.",
        'content': "La monitorización y la observabilidad son componentes clave en la implementación exitosa de DevOps en AWS. Amazon CloudWatch es una herramienta esencial para este propósito, ya que proporciona métricas detalladas, registros y alarmas que permiten a los equipos de desarrollo y operaciones supervisar el rendimiento y la salud de sus aplicaciones y recursos de AWS. La integración de CloudWatch en tu infraestructura te permite detectar y solucionar problemas de manera proactiva, realizar un seguimiento del uso de recursos y tomar decisiones basadas en datos para mejorar la eficiencia operativa."
    },
    #5
    {
        'title': "Despliegue de Aplicaciones en Contenedores con AWS ECS",
        'subtitle': "Uso de Amazon Elastic Container Service (ECS) para desplegar aplicaciones en contenedores.|Estrategias de escalado y administración de contenedores en producción.",
        'content': "El uso de contenedores es fundamental en DevOps para garantizar la portabilidad y la eficiencia en el despliegue de aplicaciones. Amazon Elastic Container Service (ECS) es una solución de AWS que simplifica la administración y la orquestación de contenedores Docker en la nube. ECS te permite empaquetar tu aplicación en contenedores y luego desplegarla en clústeres de contenedores altamente escalables. Esto facilita la implementación y la administración de aplicaciones en una arquitectura basada en microservicios, lo que es esencial para lograr una entrega continua y una infraestructura ágil en un entorno DevOps."
    },
    #4
    {
        'title': "Entrega Continua en AWS",
        'subtitle': "Cómo establecer un flujo de trabajo de entrega continua utilizando herramientas como AWS CodePipeline.|Integración con herramientas de control de versiones y pruebas automatizadas.",
        'content': "La entrega continua es un pilar de DevOps que se centra en la automatización de la implementación y las pruebas de aplicaciones en todo su ciclo de vida. AWS ofrece un conjunto de herramientas, como AWS CodePipeline, que simplifican este proceso. Con CodePipeline, puedes construir pipelines personalizados para tu aplicación que integren pruebas automáticas, revisión de código y despliegue a producción. Esta automatización no solo acelera la entrega de software, sino que también mejora la calidad al garantizar que las pruebas se realicen de manera consistente en cada iteración."
    },
    #3
    {
        'title': "Automatización de Infraestructura con AWS CloudFormation",
        'subtitle': "Definición de infraestructura como código y automatización con CloudFormation.|Ventajas de la automatización en la creación y gestión de recursos en AWS.",
        'content': "La automatización de infraestructura es una piedra angular de DevOps, y AWS CloudFormation es una herramienta esencial en este proceso. Permite definir toda la infraestructura como código, lo que significa que puedes describir y configurar recursos de AWS en archivos de plantilla. Luego, CloudFormation se encarga de crear y gestionar esos recursos de manera consistente y reproducible. Esto no solo ahorra tiempo, sino que también reduce errores y garantiza que tu infraestructura esté alineada con los requisitos de tu aplicación, lo que es fundamental para una implementación exitosa de DevOps."
    },
    #2
    {
        'title': "Cultura y Colaboración en DevOps",
        'subtitle': "Cómo fomentar la colaboración entre equipos de desarrollo y operaciones.|Importancia de la comunicación constante y la resolución colaborativa de problemas",
        'content': "Es esencial para entender cómo DevOps va más allá de las herramientas y se enfoca en la transformación cultural en las organizaciones. En DevOps, se promueve una cultura de colaboración y comunicación abierta entre los equipos de desarrollo, operaciones y otras partes interesadas. Esto implica un cambio de mentalidad en el que se prioriza la cooperación sobre la competencia, y se trabaja juntos hacia objetivos comunes. La colaboración efectiva en DevOps conlleva la eliminación de silos y la creación de equipos multidisciplinarios que asumen la responsabilidad compartida de todo el ciclo de vida de desarrollo y entrega de aplicaciones. Al adoptar esta cultura de colaboración, las organizaciones pueden acelerar la entrega de software, reducir errores y mejorar la calidad, lo que en última instancia conduce a una mayor satisfacción del cliente y a un entorno de trabajo más eficiente."
    },
    #1
    {
        'title': "Introducción a DevOps y AWS....",
        'subtitle': "Visión general de los principios y valores de DevOps.|Breve repaso de los servicios y soluciones de AWS relevantes para DevOps.",
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
