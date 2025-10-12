# Proyecto2: Ray Tracer 

## Descripción
Motor de Ray Tracing desde cero que renderiza una escena compleja con multiples figuras geométricas, ademas de materiales avanzados (reflectivos, transparentes, con texturas), múltiples fuentes de luz y un sistema de reflexiones/refracciones realistas.

## Objetivo:
Crear una escena artística y técnicamente desafiante que demuestre el dominio de algoritmos de ray tracing, geometría computacional y física de la luz.


## Características Principales

### Figuras Geométricas implementadas
- Esferas
- Cubos
- Triangulos
- Disco
- Toroide
- Piramide
- Cilindro
- Elipsoide

### Materiales Implementados

- **Reflectivos:** `Metalblack` (Torus), `steel_reflective` (pirámides con textura de acero)
- **Con Texturas:** `concreto` (cubos), `terrazo` (pirámides), `steel_reflective`
- **Transparentes:** 5 colores con IOR=2.0 (rojo, verde, amarillo, naranja, púrpura)
- **Difusos:** `bone` (blanco brillante), `oil` (negro mate)
- **Environment Map:** Fondo de galaxia espacial

### Sistema de Iluminación

- **Ambient Light** - Iluminación base (intensity=0.5)
- **Spot Light** - Luz focal desde arriba (intensity=2.0)
- **Directional Light** - Luz direccional amarilla tipo sol (intensity=0.8)
- **Point Light** - Luz puntual en el centro del Torus (intensity=1.5)

## Descripción de Archivos del Proyecto

### Core del Ray Tracer

- **`RayTracer.py`** - Script principal que define la escena completa con 41 figuras geométricas, 15+ materiales y 4 fuentes de luz. Ejecuta el renderizado y genera la imagen final.

- **`gl.py`** - Motor de ray tracing. Contiene la clase `Renderer` que implementa el algoritmo principal de trazado de rayos, cálculo de intersecciones, reflexiones, refracciones y shading.

- **`camera.py`** - Define la cámara virtual de la escena con posición, orientación y campo de visión (FOV).

### Geometría

- **`figures.py`** - Implementa todas las figuras geométricas del proyecto:
  - **Torus**: Algoritmo de muestreo + bisección con ecuación implícita
  - **Sphere**: Intersección analítica ray-sphere
  - **Cylinder**: Intersección con superficie lateral y tapas
  - **Pyramid**: Intersección con 4 planos triangulares
  - **AABB**: Cubos alineados a ejes (slab method)
  - **Ellipsoid**: Transformación a esfera unitaria
  - **Disk**: Intersección ray-plane con validación de radio
  - **Triangle**: Algoritmo de Möller-Trumbore

- **`intercept.py`** - Clase que almacena información de intersecciones ray-object (distancia, punto, normal, objeto).

### Materiales e Iluminación

- **`material.py`** - Sistema de materiales con soporte para:
  - Materiales difusos (modelo de Phong)
  - Materiales reflectivos (`REFLECTIVE`)
  - Materiales transparentes con índice de refracción (`TRANSPARENT`)
  - Texturas BMP aplicadas a materiales

- **`lights.py`** - Sistema de iluminación con 4 tipos de luces:
  - **AmbientLight**: Iluminación uniforme base
  - **PointLight**: Luz puntual con atenuación por distancia
  - **DirectionalLight**: Luz direccional (tipo sol)
  - **SpotLight**: Luz focal con dirección y cono de iluminación

### Matemáticas y Física

- **`MathLib.py`** - Funciones matemáticas auxiliares para operaciones vectoriales, normalización, productos punto y cruz.

- **`refractionFunctions.py`** - Implementa la Ley de Snell para el cálculo de refracciones en materiales transparentes, incluyendo reflexión total interna.

### Entrada/Salida

- **`BMP_Writer.py`** - Exportador de imágenes en formato BMP. Genera el archivo `output.bmp` con el resultado del renderizado.

- **`BMPTexture.py`** - Cargador de texturas en formato BMP. Lee archivos de imagen y los convierte en arrays para mapeo de texturas.

### Recursos

- **`textures/`** - Carpeta con texturas en formato BMP (resolución 2K):
  - `envGalaxy.bmp` - Environment map con fondo de galaxia espacial
  - `Concreto2K.bmp` - Textura de concreto para cubos
  - `TerrazzoSlab028_COL_2K_METALNESS.bmp` - Textura de terrazo para pirámides
  - `Poliigon_MetalSteelBrushed_7174_BaseColor.bmp` - Textura de acero cepillado
  - Otras texturas adicionales

- **`output.bmp`** - Imagen renderizada final (720×720 píxeles) generada por el ray tracer.

### Configuración

- **`.gitignore`** - Especifica archivos y carpetas que Git debe ignorar (venv, __pycache__, archivos temporales).

- **`venv/`** - Entorno virtual de Python (no incluido en el repositorio).

- **`__pycache__/`** - Caché de archivos compilados de Python (no incluido en el repositorio).

## Resultado

### Imagen de Referencia
<img width="602" height="581" alt="Image" src="https://github.com/user-attachments/assets/bc3705a5-724c-4c10-b2d4-69170d4610c4" />

### Render Final (720×720)
<img width="897" height="935" alt="Image" src="https://github.com/user-attachments/assets/e2936e40-c320-41fe-8a41-6c9729935f11" />

## Instalación y Ejecución

### Requisitos

- **Python 3.10+**
- **Pygame**
- **NumPy**

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/jaq23369/Modulo2-RayTracing.git
cd Modulo2-RayTracing

# 2. Cambiar a la rama Proyecto2
git checkout Proyecto2
cd Proyecto2

# 3. Crear entorno virtual (opcional)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 4. Instalar dependencias
pip install pygame numpy

# 5. Ejecutar
python RayTracer.py
```

# Hecho por:
- Joel Antonio Jaquez López #23369
