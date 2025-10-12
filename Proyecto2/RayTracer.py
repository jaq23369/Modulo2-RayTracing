import pygame
from gl import *
from BMP_Writer import GenerateBMP
from figures import *
from lights import *
from material import Material, REFLECTIVE, TRANSPARENT
from BMPTexture import BMPTexture

width = 720
height = 720
screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.envMap = BMPTexture("textures/envGalaxy.bmp")

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

# Material Reflectivo con textura 1K
#steel_reflective = Material(diffuse=[0.9, 0.9, 0.9], spec=128, ks=0.5, texture=BMPTexture("textures/Poliigon_MetalSteelBrushed_7174_BaseColor.bmp"), matType=REFLECTIVE)

# Material Reflectivo
mirror = Material(diffuse = [0.9, 0.9, 0.9], spec = 128, ks = 0.5, matType = REFLECTIVE)
blueMirror = Material(diffuse = [0, 0, 0.9], spec = 64, ks = 0.2, matType = REFLECTIVE)

# Material con textura y Reflectivo
terrazo = Material(texture = BMPTexture("textures/TerrazzoSlab028_COL_2K_METALNESS.bmp"))
concreto = Material(texture = BMPTexture("textures/Concreto2K.bmp"))
#flatGrass = Material(diffuse = [0.9, 0.9, 0.9], spec = 128, ks = 0.5, texture = BMPTexture("textures/Poliigon_GrassPatchyGround_4585_BaseColor.bmp"), matType = REFLECTIVE)
#quartzite = Material(diffuse = [0.9, 0.9, 0.9], spec = 128, ks = 0.5, texture = BMPTexture("textures/Poliigon_StoneQuartzite_8060_BaseColor.bmp"), matType = REFLECTIVE)
#Metalgold = Material(diffuse=[1, 0.8, 0], spec=256, ks=0.8, texture=BMPTexture("textures/Poliigon_MetalGoldPaint_7253_BaseColor.bmp"), matType=REFLECTIVE)
Metalblack = Material(diffuse=[0.9, 0.9, 0.9], spec=512, ks=0.6, matType=REFLECTIVE)
#redFabric = Material(diffuse=[1, 0.2, 0.2], spec=128, ks=0.7, texture=BMPTexture("textures/textura-de-tela-tenido-anudado-degradado-colorido.bmp"), matType=REFLECTIVE)

# Material Reflectivo con textura 1K
steel_reflective = Material(diffuse=[0.9, 0.9, 0.9], spec=128, ks=0.5, texture=BMPTexture("textures/Poliigon_MetalSteelBrushed_7174_BaseColor.bmp"), matType=REFLECTIVE)


# Material Transparente
glass = Material(ior = 1.5, matType=TRANSPARENT)
diamond_gren = Material(ior = 2.0, diffuse=[0, 1, 0], matType=TRANSPARENT)
quartz = Material(ior=1.8, matType=TRANSPARENT)
# Materiales transparentes coloreados
transparent_red = Material(diffuse=[1,0,0], ior=2.0, matType=TRANSPARENT)
transparent_green = Material(diffuse=[0,1,0], ior=2.0, matType=TRANSPARENT)
transparent_yellow = Material(diffuse=[1,1,0], ior=2.0, matType=TRANSPARENT)
transparent_orange = Material(diffuse=[1,0.5,0], ior=2.0, matType=TRANSPARENT)
transparent_purple = Material(diffuse=[0.5,0,0.5], ior=2.0, matType=TRANSPARENT)
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


#rend.scene.append(Pyramid(position=[-2, 0, -5], base_size=1.5, height=2, material=brick))
rend.scene.append(Torus(position=[0, 1.1, -5], major_radius=1.5, minor_radius=0.2, material=Metalblack))
rend.scene.append(Sphere(position=[0, 1.1, -5], radius=0.5, material=bone))

rend.scene.append(Sphere(position=[0.93, 1.1, -4.5], radius=0.1, material=transparent_red))
rend.scene.append(Sphere(position=[-1, 1.1, -5.5], radius=0.2, material=transparent_green))
rend.scene.append(Sphere(position=[0, 1.39, -3.5], radius=0.2, material=transparent_yellow))
rend.scene.append(Sphere(position=[0.69, 0.53, -5], radius=0.2, material=transparent_orange))
rend.scene.append(Sphere(position=[-0.69, 0.53, -5], radius=0.2, material=transparent_orange))
rend.scene.append(Sphere(position=[-0.69, 1.46, -5], radius=0.2, material=transparent_purple))
rend.scene.append(Sphere(position=[0.69, 1.46, -5], radius=0.2, material=transparent_purple))
rend.scene.append(Sphere(position=[0, 0.1, -3.5], radius=0.2, material=transparent_yellow))

