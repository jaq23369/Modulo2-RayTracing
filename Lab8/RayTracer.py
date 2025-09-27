import pygame
from gl import *
from BMP_Writer import GenerateBMP
from figures import *
from lights import *
from material import Material, REFLECTIVE, TRANSPARENT
from BMPTexture import BMPTexture

width = 512
height = 256
screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.envMap = BMPTexture("textures/goegap_road_4k.bmp")

brick = Material(diffuse = [1,0,0], spec = 16, ks = 0.5)
grass = Material(diffuse = [0,1,0], spec = 32, ks = 0.4)
sun = Material(diffuse = [1,1,0], spec = 16, ks = 0.5)
oil = Material(diffuse = [0,0,0], spec = 32, ks = 0.4)
ocean = Material(diffuse = [0,0.5,1], spec = 64, ks = 0.3)
fire = Material(diffuse = [1,0.5,0], spec = 64, ks = 0.3)
grape = Material(diffuse = [0.5,0,0.5], spec = 64, ks = 0.3)
bone = Material(diffuse = [1,1,1], spec = 100, ks = 0.7)
darkGrayWall = Material(diffuse=[0.3, 0.3, 0.3], spec=8, ks=0.1)
# Para techo blanco
whiteCeiling = Material(diffuse=[0.9, 0.9, 0.9], spec=10, ks=0.1)
# Para piso beige
beigeFloor = Material(diffuse=[0.8, 0.8, 0.7], spec=20, ks=0.2)
lightGrayWall = Material(diffuse=[0.8, 0.8, 0.8], spec=12, ks=0.15)

# Material Reflectivo
mirror = Material(diffuse = [0.9, 0.9, 0.9], spec = 128, ks = 0.5, matType = REFLECTIVE)
blueMirror = Material(diffuse = [0, 0, 0.9], spec = 64, ks = 0.2, matType = REFLECTIVE)

# Material con textura y Reflectivo
#terrazo = Material(texture = BMPTexture("textures/TerrazzoSlab028_COL_2K_METALNESS.bmp"))
#flatGrass = Material(diffuse = [0.9, 0.9, 0.9], spec = 128, ks = 0.5, texture = BMPTexture("textures/Poliigon_GrassPatchyGround_4585_BaseColor.bmp"), matType = REFLECTIVE)
#quartzite = Material(diffuse = [0.9, 0.9, 0.9], spec = 128, ks = 0.5, texture = BMPTexture("textures/Poliigon_StoneQuartzite_8060_BaseColor.bmp"), matType = REFLECTIVE)
#Metalgold = Material(diffuse=[1, 0.8, 0], spec=256, ks=0.8, texture=BMPTexture("textures/Poliigon_MetalGoldPaint_7253_BaseColor.bmp"), matType=REFLECTIVE)
#Metalblack = Material(diffuse=[0.9, 0.9, 0.9], spec=512, ks=0.6, texture=BMPTexture("textures/Poliigon_MetalPaintedMatte_7037_BaseColor.bmp"), matType=REFLECTIVE)
#redFabric = Material(diffuse=[1, 0.2, 0.2], spec=128, ks=0.7, texture=BMPTexture("textures/textura-de-tela-tenido-anudado-degradado-colorido.bmp"), matType=REFLECTIVE)

# Material Transparente
glass = Material(ior = 1.5, matType=TRANSPARENT)
diamond = Material(ior = 2.0, matType=TRANSPARENT)
#water = Material(ior = 1.33, texture = BMPTexture("textures/1636.bmp"), diffuse=[1, 1, 1], spec=128, ks=0.5, matType = TRANSPARENT)


#rend.scene.append(Sphere(position = [1.5, 0, -5], radius = 1, material=quartzite))
#rend.scene.append(Sphere(position = [0, 0, -5], radius = 1, material=glass))


#rend.scene.append(Sphere(position=[0, 0, -5], radius=1.0, material=brick))

# Triangulo
# rend.scene.append(Triangle(v0=[-0.75, -0.75, -5], v1=[0.75, -0.75, -5], v2=[0, 0.75, -5], material=brick))

# Cubo 1
# rend.scene.append(AABB(position=[-1.5, -0.5, -5], sizes=[0.75, 0.75, 0.75], material=ocean))

# Cubo 2
# rend.scene.append(AABB(position=[1.5, -0.5, -5], sizes=[0.75, 0.75, 0.75], material=grass))

# Ellipsoid en la posición del triángulo
#rend.scene.append(Ellipsoid(position=[0, 0, -5], radii=[0.6, 0.4, 0.4], material=brick))
rend.scene.append(Cylinder(position=[0, 0, -5], radius=0.7, height=1.2, material=brick))

# Disco
rend.scene.append(Disk(position=[0, -1, -5], normal=[0, 1, 0], radius=2, material=mirror))

# Piso
rend.scene.append( Plane(position = [0, -1.5, 0], normal = [0, 1, 0], material=bone) )

# Techo
rend.scene.append(Plane(position=[0, 3, 0], normal=[0, -1, 0], material=bone))  

# Pared Izquierda
rend.scene.append(Plane(position=[-3, 0, 0], normal=[1, 0, 0], material=darkGrayWall))

# Pared Derecha
rend.scene.append(Plane(position=[3, 0, 0], normal=[-1, 0, 0], material=darkGrayWall))  

# Fondo
rend.scene.append(Plane(position=[0, 0, -8], normal=[0, 0, 1], material=darkGrayWall)) 


#rend.scene.append(AABB(position=[2, 1.5, -7], sizes=[1,1,1], material=mirror))
#rend.scene.append(Triangle(v0=[-3, 0, -5], v1=[-2, 0, -5], v2=[-2.5, 1, -5], material=ocean))  
#rend.scene.append(Sphere(position=[3, 1, -5], radius=1.5, material=grass))
#rend.scene.append(Sphere(position=[1, 0, -5], radius=0.5, material=grass))    
#rend.scene.append(Sphere(position=[1.5, 0, -5], radius=0.6, material=grass)) 
#rend.scene.append(Sphere(position=[1.5, 1, -5], radius=0.8, material=Metalblack)) # Reflectiva 1

# Abajo
#rend.scene.append(Sphere(position=[-1.5, -1, -5], radius=0.8, material=redFabric))  # Reflectiva 2
#rend.scene.append(Sphere(position=[0, 0, -5], radius=0.6, material=diamond)) # Transparente 1
#rend.scene.append(Sphere(position=[1.5, -1, -5], radius=0.8, material=water)) # Transparente 2


rend.lights.append( AmbientLight(intensity = 0.5) )
#rend.lights.append( DirectionalLight(direction = [0, 0, 1], intensity = 3) )
rend.lights.append(SpotLight(position=[0, 2, -5], direction=[0, -1, 0], intensity=2))
#rend.lights.append( SpotLight(position = [-0.5, 1, -5], intensity = 2) )

#rend.lights.append( PointLight(position = [0, 0, -4]) )
#rend.lights.append(SpotLight(position = [0, 0, -5], direction = [-1, 0, 0]) )
#rend.lights.append( PointLight(position = [0, 0, -5], intensity = 1.5) )
#rend.lights.append( DirectionalLight(direction = [-1, -1, -1]) )
#rend.lights.append( DirectionalLight(direction = [0, -1, -1]) )
#rend.lights.append( DirectionalLight(color = [1, 1, 0], direction = [1, 0, -1], intensity = 0.5) )


rend.glRender()


isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    pygame.display.flip()
    clock.tick(60)

GenerateBMP("output.bmp", width, height, 3, rend.frameBuffer)

pygame.quit()