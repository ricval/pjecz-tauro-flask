# pjecz-tauro-flask

Sistema de Turnos

## Requerimientos

Los requerimientos son

- Python 3.11
- PostgreSQL 15
- Redis

## Instalación

Crear el entorno virtual

```bash
python3.11 -m venv .venv
```

Ingresar al entorno virtual

```bash
source venv/bin/activate
```

Actualizar el gestor de paquetes **pip**

```bash
pip install --upgrade pip
```

Instalar el paquete **wheel** para compilar las dependencias

```bash
pip install wheel
```

Instalar **poetry** en el entorno virtual si no lo tiene desde el sistema operativo

```bash
pip install poetry==1.8.5
```

Configurar **poetry** para que use el entorno virtual dentro del proyecto

```bash
poetry config virtualenvs.in-project true
```

Instalar las dependencias por medio de **poetry**

```bash
poetry install
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto con las variables, establecer sus propios SECRET_KEY, DB_PASS, CLOUD_STORAGE_DEPOSITO y SALT.

```bash
# Flask, para SECRET_KEY use openssl rand -hex 24
FLASK_APP=tauro.app
FLASK_DEBUG=1
SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Base de datos
DB_NAME=pjecz_tauro
DB_PASS=XXXXXXXXXXXXXXXX
DB_USER=adminpjecztauro
DB_HOST=127.0.0.1
DB_PORT=5432
SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://adminpjecztauro:XXXXXXXXXXXXXXXX@127.0.0.1:5432/pjecz_tauro"

# Host se usa por CORS en la API
HOST=http://127.0.0.1:5000

# Salt sirve para cifrar el ID con HashID, debe ser igual en la API
SALT=XXXXXXXXXXXXXXXX

# Huso horario
TZ=America/Mexico_City

# Límite de registros mostrados en el listado de turno
LIMITE_DE_TURNOS_LISTADOS=20

# Si esta en PRODUCTION se evita reiniciar la base de datos
DEPLOYMENT_ENVIRONMENT=develop
```

Crear un archivo `.bashrc` que se ejecute al iniciar la terminal

```bash
if [ -f ~/.bashrc ]
then
    . ~/.bashrc
fi

if command -v figlet &> /dev/null
then
    figlet Tauro Flask
else
    echo "== Tauro Flask"
fi
echo

if [ -f .env ]
then
    echo "-- Variables de entorno"
    # export $(grep -v '^#' .env | xargs)
    source .env && export $(sed '/^#/d' .env | cut -d= -f1)
    echo "   DB_HOST: ${DB_HOST}"
    echo "   DB_PORT: ${DB_PORT}"
    echo "   DB_NAME: ${DB_NAME}"
    echo "   DB_USER: ${DB_USER}"
    echo "   DB_PASS: ${DB_PASS}"
    echo "   DEPLOYMENT_ENVIRONMENT: ${DEPLOYMENT_ENVIRONMENT}"
    echo "   FLASK_APP: ${FLASK_APP}"
    echo "   HOST: ${HOST}"
    echo "   SALT: ${SALT}"
    echo "   SECRET_KEY: ${SECRET_KEY}"
    echo "   SQLALCHEMY_DATABASE_URI: ${SQLALCHEMY_DATABASE_URI}"
    echo
    export PGHOST=$DB_HOST
    export PGPORT=$DB_PORT
    export PGDATABASE=$DB_NAME
    export PGUSER=$DB_USER
    export PGPASSWORD=$DB_PASS
fi

if [ -d .venv ]
then
    echo "-- Python Virtual Environment"
    source .venv/bin/activate
    echo "   $(python3 --version)"
    export PYTHONPATH=$(pwd)
    echo "   PYTHONPATH: ${PYTHONPATH}"
    echo
    echo "-- Poetry"
    export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
    echo "   $(poetry --version)"
    echo
    if [ -f cli/app.py ]
    then
        echo "-- Ejecutar el CLI"
        alias cli="python3 ${PWD}/cli/app.py"
        echo "   cli --help"
        echo
    fi
    echo "-- Flask 127.0.0.1:5000"
    alias arrancar="flask run --port=5000"
    echo "   arrancar = flask run --port=5000"
    echo
fi
```

## Arrancar

Antes de usar el CLI o de arrancar el servidor de **Flask** debe cargar las variables de entorno y el entorno virtual.

```bash
source .bashrc
```

Para lanzar el front-end Flask, abrir una terminal, cargar `source .bashrc` y ejecutar

```bash
arrancar
```
