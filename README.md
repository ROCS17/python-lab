# Python Lab

Este proyecto es un entorno de laboratorio en Python diseñado para ejecutar pruebas y experimentos de código.

## Estructura del Proyecto
- `.venv` - Entorno virtual en la cual contiene las dependencias en caso de ser necesario para los ejercicios.
- `src/` - Contiene los scripts principales con la lógica del laboratorio:
  - `codewars/` - Ejercicios de Codewars organizados por número de kata.
  - `leetcode/` - Soluciones de problemas de LeetCode.
  - `oop/` - Ejemplos y ejercicios de Programación Orientada a Objetos.
  - `solid/` - Implementaciones de los principios SOLID en Python.
- `.gitignore` - Archivo en la cual contiene los archivos o tipso de archivos que no se quiere hacer seguimiento.
- `README.md` - Documento que describe la información general del proyecto, su estructura, instalación y uso.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/RogerCS17/python-lab.git
   cd python-lab
   ```
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv .venv        # En Windows: python -m venv . venv
   source venv/bin/activate     # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias (opcional):
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecutar algún ejercicio, por ejemplo:
```bash
cd src/codewars/
python3 kata001.py              # En Windows python kata001.py
```