from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Set up the window
window.title = "FPS Game"
window.fullscreen = False
window.borderless = False
window.exit_button.visible = False

# Define the texture paths
grass_texture = 'URSINA/textures/grass.png'
stone_texture = 'URSINA/textures/brick.png'
building_texture = 'URSINA/textures/building.png'

# Load gun texture
gun_texture = 'URSINA/textures/gun.png'

# Create the player
player = FirstPersonController()

# Create the ground and walls
ground = Entity(model='plane', texture=grass_texture, scale=(50, 1, 50), collider='box')
wall_left = Entity(model='cube', texture= "brick", scale=(1, 3, 50), position=(-25, 1.5, 0), collider='box')
wall_right = Entity(model='cube', texture="brick", scale=(1, 3, 50), position=(25, 1.5, 0), collider='box')
wall_front = Entity(model='cube', texture="brick", scale=(50, 3, 1), position=(0, 1.5, 25), collider='box')
wall_back = Entity(model='cube', texture="brick", scale=(50, 3, 1), position=(0, 1.5, -25), collider='box')

# Create terrain
terrain = Entity(model='plane', texture=grass_texture, scale=(100, 1, 100), position=(0, -1, 0))

# Create buildings
building1 = Entity(model='cube', texture="brick", scale=(4, 6, 4), position=(10, 3, 10), collider='box')
building2 = Entity(model='cube', texture="brick", scale=(6, 8, 6), position=(-15, 4, -10), collider='box')
building3 = Entity(model='cube', texture="brick", scale=(5, 7, 5), position=(20, 3.5, -15), collider='box')

# Create gun entity
gun = Entity(model='cube', texture=gun_texture, scale=(0.5, 0.5, 1), position=(0.5, -0.5, 1), parent=camera)

# Create some cubes to interact with
cubes = []
for i in range(10):
    cube = Entity(model='cube', texture="brick", collider='box')
    cube.position = (random.uniform(-20, 20), 1.5, random.uniform(-20, 20))
    cubes.append(cube)

def input(key):
    if key == 'left mouse down':
        bullet = Entity(model='sphere', color=color.red, scale=0.2, position=camera.position, collider='sphere')
        bullet.animate_position(bullet.position + (camera.forward * 50), duration=1, curve=curve.linear)
        invoke(setattr, bullet, 'enabled', False, delay=1)

def update():
    # Check for collisions with cubes
    for cube in cubes:
        if player.intersects(cube).hit:
            destroy(cube)

app.run()

