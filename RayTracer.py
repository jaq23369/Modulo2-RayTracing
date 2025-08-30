import pygame
from gl import *
from BMP_Writer import GenerateBMP
from figures import *
from lights import *
from material import Material

width = 256
height = 256

screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rend = Renderer(screen)

brick = Material(diffuse = [1,0,0], spec = 16, ks = 0.5)
grass = Material(diffuse = [0,1,0], spec = 32, ks = 0.4)
sun = Material(diffuse = [1,1,0], spec = 16, ks = 0.5)
oil = Material(diffuse = [0,0,0], spec = 32, ks = 0.4)
ocean = Material(diffuse = [0,0.5,1], spec = 64, ks = 0.3)
fire = Material(diffuse = [1,0.5,0], spec = 64, ks = 0.3)
grape = Material(diffuse = [0.5,0,0.5], spec = 64, ks = 0.3)


# Cabeza de la carita feliz 
rend.scene.append(Sphere(position = [0, 0, -7], radius = 2.5, material=sun))
# Ojo izquierdo de la carita feliz
rend.scene.append(Sphere(position = [-0.5, 0.75, -4.8], radius = 0.47, material=oil))
# Ojo derecho de la carita feliz
rend.scene.append(Sphere(position = [0.5, 0.75, -4.6], radius = 0.4, material=oil))
#rend.scene.append(Sphere(position = [1, 1, -5], radius = 0.5, material=grass))
# Parte de la boca
rend.scene.append(Sphere(position = [-1.35, -0.6, -4.8], radius = 0.3, material=brick))
rend.scene.append(Sphere(position = [1.35, -0.6, -4.8], radius = 0.3, material=grass))
rend.scene.append(Sphere(position = [-0.4, -1.1, -4.8], radius = 0.3, material=ocean))
rend.scene.append(Sphere(position = [0.4, -1.1, -4.8], radius = 0.3, material=fire))
#Nariz
rend.scene.append(Sphere(position = [-0.1, -0.1, -4.8], radius = 0.6, material=grape))


rend.lights.append( AmbientLight() )
rend.lights.append( DirectionalLight(direction = [-1, -1, -1]) )
rend.lights.append( DirectionalLight(direction = [0, 0, -1]) )
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