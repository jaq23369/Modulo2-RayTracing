from MathLib import reflectVector
import numpy as np
from refractionFunctions import refractVector, totalInternalReflection, fresnel

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2

class Material(object):
    def __init__(self, diffuse = [1,1,1], spec = 1.0, ks = 0.0, ior = 1.0, texture = None, matType = OPAQUE):
        self.diffuse = diffuse
        self.spec = spec
        # Coeficiente ks, es como un coeficiente estetico
        self.ks = ks
        self.ior = ior
        self.texture = texture
        self.matType = matType
    
    def GetSurfaceColor(self, intercept, renderer, recursion = 0):

        # Phong reflection model
        # LightColors = LightColor * (1-ks) + Specular * ks
        # FinalColor = DiffuseColor * LightColor

        lightColor = [0,0,0]
        specColor = [0,0,0]
        reflectColor = [0,0,0]
        refractColor = [0,0,0]
        
        finalColor = self.diffuse

        if self.texture and intercept.texCoords:
            textureColor = self.texture.getColor(intercept.texCoords[0], intercept.texCoords[1])
            finalColor = [finalColor[i] * textureColor[i] for i in range(3)]

        # Color de la luz
        for light in renderer.lights:
            shadowIntercept = None

            if light.lightType == "Directional":
                lightDir = [-i for i in light.direction]
                shadowIntercept = renderer.glCastRay(intercept.point, lightDir, intercept.obj)
            
            elif light.lightType == "Point" or light.lightType == "Spot":
                lightDir = np.subtract(light.position, intercept.point)
                # Distancia R, distancia desde el punto de interseccion hasta la luz
                R = np.linalg.norm(lightDir)
                lightDir /= R  # Normalizar la direccion
                shadowIntercept = renderer.glCastRay(intercept.point, lightDir, intercept.obj)
                if shadowIntercept:
                    if shadowIntercept.distance >= R:
                        shadowIntercept = None




            if shadowIntercept == None:
                specColor = [(specColor[i] + light.GetSpecularColor(intercept, renderer.camera.translation)[i]) for i in range(3)]

                if self.matType == OPAQUE:
                     lightColor = [(lightColor[i] + light.GetLightColor(intercept)[i]) for i in range(3)]

        if self.matType == REFLECTIVE:
            rayDir = [-i for i in intercept.rayDirection]
            reflect = reflectVector(intercept.normal, rayDir)
            reflectIntercept = renderer.glCastRay(intercept.point, reflect, intercept.obj, recursion + 1)
            if reflectIntercept != None:
                reflectColor = reflectIntercept.obj.material.GetSurfaceColor(reflectIntercept, renderer, recursion + 1)
            else:
                reflectColor = renderer.glEnvMapColor(intercept.point, reflect)
        
        elif self.matType == TRANSPARENT:
            # Revisamos si el rayo viene de afuera
            outside = np.dot(intercept.normal, intercept.rayDirection) < 0
            
            # Agregar el bias
            bias = [i * 0.001 for i in intercept.normal]

            # Refleccion
            rayDir = [-i for i in intercept.rayDirection]
            reflect = reflectVector(intercept.normal, rayDir)
            reflectOrig = np.add(intercept.point, bias) if outside else np.subtract(intercept.point, bias)
            reflectIntercept = renderer.glCastRay(reflectOrig, reflect, None, recursion + 1)
            if reflectIntercept != None:
                reflectColor = reflectIntercept.obj.material.GetSurfaceColor(reflectIntercept, renderer, recursion + 1)
            else:
                reflectColor = renderer.glEnvMapColor(intercept.point, reflect)
            
            # Refraccion
            if not totalInternalReflection(intercept.normal, intercept.rayDirection, 1.0, self.ior):
                refract = refractVector(intercept.normal, intercept.rayDirection, 1.0, self.ior)
                refractOrig = np.subtract(intercept.point, bias) if outside else np.add(intercept.point, bias)
                refractIntercept = renderer.glCastRay(refractOrig, refract, None, recursion + 1)
                if  refractIntercept != None:
                    refractColor = refractIntercept.obj.material.GetSurfaceColor(refractIntercept, renderer, recursion + 1)
                else:
                    refractColor = renderer.glEnvMapColor(intercept.point, refract)

                # Usamos fresnel
                Kr, Kt = fresnel(intercept.normal, intercept.rayDirection, 1.0, self.ior)
                reflectColor = [i * Kr for i in reflectColor]
                refractColor = [i * Kt for i in refractColor]

        # Diffse * (Light + Reflect + Refract) + Specular
        finalColor = [finalColor[i] * (lightColor[i] + reflectColor[i] + refractColor[i]) for i in range(3)]
        finalColor = [finalColor[i] + specColor[i] for i in range(3)]
        finalColor = [min(1, finalColor[i]) for i in range(3)]

        return finalColor
