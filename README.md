# Automatización de Pruebas con Selenium y Python

Este proyecto es una solución de automatización Web del flujo de cambio de contraseña para usuarios LDAP desde el ADManager utilizando Selenium y Python.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python (versión >= 3.11.6)
- Selenium WebDriver (versión >= 4.16.0)
- Pytest (version >= 7.4.4)
- Navegador Chrome

## Instalación

1. Clona el repositorio en tu máquina local:

    ```
    git clone https://github.com/l2ul3en/reset_win.git
    ```

2. Ingresa al directorio:

    ```
    cd .\reset_win
    ```

3. Crea un entorno virtual:

    ```
    python -m venv .\.venv
    ```

4. Activa el entorno virtual:

    ```
    .\.venv\Scripts\Activate.ps1
    ```

5. Instala las siguientes dependencias:

    ```
    pip install -r requirements.txt
    ```

6. Configura las siguientes variables de entorno a nivel de usuario en el sistema:

    `W_URL` = url_Admanager
    `W_USER` = your_user
    `W_PASS` = your_password

7. Asegurate de crear el archivo win_users.txt. Este se usará para enviar los usuarios y contraseñas.

El formato admitido por el archivo es el siguiente:
```
usuario;contraseña
usuario
```
Donde se puede enviar usuario y contraseña separado por ";" o solo usuario

8. Asegurate de crear el archivo config.toml. Este se usará para configurar el nombre del encargado para generar reporte en formato csv

Ejemplo
```
encargado = "Pepito Perez"
```

## Ejecución

1. Asegurate de tener como aplicación predeterminada el uso del navegador Chrome.

2. Antes de ejecutar las pruebas, asegurate de cerrar todos los navegadores abiertos de Chrome.

3. Abre una consola cmd/powershell/git-bash y navega hasta el directorio donde descargaste el proyecto.

    ```
    cd label:\Path\to\project\reset_win
    ```

4. Activa en entorno virtual:

    ```
    .\activate_env.ps1
    ```

5. Ejecuta el flujo utilizando el siguiente comando:

    ```
    python .\play.py
    ```

6. Verifica el reporte generado:

`procesado.csv`