# Beer Orders Project

Este proyecto es una aplicación simple para gestionar pedidos de cervezas. Implementdo con clean architecture y está construido con FastAPI para el backend y Next.js para la interfaz de usuario.

## Requisitos

### Backend

- Python 3.12 o superior
- Uvicorn para ejecutar el servidor ASGI
- `pytest` para pruebas unitarias

### Frontend

- Node.js 18 o superior
- NPM para las dependencias con Next.js
- Tailwind CSS para estilos

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

### Pruebas unitarias

PYTHONPATH=$(pwd) pytest

