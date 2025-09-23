# Lab 7: Planes, Disks, Triangles, and Cubes

## Descripción
Este laboratorio implementa un ray tracer básico en Python para renderizar una escena tridimensional de una habitación. Incluye diversas formas geométricas (planos, discos, triángulos, AABBs), sistemas de iluminación (luz ambiental y spotlight), materiales con propiedades de reflexión y transparencia, y texturas BMP para mayor realismo. La escena final muestra una habitación con paredes, piso, techo, un triángulo central, dos cubos (AABBs) a los lados y un disco reflectante.

## Características
- **Formas geométricas**:
  - Plano (Plane): Superficies infinitas.
  - Disco (Disk): Planos con radio limitado.
  - Triángulo (Triangle): Usando el algoritmo de Möller-Trumbore para intersecciones.
  - AABB (Axis-Aligned Bounding Box): Cubos alineados con los ejes.
- **Iluminación**:
  - Luz ambiental (AmbientLight): Iluminación base.
  - Spotlight (SpotLight): Luz direccional con atenuación.
- **Materiales**:
  - Opacos, reflectivos y transparentes con propiedades de Phong shading.
- **Texturas y Entorno**:
  - Texturas BMP para materiales.
  - Mapa de entorno (envMap) para reflejos ambientales.
- **Renderizado**:
  - Resolución: 512x256 píxeles.
  - Recursión para reflejos y transparencias.

## Requisitos
- Python 3.x
- NumPy
- Pygame

## Instalación
1. Asegúrate de tener Python 3.x instalado.
2. Instala las dependencias:
   ```
   pip install numpy pygame
   ```

## Uso
1. Navega al directorio del proyecto (Lab7).
2. Ejecuta el script principal:
   ```
   python RayTracer.py
   ```
3. El renderizado se guardará como una imagen BMP en el directorio actual.

## Estructura del Laboratorio
- `RayTracer.py`: Script principal que define la escena y ejecuta el renderizado.
- `figures.py`: Clases para las formas geométricas y sus métodos de intersección con rayos.
- `lights.py`: Clases para los tipos de luces.
- `material.py`: Definiciones de materiales.
- `gl.py`: Motor de renderizado con funciones de casting de rayos y recursión.
- `BMPTexture.py`: Manejo de texturas BMP.
- `camera.py`, `MathLib.py`, `model.py`: Utilidades adicionales para cámara, matemáticas y modelos.
- `BMP_Writer.py`: Escritura de archivos BMP.

## Imagen del resultado obtenido
<img width="1917" height="993" alt="Image" src="https://github.com/user-attachments/assets/dc71b863-2672-4df9-8a35-aa25a660a5b8" />

## Hecho por:
- Joel Antonio Jaquez Lopez  #23369
