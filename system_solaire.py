import turtle
import math

class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)
        self.ssscreen.tracer(50)

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.planets:   
           p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

           rx = self.thesun.getXPos() - p.getXPos()
           ry = self.thesun.getYPos() - p.getYPos()
           r = math.sqrt(rx**2 + ry**2)

           accx = G * self.thesun.getMass()*rx/r**3
           accy = G * self.thesun.getMass()*ry/r**3

           p.setXVel(p.getXVel() + dt * accx)

           p.setYVel(p.getYVel() + dt * accy)

class Sun:
   def __init__(self, iname, irad, im, itemp):
       self.name = iname
       self.radius = irad
       self.mass = im
       self.temp = itemp
       self.x = 0
       self.y = 0

       self.sturtle = turtle.Turtle()
       self.sturtle.shape("circle")
       self.sturtle.color("yellow")

   def getName(self):
       return self.name

   def getRadius(self):
       return self.radius

   def getMass(self):
       return self.mass

   def getTemperature(self):
       return self.temp

   def getVolume(self):
       v = 4.0/3 * math.pi * self.radius**3
       return v

   def getSurfaceArea(self):
       sa = 4.0 * math.pi * self.radius**2
       return sa

   def getDensity(self):
       d = self.mass / self.getVolume()
       return d

   def setName(self, newname):
       self.name = newname

   def __str__(self):
       return self.name

   def getXPos(self):
       return self.x

   def getYPos(self):
       return self.y

class Planet:

   def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
       self.name = iname
       self.radius = irad
       self.mass = im
       self.distance = idist
       self.x = idist
       self.y = 0
       self.velx = ivx
       self.vely = ivy
       self.color = ic

       self.pturtle = turtle.Turtle()
       self.pturtle.up()
       self.pturtle.color(self.color)
       self.pturtle.shape("circle")
       self.pturtle.goto(self.x,self.y)
       self.pturtle.down()

   def getName(self):
       return self.name

   def getRadius(self):
       return self.radius

   def getMass(self):
       return self.mass

   def getDistance(self):
       return self.distance

   def getVolume(self):
       v = 4.0/3 * math.pi * self.radius**3
       return v

   def getSurfaceArea(self):
       sa = 4.0 * math.pi * self.radius**2
       return sa

   def getDensity(self):
       d = self.mass / self.getVolume()
       return d

   def setName(self, newname):
       self.name = newname

   def show(self):
        print(self.name)   

   def __str__(self):
       return self.name

   def moveTo(self, newx, newy):
       self.x = newx
       self.y = newy
       self.pturtle.goto(newx, newy)

   def getXPos(self):
       return self.x

   def getYPos(self):
       return self.y

   def getXVel(self):
       return self.velx

   def getYVel(self):
       return self.vely

   def setXVel(self, newvx):
       self.velx = newvx

   def setYVel(self, newvy):
       self.vely = newvy


def createSSandAnimate():
   ss = SolarSystem(2,2)    

   sun = Sun("SUN", 5000, 10, 5800)
   ss.addSun(sun)


   m = Planet("MERCURY", 19.5, 1000, .25, 0, 2, "blue")
   ss.addPlanet(m)

   m = Planet("EARTH", 47.5, 5000, 0.3, 0, 2.0, "green")
   ss.addPlanet(m)

   m = Planet("MARS", 50, 9000, 0.5, 0, 1.63, "red")
   ss.addPlanet(m)

   m = Planet("JUPITER", 100, 49000, 0.7, 0, 1, "black")
   ss.addPlanet(m)

   m = Planet("Pluto", 1, 500, 0.9, 0, .5, "orange")
   ss.addPlanet(m)

   m = Planet("Asteroid", 1, 500, 1.0, 0, .75, "cyan")
   ss.addPlanet(m)

   numTimePeriods = 20000
   for amove in range(numTimePeriods):
        ss.movePlanets()

   ss.freeze()

createSSandAnimate()

print(**********************************************************************************************************************************)

from turtle import Shape, Turtle, mainloop, Vec2D as Vec 
from time import sleep
#Turtle.bgcolor("black")

G = 8#constance gravitationnnelle


class Gravity(object):# classe Gravity avec un objet
    
    def __init__(self):
        self.planets = []#mettre la planet dans une liste
        self.time = 0# temps initial
        self.distance = 0.1# distance initiale
        
    def init(self):
        for planet in self.planets:#lire la liste
            planet.init()#ajouter les elements de la liste à la planete
            
    def start(self):
        for i in range(200):# boucle pour répéter 500 fois
            self.time += self.distance# additionner le temps initiale avec la distance initiale
            for planet in self.planets:#lire la liste
                planet.step()#permet d'avancer les planetes
                
                
