from turtle import Shape, Turtle, mainloop, Vec2D as Vec
from time import sleep

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()

class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a

## create compound yellow/blue turtleshape for planets

def main():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6,180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"orange")
    planetshape.addcomponent(m2,"blue")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)

    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec(0,0), Vec(0,0), gs, "circle")
    sun.color("yellow")
    sun.shapesize(1.8)
    sun.pu()
    
    mercure = Star(11500, Vec(100,0), Vec(0,195), gs, "planet")
    mercure.pencolor("green")
    mercure.shapesize(0.4)
    
    vénus = Star(11100, Vec(150,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    vénus.pencolor("pink")#changer la couleur
    vénus.shapesize(0.6)# taille de la boule
    
    earth = Star(12500, Vec(200,0), Vec(0,195), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)
    
    moon = Star(1, Vec(210,0), Vec(0,295), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)
    
    mars = Star(40000, Vec(320,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    mars.pencolor('red')#changer la couleur
    mars.shapesize(2)# taille de la boule
    
    jupiter = Star(75000, Vec(430,0), Vec(-50,300), gs, "planet")#utilsation de la classe planet avec les paramètres 
    jupiter.pencolor('purple')#changer la couleur
    jupiter.shapesize(3)# taille de la boule
    
    saturne  = Star(76500, Vec(500,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    saturne.pencolor("yellow")#changer la couleur
    saturne.shapesize(2)# taille de la boule
    
    uranus = Star(12500, Vec(570,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    uranus.pencolor("green")#changer la couleur
    uranus.shapesize(2)# taille de la boule
    
    neptune = Star(12500, Vec(650,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    neptune.pencolor("green")#changer la couleur
    neptune.shapesize(2)# taille de la boule
    
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print (msg)
    mainloop()

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
        for i in range(500):# boucle pour répéter 500 fois
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
        self.velocity = self.velocity + 0.5 * distance * self.a# permet de changer la rapidité
        
    def acc(self):
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
            self.setheading(self.towards(self.gravity.planets[0]))# angle de la planète qui tend vers la première valeur dans la liste self.planète
        self.a = self.acc()# fait bouger la planete en changant le vecteur initial 
        self.velocity = self.velocity + distance * self.a# vitesse qui change
        
        
        
def main():
    s = Turtle()#affecter turtle à s
    s.reset()# tout effacer
    s.getscreen().tracer(0,0)# forme de l'objet qui permet de faire une animation
    s.ht() # cacher la tortue(la planète)
    s.pu() #ne pas tacer
    s.fd(6) # déplacer la planète de 6 sur l'axe des x
    s.lt(90) #touner à un angle de 90 degre
    s.begin_poly() #begining of the polygon, the current position is the first vecto of the polygon
    s.circle(5) #dessiner un cercle de rayon 5 
    s.end_poly() # fin de la figure
    #création de m1, un demi cercle
    m1 = s.get_poly()# utilise le dernier polynome enregistré
    s.begin_poly()# début du poly(tracer)
    s.circle(5)#dessiner un cercle de rayon 5
    s.end_poly()#fin de la figure
    # création de m2 avec les même propriétés que m1 
    m2 = s.get_poly()# utilise le dernier polynome enregistré
    planetshape = Shape("compound")# forme de la planète 
    planetshape.addcomponent(m1,"green")# ajoute m1 et la couleur vert comme donnée
    s.getscreen().register_shape("planet", planetshape)#enregistre les données 
    s.getscreen().tracer(1,0)#forme de l'objet qui permet de faire une animation une fois
    
    gs = Gravity()# utilise la classe gravity et en l'affectantà gs
    sun = Soleil(1000000, Vec(0,0), Vec(0,0), gs, "circle") #utilsation de la classe planet avec les paramètres 
    sun.color("yellow")#changer la couleur
    sun.shapesize(5)# taille de la boule
    sun.pu()#ne fait pas de tracer
    
    mercure = Planet(12500, Vec(200,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    mercure.pencolor("orange")#changer la couleur
    mercure.shapesize(1)# taille de la boule
    
    vénus = Planet(12500, Vec(215,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    vénus.pencolor("pink")#changer la couleur
    vénus.shapesize(2)# taille de la boule
    
    earth = Planet(12500, Vec(215,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    earth.pencolor("green")#changer la couleur
    earth.shapesize(2)# taille de la boule
    
    moon = Planet(1, Vec(225,0), Vec(0,295),gs, 'planet')#utilsation de la classe planet avec les paramètres 
    moon.pencolor('blue')#changer la couleur
    moon.shapesize(1)# taille de la boule
    
    mars = Planet(4000, Vec(327,0), Vec(150,0), gs, "planet")#utilsation de la classe planet avec les paramètres 
    mars.pencolor('red')#changer la couleur
    mars.shapesize(2)# taille de la boule
    
    jupiter = Planet(750, Vec(430,0), Vec(0,100), gs, "planet")#utilsation de la classe planet avec les paramètres 
    jupiter.pencolor('purple')#changer la couleur
    jupiter.shapesize(3)# taille de la boule
    
    saturne  = Planet(12500, Vec(500,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    saturne.pencolor("yellow")#changer la couleur
    saturne.shapesize(2)# taille de la boule
    
    uranus = Planet(12500, Vec(550,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    uranus.pencolor("green")#changer la couleur
    uranus.shapesize(2)# taille de la boule
    
    neptune = Planet(12500, Vec(600,0), Vec(0,195), gs, "planet")#utilsation de la classe planet avec les paramètres 
    neptune.pencolor("green")#changer la couleur
    neptune.shapesize(2)# taille de la boule
 #   p5 = Planet (mass, vec(x,y), vec(pos,temps), gravity, shape)
 #   p6 = (name, radius), mass, colour, distance, x velocity, y velocity
    gs.init()#inclure gs dans init
    gs.start()#inclure gs dans start
    s.onclick(pause)# faire pause 
    return "Done!"# 

if __name__ == '__main__': 
    msg = main()#associé à msg la fonc main
    print(msg)#utiliser la fonction main
    mainloop()# reboucler 
