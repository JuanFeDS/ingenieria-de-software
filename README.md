# 🛠️ Ingeniería de Software

Repositorio de estudio de las bases de ingeniería de software con Python: herramientas de trabajo, programación orientada a objetos, principios SOLID, testing y backend.

Consolida varios repositorios de aprendizaje que tenía por separado. Cada uno conserva su historial de commits.

## Estructura

🌱 [**01. Fundamentos**](./01.Fundamentos/): conectar Git con GitHub, configurar WSL y una introducción a la POO

🧱 [**02. POO**](./02.POO/): clases, herencia, herencia múltiple, MRO, polimorfismo y ejercicios

📐 [**03. SOLID**](./03.SOLID/): responsabilidad única y abierto/cerrado con código *before/after* sobre un procesador de pagos (Stripe, Pydantic y logging)

🧪 [**04. Testing**](./04.Testing/): pruebas unitarias con `unittest`, asserts y suites, sobre una calculadora y una cuenta bancaria

🌐 [**05. Backend**](./05.Backend/)
- [FastAPI](./05.Backend/FastAPI/): rutas, parámetros, CORS, autenticación con JWT y un ejemplo de despliegue
- [Firebase](./05.Backend/Firebase/): CRUD sobre Firestore y una API con FastAPI

## Notas

- Los despliegues de `05.Backend` se hicieron en Deta, que cerró en 2024; el código sirve como referencia, pero hay que desplegarlo en otro servicio.
- Las variables de entorno van en un `.env` (ver `05.Backend/FastAPI/authentication/.env.example`), que no se versiona.
