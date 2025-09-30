# Lab 8: Ray-Intersect Algorithm, New Shapes

El objetivo de este laboratorio era renderizar nuevas figuras a través del RayTracer simple que se ha estado trabajando. Para este laboratorio se implementó el cilindro y la elipsoide:

## Cylinder (Cilindro)

### Descripción
El cilindro se define por su posición (centro de la base inferior), radio y altura. La intersección se divide en dos partes: el cuerpo lateral (cilindro infinito) y las tapas (discos superior e inferior).

### Algoritmo de Intersección
1. **Intersección Lateral**: Se resuelve la ecuación cuadrática para un cilindro infinito alineado con el eje Y.
   - Ecuación: (x - cx)² + (z - cz)² = r², ignorando Y.
   - Coeficientes:
     - a = dx² + dz²
     - b = 2 * ((ox - cx) * dx + (oz - cz) * dz)
     - c = (ox - cx)² + (oz - cz)² - r²
   - Discriminante: D = b² - 4*a*c
   - Si D >= 0, calcular t1 y t2, verificar si el punto de intersección está dentro de la altura (0 <= y_rel <= h).

2. **Intersección con Tapas**: Para cada tapa (superior e inferior), se calcula la intersección con un plano y se verifica si está dentro del radio.
   - Tapa inferior: y = cy, normal = [0, -1, 0]
   - Tapa superior: y = cy + h, normal = [0, 1, 0]
   - Distancia: t = (y_plano - oy) / dy, verificar distancia al centro <= r.

3. **Selección de Intersección**: Se elige la intersección más cercana válida (t > 0).

### Normal y Coordenadas UV
- Normal lateral: Vector desde el centro al punto de impacto, normalizado.
- UV: Cilíndricas para lateral (u basado en ángulo, v en altura), planas para tapas.

## Ellipsoid (Elipsoide)

### Descripción
El elipsoide se define por su centro y radios en los ejes X, Y, Z. Se asume alineado con los ejes coordenados.

### Algoritmo de Intersección
Se resuelve la ecuación cuadrática general del elipsoide:
(x - cx)² / rx² + (y - cy)² / ry² + (z - cz)² / rz² = 1

1. **Coeficientes Cuadráticos**:
   - A = (dx / rx)² + (dy / ry)² + (dz / rz)²
   - B = 2 * ((ox - cx) * dx / rx² + (oy - cy) * dy / ry² + (oz - cz) * dz / rz²)
   - C = (ox - cx)² / rx² + (oy - cy)² / ry² + (oz - cz)² / rz² - 1

2. **Discriminante y Soluciones**:
   - D = B² - 4*A*C
   - Si D >= 0, calcular t1 = (-B - sqrt(D)) / (2*A), t2 = (-B + sqrt(D)) / (2*A)
   - Elegir la t > 0 más pequeña.

### Normal y Coordenadas UV
- Normal: Gradiente de la ecuación elipsoidal, normalizado.
- UV: Esféricas (u basado en ángulo XZ, v en Y).

## Instalación y Dependencias

# Asegurarse de tener instaladas las siguientes dependencias
- pip install numpy pygame

### Clonación del Repositorio
Para clonar el repositorio y acceder a la carpeta de Lab8:
```bash
git clone https://github.com/jaq23369/Modulo2-RayTracing.git
cd Modulo2-RayTracing/Lab8
```
# Imagen del resultado:
<img width="1576" height="796" alt="Image" src="https://github.com/user-attachments/assets/49088348-cc8a-4e8f-b50a-ebc37d36d03a" />
