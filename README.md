# DS-BOT

## Descripción

Este proyecto tiene como objetivo desarrollar un bot de Discord que, en el futuro, integrará inteligencia artificial para reconocer comandos de voz y reproducir música según las solicitudes de los usuarios. Actualmente, el bot está en una fase inicial donde puede reproducir música a partir de enlaces de YouTube proporcionados en el chat.

## Características

- **Reproducción de música desde YouTube:** El bot permite a los usuarios enviar enlaces de YouTube para reproducir música en canales de voz.
- **Comando `,play` y `,p`:** Puedes utilizar estos comandos para pedirle al bot que busque y reproduzca música desde YouTube.
- **Comando `,stop`:** Detiene la música y desconecta el bot del canal de voz.

## Tecnologías Utilizadas

- **Python:** Lenguaje de programación utilizado para desarrollar el bot.
- **Discord.py:** Librería para interactuar con la API de Discord.
- **yt-dlp:** Módulo para descargar y transmitir audio desde YouTube.
- **FFmpeg:** Herramienta para la manipulación de audio y video (utilizada para reproducir audio en Discord).

## Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/parkerbfb/DS-BOT.git

2. **Navegar al Directorio del Proyecto**
   
   ```bash    
   cd DS-BOT

4. **Instalar las Dependencias:**
    Asegúrate de tener Python instalado en tu sistema. Luego, instala las dependencias necesarias utilizando pip:
   
    ```bash
    pip install -r requirements.txt

4. **Configurar el Bot:**
    Renombra config.example.py a config.py.
    Abre config.py y completa los campos necesarios, como el token de tu bot.

5. **Ejecutar el Bot:**
    En Windows, abre una terminal de PowerShell o CMD y ejecuta:
       
    ```bash
    python bot.py