rend.scene.append(Cylinder(position=[-2.4, -1.7, -5], radius=0.2, height=3.5, material=Metalblack))
rend.scene.append(Cylinder(position=[-2.27, -1.7, -6], radius=0.2, height=2.5, material=Metalblack))
rend.scene.append(Cylinder(position=[2.4, -1.7, -5], radius=0.2, height=3.5, material=Metalblack))
rend.scene.append(Cylinder(position=[2.27, -1.7, -6], radius=0.2, height=2.5, material=Metalblack))
rend.scene.append(Pyramid(position=[-2.4, 1.82, -5], base_size=0.4, height=0.4, material=terrazo))
rend.scene.append(Pyramid(position=[2.4, 1.82, -5], base_size=0.4, height=0.4, material=terrazo))
rend.scene.append(Pyramid(position=[-2.33, -1.7, -7], base_size=1.1, height=5.8, material=steel_reflective))
rend.scene.append(Pyramid(position=[2.33, -1.7, -7], base_size=1.1, height=5.8, material=steel_reflective))
rend.scene.append(AABB(position=[-1.37, -1.1, -4], sizes=[0.5, 0.5, 0.5], material=concreto))
rend.scene.append(AABB(position=[-0.84, -1.1, -5], sizes=[0.6, 0.6, 0.6], material=concreto))
rend.scene.append(AABB(position=[-1.27, -0.68, -4.6], sizes=[0.48, 0.48, 0.48], material=concreto))
rend.scene.append(AABB(position=[1.37, -1.1, -4], sizes=[0.5, 0.5, 0.5], material=concreto))
rend.scene.append(AABB(position=[0.84, -1.1, -5], sizes=[0.6, 0.6, 0.6], material=concreto))
rend.scene.append(AABB(position=[1.27, -0.68, -4.6], sizes=[0.48, 0.48, 0.48], material=concreto))

rend.scene.append(AABB(position=[0, -1, -3], sizes=[0.7,0.7,0.7], material=concreto))
rend.scene.append(AABB(position=[-0.56, -1, -2.8], sizes=[0.4,0.4,0.4], material=concreto))
rend.scene.append(AABB(position=[0.56, -1, -2.8], sizes=[0.4,0.4,0.4], material=concreto))
rend.scene.append(Triangle(v0=[0.46, -0.8, -2.8], v1=[0.66, -0.8, -2.8], v2=[0.56, -0.4, -2.8], material=transparent_yellow))
rend.scene.append(Sphere(position=[-0.56, -0.6, -2.8], radius=0.15, material=transparent_green))
rend.scene.append(Ellipsoid(position=[0, -0.5, -3], radii=[0.2, 0.1, 0.1], material=transparent_red))
#rend.scene.append(Ellipsoid(position=[0, 1.45, -5], radii=[0.4, 0.2, 0.2], material=redFabric))
#rend.scene.append(Cylinder(position=[0, -0.88, -5], radius=0.4, height=2.0, material=fire))

# Cilindro grande a la derecha
#rend.scene.append(Ellipsoid(position=[1.5, 1.8, -5], radii=[0.3, 0.15, 0.15], material=sun))
#rend.scene.append(Cylinder(position=[1.5, -0.9, -5], radius=0.5, height=2.5, material=diamond_gren))


# Disco
rend.scene.append(Disk(position=[0, -1.6, -6], normal=[0, 1, 0], radius=2.9, material=oil))

# Piso
#rend.scene.append( Plane(position = [0, -1.5, 0], normal = [0, 1, 0], material=bone) )

# Techo
#rend.scene.append(Plane(position=[0, 3, 0], normal=[0, -1, 0], material=bone))  

# Pared Izquierda
#rend.scene.append(Plane(position=[-3, 0, 0], normal=[1, 0, 0], material=darkGrayWall))

# Pared Derecha
#rend.scene.append(Plane(position=[3, 0, 0], normal=[-1, 0, 0], material=darkGrayWall))  

# Fondo
#rend.scene.append(Plane(position=[0, 0, -8], normal=[0, 0, 1], material=darkGrayWall)) 


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
rend.lights.append(DirectionalLight(direction=[1, -1, -1], intensity=0.8, color=[1, 1, 0.8]))
rend.lights.append(PointLight(position=[0, 1.1, -5], intensity=1.5))
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