class Planet(Turtle):# classe planete
    
    def __init__(self, mass, x_pos, velocity, gravity, shape):# soi-meme,masse, position initaile x, rapidité, gravité, forme
        Turtle.__init__(self, shape=shape)#
        self.penup()# ne pas dessiner (ne pas faire de tracer)
        self.mass = mass#masse donné = masse
        self.setpos(x_pos)# position x donné= position
        self.velocity = velocity#rapidité donné= rapidité
        gravity.planets.append(self)# apelle de la fonction gravity 
        self.gravity = gravity#gravité donné=gravité
        self.resizemode("user")# l'utilisateur choisi la forme de de la tortue
        self.pendown()#dessiner (faire un tracer)
        
    def init(self):
        distance = self.gravity.distance# utilise la fonction distance et la mettre dans une variable
        self.a = self.acc()# 
        self.velocity = self.velocity + 0.5 * distance * self.a#
        
    def acc(self):#
        a = Vec(0,0)# definir un vecteur a de 0,0
        for planet in self.gravity.planets:#lire la gravité des planets
            if planet != self:# si une planete differente d'une autre 
                velocity = planet.pos()-self.pos()# position de la planète moins la position de l'autre
                a += (G*planet.mass/abs(velocity)**3)*velocity# force de la planète 
        return a
    
    def step(self):
        distance = self.gravity.distance# apelle la disance dans la fonc gravity pour placer la valeur distance dans une variable
        self.setpos(self.pos() + distance * self.velocity)#mettre la planete à une position précise 
        if self.gravity.planets.index(self) != 0:#si les elément de la liste self.planete est différent de 0
            self.setheading(self.towards(self.gravity.planets[0]))# angle de la planète qui tend vers 
        self.a = self.acc()#
        self.velocity = self.velocity + distance * self.a#
        
        
class Soleil(Turtle):# classe planete
    
    def __init__(self, mass, x_pos, velocity, gravity, shape):# soi-meme,masse, position initaile x, rapidité, gravité, forme
        Turtle.__init__(self, shape=shape)#
        self.penup()# ne pas dessiner (ne pas faire de tracer)
        self.mass = mass#masse donné = masse
        self.setpos(x_pos)# position x donné= position
        self.velocity = velocity#rapidité donné= rapidité
        gravity.planets.append(self)# apelle de la fonction gravity 
        self.gravity = gravity#gravité donné=gravité
        self.resizemode("user")# l'utilisateur choisi la forme de de la tortue
        self.pendown()#dessiner (faire un tracer)
        
        
        
## create compound yellow/blue turtleshape for planets
def main():
    s = Turtle()#affecter turtle à s
    s.reset()# tout effacer
    s.getscreen().tracer(0,0)#
    s.ht() # cacher la tortue(la planète)
    s.pu() #ne pas tacer
    s.fd(6) # déplacer la planète de 6 sur l'axe des x
    s.lt(90) #touner à un angle de 90 degre
    s.begin_poly() #begining of the polygon, the current position is the first vecto of the polygon
    s.circle(5) #dessiner un cercle de rayon 5 
    s.end_poly() # fin de la figure
    #creates m1, creats a semi circle  
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(5)
    s.end_poly()
    #creates m2, uses the specs from the last recorded poly ^
    #m2 = s.get_poly()
    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"green")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)
    ## setup gravitational system
    gs = Gravity()# utilise la classe gravity et en l'affectantà gs
    sun = Soleil(1000000, Vec(0,0), Vec(0,0), gs, "circle") #utilsation de la classe planet avec les paramètres 
    sun.color("yellow")#changer la couleur
    sun.shapesize(5)# taille de la boule
    sun.pu()#ne fait pas de tracer
    earth = Planet(12500, Vec(215,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    earth.pencolor("green")#changer la couleur
    earth.shapesize(2)# taille de la boule
    #moon = Planet(1, Vec(225,0), Vec(0,295),gs, 'planet')#utilsation de la classe planet avec les paramètres 
    #moon.pencolor('blue')#changer la couleur
    #moon.shapesize(1)# taille de la boule
    #mars = Planet(4000, Vec(327,0), Vec(150,0), gs, "planet")#utilsation de la classe planet avec les paramètres 
    #mars.pencolor('red')#changer la couleur
    #mars.shapesize(2)# taille de la boule
    #jupiter = Planet(750, Vec(430,0), Vec(0,100), gs, "planet")#utilsation de la classe planet avec les paramètres 
    #jupiter.pencolor('purple')#changer la couleur
    #jupiter.shapesize(3)# taille de la boule
 #   p5 = Planet (mass, vec(x,y), vec(), gravity, shape)
 #   p6 = (name, radius), mass, colour, distance, x velocity, y velocity
    gs.init()#inclure gs dans init
    gs.start()#inclure gs dans start
#   s.onclick(pause)
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
    
