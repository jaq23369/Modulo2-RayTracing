# Lab 5: Spheres, Materials & Phong Shading

## Descripción del Laboratorio
Este Laboratorio implementa un ray tracer básico en Python utilizando Pygame para renderizado y NumPy para cálculos matemáticos. El foco principal es el Lab 5, que incluye la intersección de rayos con esferas, el modelo de iluminación Phong (difusa, especular y ambiental), materiales, sombras y una figura compuesta por múltiples esferas (cara sonriente).

## Requisitos del Lab 5
- **Intersección de Rayos con Esferas**: Implementar el algoritmo de intersección geométrica para detectar colisiones entre rayos y esferas.
- **Modelo de Iluminación Phong**: Incluir componentes difusa, especular y ambiental para un sombreado realista.
- **Materiales**: Definir materiales con propiedades como color difuso, especular, coeficientes de reflexión y exponente especular.

## Archivos del Proyecto

### RayTracer.py
- **Función**: Archivo principal que configura la escena, define la cámara, luces, materiales y esferas. Crea la cara sonriente (cabeza, ojos, boca) y exporta la imagen a BMP.
- **Detalles**: Incluye la configuración de la ventana Pygame, el renderizado de la escena y la exportación de la imagen.

### gl.py
- **Función**: Contiene la clase Renderer, responsable del renderizado por píxel. Implementa `glRender` para trazar rayos desde la cámara y `glCastRay` para encontrar intersecciones con objetos, incluyendo z-buffer para profundidad.
- **Detalles**: Maneja el viewport, la proyección de rayos y la integración de iluminación y sombras.

### figures.py
- **Función**: Define la clase Sphere con el método `ray_intersect`, que calcula la intersección de un rayo con la esfera y devuelve un objeto Intercept con punto de impacto, normal y distancia.
- **Detalles**: Soporta transformación de coordenadas para posicionar y escalar esferas.

### material.py
- **Función**: Clase Material que define propiedades como color difuso, especular, coeficientes de reflexión y exponente especular. Incluye `GetSurfaceColor` para calcular el color final usando el modelo Phong.
- **Detalles**: Integra iluminación difusa (N·L), especular ((V·R)^spec * ks) y ambiental.

### lights.py
- **Función**: Define clases para luces: DirectionalLight (con soporte para especular) y AmbientLight.
- **Detalles**: Calcula la contribución de luz en el sombreado, incluyendo sombras para luces direccionales.

### intercept.py
- **Función**: Estructura de datos para almacenar información de intersección: punto de impacto, normal, distancia y objeto intersectado.
- **Detalles**: Usada para pasar datos entre el ray casting y el cálculo de iluminación.

### camera.py
- **Función**: Clase Camera para manejar la vista 3D, incluyendo matrices de transformación y proyección.
- **Detalles**: Configura la posición y orientación de la cámara para el renderizado.

### MathLib.py
- **Función**: Biblioteca de funciones matemáticas para vectores, matrices y operaciones como normalización, producto punto y vector de reflexión.
- **Detalles**: Incluye `reflectVector` para cálculos especulares.

### BMP_Writer.py
- **Función**: Utilidad para escribir imágenes en formato BMP.
- **Detalles**: Exporta el buffer de píxeles renderizado a un archivo BMP.

### BMPTexture.py
- **Función**: Maneja texturas BMP para aplicar a superficies (opcional en este lab).
- **Detalles**: No utilizado en la implementación actual, pero disponible para extensiones futuras.

### model.py
- **Función**: Clase para cargar modelos 3D (opcional).
- **Detalles**: No utilizado en este lab, enfocado en esferas.

## Dependencias
- Python 3.10+
- Pygame
- NumPy

## Instalación y Ejecución
1. Clona el repositorio:
- git clone https://github.com/jaq23369/Modulo2-RayTracing.git
- cd Modulo2-RayTracing
- git checkout lab5

2. Crea el entorno virtual:
- python -m venv venv
- venv\Scripts\activate  # En Windows

3. Instala las dependencias:
- pip install pygame
- pip install numpy

4. Ejecuta el programa:
- python RayTracer.py

# Imagenen de lo creado
## Cara sonriente con luz ambiental y 1 luz direccional [-1, -1, -1]
<img width="955" height="988" alt="Image" src="https://github.com/user-attachments/assets/996e226e-5826-4408-bea1-393226f56d73" />

## Cara sonriente con luz ambiental y 2 luces direccionales, una es la de antes [-1, -1, -1] y la otra es [0, 0, -1]
<img width="1315" height="988" alt="Image" src="https://github.com/user-attachments/assets/4adb510e-d509-4e13-9ba2-bc02dc382016" />

# Hecho por:
- Joel Antonio Jaquez López #23369

