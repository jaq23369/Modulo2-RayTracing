# Ray Tracing Lab 6

Este laboratorio implementa un motor de ray tracing básico en Python utilizando Pygame para renderizar escenas 3D con esferas de diferentes tipos de materiales.

## Descripción

El programa renderiza una escena con 6 esferas: 2 opacas, 2 reflectivas y 2 transparentes. Incluye un mapa de entorno (environment map) cargado desde una textura BMP para simular reflexiones y refracciones realistas.

## Características

- **Renderizado de esferas**: Soporte para materiales opacos, reflectivos y transparentes con índices de refracción (IOR).
- **Mapa de entorno**: Textura BMP usada como fondo y para reflexiones/refracciones.
- **Iluminación**: Luces ambientales y direccionales con sombras.
- **Texturas**: Aplicadas a algunos materiales para mayor detalle.
- **Salida**: Genera un archivo BMP con la imagen renderizada.

## Requisitos

- Python 3.x
- Pygame
- NumPy

## Instalación y Ejecucion

1. Clona el repositorio: git clone https://github.com/jaq23369/Modulo2-RayTracing.git y accede al modulo cd Modulo2-RayTracing/Lab6
2. Instala las dependencias: pip install pygame numpy
3. Ejecuta el script principal: python RayTracer.py

# Imagen del FrameBuffer final:
<img width="636" height="672" alt="Image" src="https://github.com/user-attachments/assets/90c578dc-e93a-43f2-b54e-bbaa9d8f719b" />

La escena incluye:
- Esfera opaca roja (fuego).
- Esfera opaca azul (océano).
- Esfera reflectiva negra (metal).
- Esfera reflectiva roja (tela).
- Esfera transparente (diamante, IOR=2.0).
- Esfera transparente (agua, IOR=1.33).

# Hecho por:
- Joel Antonio Jaquez López #23369
