import numpy as np
from intercept import Intercept
from math import atan2, acos, pi

class Shape(object):
    def __init__(self, position, material):
        self.position = position
        self.material = material
        self.type = "None"

    def ray_intersect(self, orig, dir):
        return None

class Sphere(Shape):
    def __init__(self, position, radius, material):
        super().__init__(position, material)
        self.radius = radius
        self.type = "Sphere"
    
    def ray_intersect(self, orig, dir):

        # Asegurarse de trabajar con numpy arrays
        orig = np.array(orig, dtype=float)
        dir = np.array(dir, dtype=float)

        # Vector desde el origen del rayo hasta el centro de la esfera
        dir_length = np.linalg.norm(dir)
        if dir_length == 0:
            return  None
        dir = dir / dir_length  # Normalizar la dirección del rayo

        # Vector del origen del rayo al centro de la esfera
        origin_to_center = np.array(self.position, dtype=float) - orig

        # Proyeccion de que tan lejos esta el punto mas cercano del rayo al centro
        projection_distance = np.dot(origin_to_center, dir)

        # Distancia perpendicular al cuadrado (usando pitagoras)
        perpendicular_distance_squared = np.dot(origin_to_center, origin_to_center) - projection_distance ** 2
        radius_squared = self.radius * self.radius

        # Si el rayo pasa mas lejos que el radio, no hay interseccion
        if perpendicular_distance_squared > radius_squared:
            return None
        
        # Distanci desde el punto de proyeccion hasta las intersecciones
        half_chord_distance = np.sqrt(radius_squared - perpendicular_distance_squared)

        # Las 2 distancias de interseccion
        near_distance = projection_distance - half_chord_distance
        far_distance = projection_distance + half_chord_distance

        # Elegir la interseccion mas cercana que este adelante del origen
        epsilon = 1e-6
        if near_distance > epsilon:
            # Calcular punto de impacto y normal
            hit_point = orig + dir * near_distance
            normal = (hit_point - np.array(self.position)) / self.radius

            # Calcular coordenadas UV para texturas esféricas
            u = -atan2(normal[2], normal[0]) / (2 * pi) + 0.5
            v = acos(np.clip(-normal[1], -1, 1)) / pi
            texCoords = (u, v)

            # Devolver Intercept con toda la info
            return Intercept(hit_point, normal, near_distance, texCoords, dir, self)
    
        if far_distance > epsilon:
            # Lo mismo para la intersección lejana
            hit_point = orig + dir * far_distance
            normal = (hit_point - np.array(self.position)) / self.radius

            # Calcular coordenadas UV para texturas esféricas
            u = -atan2(normal[2], normal[0]) / (2 * pi) + 0.5
            v = acos(np.clip(-normal[1], -1, 1)) / pi
            texCoords = (u, v)

            return Intercept(hit_point, normal, far_distance, texCoords, dir, self)
        
        # Ambas estan detras del origen
        return None
    
class Plane(Shape):
    def __init__(self, position, normal, material):
        super().__init__(position, material)
        self.normal = normal / np.linalg.norm(normal)
        self.type = "Plane"

    def ray_intersect(self, orig, dir):
        # Asegurarse de trabajar con numpy arrays
        orig = np.array(orig, dtype=float)
        dir = np.array(dir, dtype=float)

        # Normalizar la dirección del rayo
        dir_length = np.linalg.norm(dir)
        if dir_length == 0:
            return None
        dir = dir / dir_length

        # Producto punto entre dirección del rayo y normal del plano
        denom = np.dot(dir, self.normal)

        # Si el rayo es paralelo al plano (denom ≈ 0), no hay intersección
        epsilon = 1e-6
        if abs(denom) < epsilon:
            return None

        # Calcular t: distancia desde el origen del rayo al plano
        t = np.dot(np.array(self.position) - orig, self.normal) / denom

        # Si t es negativo, la intersección está detrás del origen del rayo
        if t < epsilon:
            return None

        # Calcular punto de impacto
        hit_point = orig + dir * t

        # La normal del plano es constante
        normal = self.normal

        # Calcular coordenadas UV para texturas planas (basado en el punto de impacto)
        # Usar las coordenadas X y Z para U y V, escaladas para evitar repetición
        u = (hit_point[0] % 1 + 1) % 1  # Ciclo entre 0 y 1
        v = (hit_point[2] % 1 + 1) % 1  # Ciclo entre 0 y 1
        texCoords = (u, v)

        # Devolver Intercept con toda la info
        return Intercept(hit_point, normal, t, texCoords, dir, self)

