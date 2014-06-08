'''
Created on May 14, 2014

@author: tdongsi
'''

# program template for Spaceship
import simpleguitk as simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600

MAX_ROCK_NUMBER = 12
score = 0
lives = 3
time = 0.5
started = False
mode = 'web' # 'local' or 'web'

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image_url = {'local' : "E:\MyDropbox\Photos\spaceship\debris2_blue.png",
                    'web' : "https://dl.dropbox.com/s/ltii3ztqgesc8kk/debris2_blue.png"}
debris_image = simplegui.load_image(debris_image_url[mode])

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("https://dl.dropbox.com/s/1b8nkxdedap16kc/nebula_blue.s2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("https://dl.dropbox.com/s/vkcje1kj1kzfrgp/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("https://dl.dropbox.com/s/8l4zmm1ez6lyqnb/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("https://dl.dropbox.com/s/mopmaasmcw4s2le/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("https://dl.dropbox.com/s/rrbr4nx1g5nsmrh/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("https://dl.dropbox.com/s/77tmkiovimuukvl/explosion_alpha.png")

# # sound assets purchased from sounddogs.com, please do not redistribute
# soundtrack = simplegui.load_sound("https://dl.dropbox.com/s/pb3gk4umf2gw0p6/soundtrack.mp3")
missile_sound = simplegui.load_sound("https://www.dropbox.com/s/qy740p7a25vujhp/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("https://dl.dropbox.com/s/5kztd3jqw2buy98/thrust.mp3")
# explosion_sound = simplegui.load_sound("https://dl.dropbox.com/s/1cs4483k0hivthh/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.thruster_sound = sound
        
        self.ANGLE_VEL_INCREMENT = 0.1
        self.ANGLE_VEL_MAX = 0.3
    
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
        
    def set_thruster(self, status):
        self.thrust = status
        if (self.thruster_sound): 
            if (self.thrust):
                self.thruster_sound.play()
            else:
                self.thruster_sound.rewind()
        
    def increment_angle_vel(self):
        self.angle_vel += self.ANGLE_VEL_INCREMENT
        if self.angle_vel > self.ANGLE_VEL_MAX:
            self.angle_vel = self.ANGLE_VEL_MAX
        
    def decrement_angle_vel(self):
        self.angle_vel -= self.ANGLE_VEL_INCREMENT
        if self.angle_vel < -self.ANGLE_VEL_MAX:
            self.angle_vel = -self.ANGLE_VEL_MAX
        
    def shoot(self):
        global a_missile
        
        CANNON_DISPLACEMENT = 35
        cannon_pos = angle_to_vector(self.angle)
        cannon_pos[0] *= CANNON_DISPLACEMENT
        cannon_pos[1] *= CANNON_DISPLACEMENT
        cannon_pos[0] += self.pos[0]
        cannon_pos[1] += self.pos[1]
        
        MISSILE_SPEED = 10
        missile_vel = angle_to_vector(self.angle)
        missile_vel[0] *=  MISSILE_SPEED
        missile_vel[1] *=  MISSILE_SPEED
        missile_vel[0] += self.vel[0]
        missile_vel[1] += self.vel[1]
        
        a_missile = Sprite(cannon_pos, missile_vel, self.angle, 0, 
                           missile_image, missile_info, missile_sound)
        
    def draw(self,canvas):
        # There is a small displacement of the ship's center in the image 
        DIPLACEMENT = 2
        if (self.thrust):
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0] + DIPLACEMENT, self.image_center[1]], 
                              self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        # Update thrust
        accel = [0, 0]
        if (self.thrust):
            accel = angle_to_vector(self.angle)
        
        ACCEL_MAG = 0.4
        # Update velocity
        self.vel[0] += ACCEL_MAG * accel[0]
        self.vel[1] += ACCEL_MAG * accel[1]
        
        # Update position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # Warp around
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
        
        # Update angle
        self.angle += self.angle_vel
        
        # Friction - let c be a small constant, then friction = - c * velocity 
        # Friction udpate. c = 0.05
        FRICTION = 0.99
        self.vel[0] *= FRICTION
        self.vel[1] *= FRICTION
        
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
    
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
       
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, 
                          self.pos, self.image_size, self.angle)
#         canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
    
    def update(self):
        # Update position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # Warp around
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
        
        # Update angle
        self.angle += self.angle_vel
        
    def collide(self, other_object):
        distance = dist( self.get_position(), other_object.get_position())
        radius_sum = self.get_radius() + other_object.get_radius()
        if distance > radius_sum:
            return False
        else:
            return True
        
def keyup(key):
    if (key == simplegui.KEY_MAP['left']):
        my_ship.increment_angle_vel()
    elif (key == simplegui.KEY_MAP['right']):
        my_ship.decrement_angle_vel()
    elif (key == simplegui.KEY_MAP['up']):
        my_ship.set_thruster(False)

def keydown(key):
    global my_ship
    if (key == simplegui.KEY_MAP['right']):
        my_ship.increment_angle_vel()
    elif (key == simplegui.KEY_MAP['left']):
        my_ship.decrement_angle_vel()
    elif (key == simplegui.KEY_MAP['up']):
        my_ship.set_thruster(True)
    elif (key == simplegui.KEY_MAP['space']):
        my_ship.shoot()

# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True

def process_sprite_group(canvas, sprite_set):
    # Create a copy to avoid "RuntimeError: Set changed size during iteration"
    # rock_spawner() maybe activated during iteration
    for sprite in list(sprite_set):
        sprite.draw(canvas)
        sprite.update()

def group_collide(sprite_set, other_object):
    for sprite in list(sprite_set):
        if sprite.collide(other_object):
            sprite_set.remove(sprite)
            return True
    
    # No collision here
    return False
           
def draw(canvas):
    global time, started, lives
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    # Process rocks
    process_sprite_group(canvas, rock_group)
    if group_collide(rock_group, my_ship):
        lives -= 1
    
    # draw text
    canvas.draw_text( 'Lives: %d'%lives, (50, 50), 20, 'White')
    canvas.draw_text( 'Score: %d'%score, (WIDTH-150, 50), 20, 'White')

    # draw ship and sprites
    my_ship.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_missile.update()
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    # Random velocity
    MAX_VEL = 2
    RANGE_VEL = 2*MAX_VEL
    vx = RANGE_VEL*random.random() - MAX_VEL
    vy = RANGE_VEL*random.random() - MAX_VEL
    # Random angular velocity
    MAX_ANG_VEL = 0.2
    RANGE_ANG_VEL = 2*MAX_ANG_VEL
    
    if len(rock_group) < MAX_ROCK_NUMBER:
        a_rock = Sprite([random.randrange(WIDTH), random.randrange(HEIGHT)], [vx, vy], random.random(), RANGE_ANG_VEL*random.random() - MAX_ANG_VEL, asteroid_image, asteroid_info)
        rock_group.add(a_rock)
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 3], 0, ship_image, ship_info, ship_thrust_sound)
# my_ship = Ship([WIDTH / 2, HEIGHT / 2], [3, 0], 1, ship_image, ship_info, ship_thrust_sound)

# a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
# a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.2, asteroid_image, asteroid_info)
rock_group = set([])

a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
