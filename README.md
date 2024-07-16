<!--- cSpell:locale es --->

# Guía de Python para la captura de imágenes

## Requisitos

Necesitamos el software base para nuestros experimentos.

En una terminal, ejecutar los siguientes comandos:

```
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
pip3 install opencv-python
```

## OpenCV

Abrir una cámara:

```
cam = open()
cam = VideoCapture()
cam = isOpened()
```

Capturar:

```
valid, image = cam.read()
valid = cam.grab()
valid = cam.retrieve(image)
imwrite("MyImage.png", image)
```

Mostrar en ventana:

```
imshow("MyWindow", image)
destroyWindow("MyWindow")
```

Liberar el recurso:

```
cam.release()
```

## Resolución de problemas

### Si por error se cierra la ventana y la terminal se queda congelada:

Abrir otra terminal, identificar el proceso y detenerlo:

```
ps a
kill <pid>
```

## Practica

### Ejercicio 1

Crear un script que tome una única foto y la guarde en la carpeta local.

> pueden encontrar una solución a esta practica en `src/single-capture.py`

### Ejercicio 2

Modificar el script anterior para que prepare la cámara por unos segundos antes de tomar una foto.

Para este ejercicio queremos leer varios frames antes de guardar una captura final, de esta forma la imagen sera mucho mas estable.

### Ejercicio 3

Crear un programa que capture video constante de la cámara.

> pueden encontrar una solución a esta practica en `src/video.py`

### Ejercicio 4

Crear un programa que aplique alguna transformación a la imagen, por ejemplo voltear en espejo la captura.
