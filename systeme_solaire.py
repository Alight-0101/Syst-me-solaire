# -*- coding: utf-8 -*-

from tkinter import*
from math import*
 
fenetre = Tk()
fenetre.title("le mouvement d'une planète autour de son étoile")

def mouvement():
    global t
    t=t+0.2#temps
    w1=0.25#poids
    w2=0.3
    dessin.coords(etoile,(xc-rs)+R*sin(t*pi),(yc-rs)+R*cos(t*pi),(xc+rs)+R*sin(t*pi),(yc+rs)+R*cos(t*pi))#mvt de l'etoile
    dessin.create_oval((xc-rs)+R*sin(t*pi)+rs-0.01,(yc-rs)+R*cos(t*pi)+rs-0.01,(xc-rs)+R*sin(t*pi)+rs+0.01,(yc-rs)+R*cos(t*pi)+rs+0.01,fill='blue')#trace laissee par le jaune et  le bleu
    dessin.coords(planete,(xc-rp)+R1*sin(t*w1*pi),(yc-rp)+R1*cos(t*w1*pi),(xc+rp)+R1*sin(t*w1*pi),(yc+rp)+R1*cos(t*w1*pi))#mvt du rouge
    dessin.create_oval((xc-rp)+R1*sin(t*0.25*pi)+rp-0.01,(yc-rp)+R1*cos(t*0.25*pi)+rp-0.01,(xc-rp)+R1*sin(t*0.25*pi)+rp+0.1,(yc-rp)+R1*cos(t*0.25*pi)+rp+0.1,fill='green')#trace du rouge
    dessin.coords(lune,(xc-rlune)+R2*sin(t*w2*pi),(yc-rp)+R2*cos(t*w2*pi),(xc+rlune)+ R2*sin(t*w2*pi),(yc+rlune)+R2*cos(t*w2*pi))#mvt du bleu

    fenetre.after(90,mouvement)#vitesse de defilement

global xs,ys,rs,xp,yp,rp,xc,yc,rc,R,t,xlune,ylune,rlune
t=0
#coordonnées du milieu de centre de masse
xc=500
yc=500
rc=5 #son rayon
#coordonées du centre de l'étoile
xs=450
ys=450
rs=20 #son rayon
#coordonnées de la planète
xp=300
yp=300
rp=20


#coordonnées de lune
xlune=450
ylune=450
rlune=20



# Rayon de la trajectoire de la planete autour de son étoile
R= sqrt((xs-xc)**2+(ys-yc)**2)

R1=sqrt((xp-xc)**2+(yp-yc)**2)

R2=sqrt((xlune-xc)**2+(ylune-yc)**2)

dessin = Canvas(fenetre, width=1000, height = 1000, bg="white", bd=8, relief="ridge")#width=largeur height=longueur bg=fond bd=le contour relief=la mise en avant de la fenetre testez avec raised
dessin.pack()
centre=dessin.create_oval(xc-rc,yc-rc,xc+rc,yc+rc,fill="black")#cree une boule noire
etoile=dessin.create_oval(xs-rs,ys-rs,xs+rs,ys+rs,fill="yellow")#cree une boule jaune
planete=dessin.create_oval(xp-rp,yp-rp,xp+rp,yp+rp,fill="red")#cree une boule rouge
lune=dessin.create_oval(xlune-rlune,ylune-rlune,xlune+rlune,ylune+rlune,fill="blue")#cree une boule bleu 
#si une des 3 lignes ci dessus disparait, il n'y a pas que la boule qui disparait. testez pour comprendre

mouvement()

fenetre.mainloop()
