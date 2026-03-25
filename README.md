# Kirara Launcher

Launcher, asistente y diccionario de japo que usa la api de jisho.

![kirara_Icon](https://github.com/Bunkai9448/kirara_launcher/blob/main/kirara_Icon.png)

## Uso

Abre la terminal y ejecuta los comandos que se indican a continuación (Puedes copiar y pegar):  
```
# Permite permisos de ejecucion a los archivos (Solo hace falta la primera vez)
chmod +x ../kirara_launcher ./kirara.desktop kirara_launcher/*.py
```

Tienes dos opciones para ejecutarlo:
- Abre la terminal y ejecuta el comando `python3 kirara_main.py`
- O simplemente clicka dos veces sobre el archivo `kirara.desktop`  

Para usar el diccionario: simplemente introduce la palabra que quieras buscar y pulsa la tecla "enter".   
Para iniciar la radio usa: `!` y pulsa la tecla "enter".  
Para detener la radio usa: `?` y pulsa la tecla "enter".  
Cualquier carácter adicional después de `!` o `?` se ignora.  

## FAQ

El proyecto esta programado en python3 y usa la libreria pyqt5.  
Para usar la radio se requiere ffplay, que forma parte del paquete [ffmpeg](https://ffmpeg.org/).

- Includes a shell script to use VPN, It's made with AI, in case the radio has geo-lock. Due to the nature of the script and the perms required it has to be launched separately.

## About

Created by Bunkai
        &
Powered by the Jisho API