class Disk(Plane):
    def __init__(self, position, normal, radius, material):
        super().__init__(position, normal, material)
        self.radius = radius
        self.type = "Disk"

    def ray_intersect(self, orig, dir):
        # Llamar al ray_intersect del plano padre
        intercept = super().ray_intersect(orig, dir)
        
        if intercept is None:
            return None
        
        # Calcular la distancia desde el centro del disco al punto de impacto
        distance = np.linalg.norm(intercept.point - np.array(self.position))
        
        # Si la distancia es menor o igual al radio, hay intersección
        if distance <= self.radius:
            return intercept
        
        # Si no, no hay intersección
        return None

class AABB(Shape):
    def __init__(self, position, sizes, material):
        super().__init__(position, material)
        self.sizes = np.array(sizes, dtype=float)
        self.bounds_min = np.array(position) - self.sizes / 2
        self.bounds_max = np.array(position) + self.sizes / 2
        self.type = "AABB"

    def ray_intersect(self, orig, dir):
        # Asegurarse de trabajar con numpy arrays
        orig = np.array(orig, dtype=float)
        dir = np.array(dir, dtype=float)

        # Normalizar la dirección del rayo
        dir_length = np.linalg.norm(dir)
        if dir_length == 0:
            return None
        dir = dir / dir_length

        # Inicializar t_min y t_max
        t_min = -float('inf')
        t_max = float('inf')

        # Para cada eje (x, y, z)
        for i in range(3):
            if abs(dir[i]) < 1e-6:
                # Rayo paralelo al eje
                if orig[i] < self.bounds_min[i] or orig[i] > self.bounds_max[i]:
                    return None
            else:
                t1 = (self.bounds_min[i] - orig[i]) / dir[i]
                t2 = (self.bounds_max[i] - orig[i]) / dir[i]
                t_near = min(t1, t2)
                t_far = max(t1, t2)
                t_min = max(t_min, t_near)
                t_max = min(t_max, t_far)
                if t_min > t_max:
                    return None

        # Si t_max < 0, la intersección está detrás
        if t_max < 0:
            return None

        # Punto de impacto
        t = t_min if t_min >= 0 else t_max
        hit_point = orig + dir * t

        # Calcular normal basada en la cara intersectada
        normal = np.zeros(3)
        epsilon = 1e-6
        if abs(hit_point[0] - self.bounds_min[0]) < epsilon:
            normal[0] = -1
        elif abs(hit_point[0] - self.bounds_max[0]) < epsilon:
            normal[0] = 1
        elif abs(hit_point[1] - self.bounds_min[1]) < epsilon:
            normal[1] = -1
        elif abs(hit_point[1] - self.bounds_max[1]) < epsilon:
            normal[1] = 1
        elif abs(hit_point[2] - self.bounds_min[2]) < epsilon:
            normal[2] = -1
        elif abs(hit_point[2] - self.bounds_max[2]) < epsilon:
            normal[2] = 1

        # Coordenadas UV simples (basadas en la cara)
        u = (hit_point[0] - self.bounds_min[0]) / (self.bounds_max[0] - self.bounds_min[0])
        v = (hit_point[1] - self.bounds_min[1]) / (self.bounds_max[1] - self.bounds_min[1])
        texCoords = (u, v)

        return Intercept(hit_point, normal, t, texCoords, dir, self)

class Triangle(Shape):
    def __init__(self, v0, v1, v2, material):
        # Centro del triángulo como position
        center = (np.array(v0) + np.array(v1) + np.array(v2)) / 3
        super().__init__(center, material)
        self.v0 = np.array(v0, dtype=float)
        self.v1 = np.array(v1, dtype=float)
        self.v2 = np.array(v2, dtype=float)
        # Calcular normal del triángulo
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        self.normal = np.cross(edge1, edge2)
        norm_length = np.linalg.norm(self.normal)
        if norm_length > 0:
            self.normal = self.normal / norm_length
        self.type = "Triangle"

    def ray_intersect(self, orig, dir):
        # Algoritmo de Möller-Trumbore
        orig = np.array(orig, dtype=float)
        dir = np.array(dir, dtype=float)

        # Normalizar dirección
        dir_length = np.linalg.norm(dir)
        if dir_length == 0:
            return None
        dir = dir / dir_length

        # Edges
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0

        # Determinante
        h = np.cross(dir, edge2)
        a = np.dot(edge1, h)
        if abs(a) < 1e-6:
            return None  # Rayo paralelo al triángulo

        f = 1.0 / a
        s = orig - self.v0
        u = f * np.dot(s, h)
        if u < 0.0 or u > 1.0:
            return None

        q = np.cross(s, edge1)
        v = f * np.dot(dir, q)
        if v < 0.0 or u + v > 1.0:
            return None

        # t
        t = f * np.dot(edge2, q)
        if t < 1e-6:
            return None  # Intersección detrás del origen

        # Punto de impacto
        hit_point = orig + dir * t

        # UV coords (barycentric)
        w = 1 - u - v
        texCoords = (u, v)  # u, v barycentric

        return Intercept(hit_point, self.normal, t, texCoords, dir, self)

