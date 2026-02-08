# Microscopio-Pro
Aplicación de medición en tiempo real basada en **Python + OpenCV**, diseñada para trabajar con microscopios USB UVC (como los basados en eMPIA) en Linux (probado en Debian 13).

## Instalación

1) Instalar dependencias

~~~
sudo apt install python3-opencv python3-numpy v4l-utils
~~~

2) Bajar el script python a una carpeta
3) Editar el principio del script para ajustar dispositivo de video */dev/videoX* y resolución
~~~
# ================= CONFIG =================
VIDEO_DEVICE = 2
WIDTH, HEIGHT = 1920, 1080
~~~

## Uso

Abrir un terminal en la carpeta y ejecutar

~~~
python3 microscopio.py
~~~

![](captura_20260208_211035.png)

* [Documentación](Microscopio_PRO_Documentacion.md)
* [Script Python3](microscopio.py)
