# Guía de instalación

## Requisitos previos

Antes de comenzar, asegurate de tener instalado:

- Python 3.12+ (recomendado 3.13)
- pip (gestor de paquetes de Python)
- pyenv (opcional, para manejo de versiones)

---

## Instalación de Python (si no lo tenés)

Se recomienda usar pyenv:

```bash
pyenv install 3.13.12
pyenv local 3.13.12
```

## Instalación de dependencias

### Entorno virtual

```bash
Creacion : python -m venv venv

# Activar entorno
# En Linux/macOS:
source venv/bin/activate
# En Windows:
source venv/scripts/activate

#Desactivar entorno:
deactivate
```

### Instalar todas las dependencias con el siguiente comando :

- `pip install -r requirements.txt` : installa todos los entornos que son requeridos, los que estan escritos en requirements.tx

# Guia para instalacion individual

### Se recomienda generar un entorno virtual -> (venv) Activado

## Jupyter Notebook

```bash
#instalar Jupyter
$ pip install notebook

#Iniciar servidor de Jupyter
$ jupyter notebook

# Finalizar servidor (en consola
$ ctrl + c

# Ver versión instalada
$ pip show jupyter
```