class Cylinder(Shape):
    def __init__(self, position, radius, height, material):
        super().__init__(position, material)
        self.radius = radius
        self.height = height
        self.type = "Cylinder"

    def ray_intersect(self, orig, dir):
        orig = np.array(orig, dtype=float)
        dir = np.array(dir, dtype=float)

        dir_length = np.linalg.norm(dir)
        if dir_length == 0:
            return None
        dir = dir / dir_length

        # Centro de la base inferior
        center = np.array(self.position)

        # Intersección con el cilindro lateral (cilindro infinito)
        # Ecuación: (x - cx)^2 + (z - cz)^2 = r^2, ignorando y
        oc = orig - center
        a = dir[0]**2 + dir[2]**2
        b = 2 * (oc[0] * dir[0] + oc[2] * dir[2])
        c = oc[0]**2 + oc[2]**2 - self.radius**2

        if abs(a) < 1e-6:
            # Rayo paralelo al eje y
            if c > 0:
                return None
            # Intersección con tapas
            return self._intersect_caps(orig, dir)

        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return None

        sqrt_d = np.sqrt(discriminant)
        t1 = (-b - sqrt_d) / (2*a)
        t2 = (-b + sqrt_d) / (2*a)

        # Verificar si t1 o t2 están dentro de la altura
        hits = []
        for t in [t1, t2]:
            if t > 1e-6:
                hit_point = orig + dir * t
                y_rel = hit_point[1] - center[1]
                if 0 <= y_rel <= self.height:
                    normal = np.array([hit_point[0] - center[0], 0, hit_point[2] - center[2]])
                    normal = normal / np.linalg.norm(normal)
                    u = np.arctan2(hit_point[2] - center[2], hit_point[0] - center[0]) / (2 * np.pi) + 0.5
                    v = y_rel / self.height
                    texCoords = (u, v)
                    hits.append(Intercept(hit_point, normal, t, texCoords, dir, self))

        # Intersección con tapas
        cap_hit = self._intersect_caps(orig, dir)
        if cap_hit:
            hits.append(cap_hit)

        # Elegir la más cercana
        if hits:
            return min(hits, key=lambda h: h.distance)
        return None

    def _intersect_caps(self, orig, dir):
        center = np.array(self.position)
        # Tapa inferior (y = center[1])
        denom = dir[1]
        if abs(denom) > 1e-6:
            t_bottom = (center[1] - orig[1]) / denom
            if t_bottom > 1e-6:
                hit_point = orig + dir * t_bottom
                dist_sq = (hit_point[0] - center[0])**2 + (hit_point[2] - center[2])**2
                if dist_sq <= self.radius**2:
                    normal = np.array([0, -1, 0])
                    u = (hit_point[0] - center[0]) / self.radius * 0.5 + 0.5
                    v = (hit_point[2] - center[2]) / self.radius * 0.5 + 0.5
                    texCoords = (u, v)
                    return Intercept(hit_point, normal, t_bottom, texCoords, dir, self)

        # Tapa superior (y = center[1] + height)
        t_top = (center[1] + self.height - orig[1]) / denom
        if t_top > 1e-6:
            hit_point = orig + dir * t_top
            dist_sq = (hit_point[0] - center[0])**2 + (hit_point[2] - center[2])**2
            if dist_sq <= self.radius**2:
                normal = np.array([0, 1, 0])
                u = (hit_point[0] - center[0]) / self.radius * 0.5 + 0.5
                v = (hit_point[2] - center[2]) / self.radius * 0.5 + 0.5
                texCoords = (u, v)
                return Intercept(hit_point, normal, t_top, texCoords, dir, self)

        return None
