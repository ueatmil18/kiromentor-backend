# KiroMentor Backend

API en Flask para explicar código automáticamente. Parte del proyecto KiroMentor para el hackathon "Code with Kiro".

## Endpoints
- `GET /` → Bienvenida
- `POST /explicar` → Explica el código recibido en JSON

## Deploy
1. Subir a GitHub
2. Crear Web Service en Render.com
3. Usar `gunicorn app:app` como comando de inicio
