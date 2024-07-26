# Beer Orders Project

Este proyecto es una aplicación simple para gestionar pedidos de cervezas. Implementdo con clean architecture y está construido con FastAPI para el backend y Next.js para la interfaz de usuario.

## Requisitos

### Backend

1- Python 3.12 o superior
2- Uvicorn para ejecutar el servidor ASGI
3- `pytest` para pruebas unitarias

## Instalación y Ejecución

### Backend

1. **Clonar el Repositorio**

Repo: https://github.com/Cornielle/beer-project.git

### Entorno virtual

python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate 

### Instalar Dependencias

pip install -r requirements.txt

### Correr el proyecto

uvicorn app.main:app --reload

### Endpoints

"api/v1/order/status" Para visualizar el estatus de la orden
"api/v1/order/add-round" Para agregar una "ronda" y pedir una o varias cervezas enviando desde el body lo siguiente:

Ejemplo:

[{
	"name":"Quilmes",
	"quantity":5
}]

NOTA: En caso de pedir cervezas que no estan dentro del stock, el backend deloverá un exception

### Pruebas unitarias 

PYTHONPATH=$(pwd) pytest

### Frontend
    IMPORTANTE: renombrar el archivo .env.example por .env y quitar el signo "#" para habilitar el dominio:
```NEXT_PUBLIC_BACKEND_BEER_STATUS_DOMAIN=http://localhost:8000/api/v1/order/status```
    Permite conectar el backend con el frontend

1 - Posicionarse en la carpeta de Frontend: cd frontend (o cd .. y luego cd frontend si estuviste en la carpeta "backend")
2 - Node.js 18 o superior
3 - Correr npm install y luego npm run dev para poner a funcionar el proyecto
