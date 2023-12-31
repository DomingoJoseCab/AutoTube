# AutoTube

Bienvenidos a AutoTube, una herramienta creada por Domingo Caballero para generar vídeos automáticos de productos de Amazon para YouTube.

## Cómo Usarlo

Para utilizar AutoTube, sigue estos pasos:

1. **Instalar Dependencias**:
   - Asegúrate de tener Python instalado en tu sistema.
   - Clona o descarga este repositorio en tu máquina local.
   - Abre una terminal y navega hasta la carpeta del proyecto.
   - Ejecuta `pip install -r requirements.txt` para instalar todas las dependencias necesarias.

2. **Configuración del Archivo `args.json` siguiendo el patron de `args_example.json`**:
   - Encontrarás un archivo llamado `args.json` en el directorio principal.
   - Abre este archivo con un editor de texto.
   - Configura los siguientes parámetros:
     - `"OPENAI_API_KEY"`: Coloca aquí tu key de la API de OPENAI (CHATGPT4 Y DALL-E)
     - `"LOVOAI_API_KEY"`: Coloca aquí tu key de la API de LOVOAI (voz con IA)
     - `"video_name"`: Coloca aquí el nombre del producto el cual estas haciendo el video.
     - `"ASIN_TOPx"`: Ingresa los ASIN relevantes para tu video.

3. **Ejecutar AutoTube**:
   - Una vez configurado el `args.json`, ejecuta `main.py` desde tu terminal con el comando `python main.py`.
   - El programa procesará la información según lo configurado y realizará las acciones programadas.

Si tienes alguna duda o necesitas ayuda adicional, no dudes en contactarme.

---

**Nota**: Asegúrate de seguir estos pasos cuidadosamente para el correcto funcionamiento de AutoTube.

## Licencia
Este proyecto es de mi autoría y retengo todos los derechos sobre él. Sin embargo, permito y animo a otros a usar y compartir AutoTube bajo las siguientes condiciones:

- **Distribución**: Puedes distribuir AutoTube libremente, siempre que enlaces y promociones mi canal de YouTube (https://www.youtube.com/@emprendedomingo?=sub_confirmation=1).
- **Créditos**: Al compartir o distribuir AutoTube, debes darme crédito y enlazar a mi canal de YouTube.
- **Mismas Condiciones**: Si alteras, transformas o creas a partir de AutoTube, debes distribuir tus contribuciones bajo la misma licencia que esta original.

## Apoyo
Si te gusta AutoTube y quieres apoyar mi trabajo, considera [suscribirte a mi canal de YouTube](https://www.youtube.com/@emprendedomingo?=sub_confirmation=1) y compartirlo con otros. Tu apoyo me ayuda a continuar desarrollando este y otros proyectos.

## Contacto
Si tienes alguna pregunta, comentario o sugerencia, no dudes en contactarme a través de X (Twitter) como @emprendedomingo (https://twitter.com/emprendedomingo).

---

¡Gracias por usar y apoyar AutoTube!
