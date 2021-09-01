"""
________WHAT's NEW____________
  >>>created particle flowers for realistic touch
  >>>created custom fill and stroke method used for drawing patterns with objects [flowers]
 
  created by VISHNU VS , 1st YEAR
  all rights reserved
"""
#2D is set by default
_3D = False  #Toggle this to True to view like firstperson







#USED TO DRAW CIRCLES AND ARCS USING FLOWERS     
def Petal_Stroke_Circle(flower="ROSE" , r=50 , joints=10 , angle=36 , size = 1 ,fill="white", stroke="grey"):
    shape = Flower(type=flower ,fill=fill , stroke=stroke ) | scale(size) | translate(x=r) | repeat(int(joints) , rotate(angle))
    return shape 

# USED TO DRAW SQUARE STROKES USING FLOWERS    
def Petal_Stroke_Square(flower_type="ROSE" , columns=2 , size = 1 , width=50 , fill="white", stroke="grey"):
    shape = flower_lines(flower=flower_type , size = size,  width=width ,fill=fill, stroke=stroke, divisions=columns)
    shape1 =shape | rotate(90) | repeat(2 , translate(x=0 , y=width))
    shape2 =shape1 | rotate(-90) | translate(y=width)
    return combine([shape , shape1 , shape2]) | translate(x=-width/2 , y=-width/2) 
    
def Petal_Fill(flower_type="JAMANTHI" , side=50 , petal_fill="yellow" , petal_stroke="orange", columns=5):
    width = side
    d = width/columns
    xstart = width/2 + d/2
    ystart = width/2 + d/2
    shapes = []
    for i in range(columns):
        for j in range(columns):
            x = -xstart + d*j
            y = ystart - d*i
            shape = Flower(fill=petal_fill , stroke=petal_stroke )|rotate(random(0,360)) | translate(x=random(x-1 , x+1), y=random(y-1, y+1))
            shapes.append(shape)
    return combine(shapes)

def flower_lines(flower="ROSE" ,fill="yellow" , size = 1 , stroke="orange", width=50 ,  divisions=5):
        dw = width/(divisions*size)
        shapes = []
        for i in range(int(divisions+1)):
            x = dw*i
            shape = Flower(type=type , fill=fill , stroke=stroke ) |  rotate(random(0,360))  | translate(x=x,y=0) | scale(size)
            shapes.append(shape)
        return combine(shapes) 
            
 
#CUSTOM POOGRID 
def custom_pooGrid(type="JAMANTHI" , size=1,  fill="white", stroke="grey"):
    c = Petal_Stroke_Square(flower_type="ROSE" , columns=4 , size = size , width=20 , fill=fill, stroke=stroke)
    c1 = Flower(type=type ,size=0.6, fill=fill , stroke=stroke) | scale(size)
    shape = c  + c1
    return shape | rotate(45)
            

#USED TO GET APPROPRIATE FLOWER FOR POOKKALAM
def Flower(type="ROSE" , fill="white" , stroke="lightgrey"):
    if type=="ROSE":
        return Rose(fill=fill , stroke=stroke)
    elif type == "JASMINE":
        return Jasmine(fill=fill , stroke=stroke)
    else:
        return Jamanthi(fill=fill , stroke=stroke)



#ROSE
def Rose(fill="tomato" , stroke="red"):
        c1 = ellipse(w=15, h=10, fill=fill , stroke=stroke) | repeat(10 , rotate(50) | scale(0.90))
        return (c1)
        
#JASMINE
def Jasmine(fill="white" , stroke="lightgrey"):
    c1 = ellipse(w=15, h=5 , fill=fill , stroke=stroke) | translate(x=10) | repeat(10 , rotate(36))
    c2 = circle(r=3 , fill="yellow", stroke="orange")
    return c1 + c2
    
#JAMANTHI
def Jamanthi(fill="#ffee00" , stroke="#f0b400"):
    c1 = ellipse(w=8, h=3 , fill=fill , stroke=stroke) | translate(x=5) | repeat(10 , rotate(36))
    c2 = c1 | scale(0.9) | rotate(15)
    c3 = c2 | scale(0.6) | rotate(15)
    shape = c1 + c2 + c3 
    return shape | rotate(random(0,360))







#FILLS A COONTAINER WITH FLOWERS-SQUARE
def Petal_Fill(flower_type , side , petal_fill , petal_stroke , columns):
    width = side
    d = int(width/columns)
    xstart = int(width/2)- d/2
    ystart = int(width/2 - d/2)
    shapes = []
    for i in range(columns):
        for j in range(columns):
            x = (-xstart) + int(d*j)
            y = ystart - int(d*i)
            shape = Flower(type=flower_type , fill=petal_fill , stroke=petal_stroke )|rotate(random(0,360))  | translate(x=random(x-1 , x+1), y=random(y-1, y+1))
            shapes.append(shape)
    return combine(shapes)
    


def petals(pw=10 , ph=5 , p_fill="#f7df00" , p_stroke="orange"):
    e1 = ellipse(w=pw , h=ph, x=pw/2 , fill=p_fill , stroke=p_stroke )
    e2 = e1 | repeat(10 , rotate(36))
    return e1+e2



#TEST PROCESS POOKKALAM
def getOuterPookkalam():
        #0UTER STRUCTURE
        c1   = Petal_Stroke_Circle(flower="JAMANTHI" , r=140 , joints=7 , angle=2 , size = 0.6 ,fill="yellow", stroke="orange") | rotate(0)|repeat(6 , rotate(60))
        c1_1 = Petal_Stroke_Circle(flower="JAMANTHI" , r=140 , joints=7, angle=2 , size = 0.6 ,fill="tomato", stroke="red") | rotate(30)|repeat(6 , rotate(60))
        c1_2 = Petal_Stroke_Circle(flower="JAMANTHI" , r=140 , joints=7 , angle=2 , size = 0.6 ,fill="white", stroke="lightgrey") | rotate(15)|repeat(6 , rotate(60))
        c1_3 = Petal_Stroke_Circle(flower="JAMANTHI" , r=140 , joints=7 , angle=2 , size = 0.6 ,fill="#07ad23", stroke="#015c10") | rotate(-15)|repeat(6 , rotate(60))
        b   = Petal_Stroke_Circle(flower="JASMINE" , r=150 , joints=20 , angle=20 , size = 0.3 ,fill="white", stroke="grey") |repeat(2, rotate(15))
        outer0 = c1 + c1_1 + c1_2 + c1_3  | rotate(5) | repeat(5 , rotate(15) | scale(0.95))
        outer0 += b
        outerpookkalam = outer0
        return outerpookkalam
    
def getInnerPookkalam():
    c1 = Petal_Stroke_Circle(flower="JAMANTHI" , r=47, joints=9 , angle=7 , size = 0.5,fill="#07ad23", stroke="#017815") | rotate(12)|repeat(6 , rotate(60))
    innerPookkalam =  c1 
    return innerPookkalam 

#3D KADHAKALI
#eyes and eyebrows
def greenface():
    face= ellipse(w=90 , h=120 , fill="#208016" , stroke="#208016" ) | translate(x=10 , y=-10)
    face1 = ellipse(w = 25 , h=50 , fill="#208016" , stroke="#208016" ) | rotate(-10) | translate(x=-20 , y=20)
    face2 = ellipse(w = 30 , h=65 , fill="#208016" , stroke="#208016" ) | rotate(18) | translate(x=-18 , y=-33)
    face3 = ellipse(w = 60 , h=75 , fill="#208016" , stroke="#208016" ) | rotate(-55) |translate(x=19 , y=-35)
    face4 = ellipse(w = 60 , h=75 , fill="#208016" , stroke="#208016" ) |  rotate(-5) |translate(x=5 ,y=-35)
    return (face + face1 + face2 + face3 + face4) | rotate(-2)

#eyebrow
def eyebrow():
    e1 = ellipse(w=35 , h=7 , fill="black") | rotate(28) | translate(x=14 , y=16)
    e2 = rectangle(w=12 , h=7 , fill="black") | rotate(-23) | translate(x=33 , y=19) 
    e3 = ellipse(w=20 , h=5 , fill="black") | rotate(30) | translate(x=41 , y=20) 
    e4 = ellipse(w=20 , h=5 , fill="black") | translate(x=10) | rotate(4) | translate(x=35 , y=15)
    eR = e1 + e2 + e3 + e4
    eL = eR |rotate(-11) | translate(x=18 , y=2) | scale(x=-0.6 , y=1)
    return eR + eL

def lips():
    e1 = ellipse(w=16 , h=4 , fill="#b0232a" , stroke="#b0232a") | translate(y=-49)
    e2 = ellipse(w=30 , h=5 , fill="#b0232a" , stroke="#b0232a") | translate(y=-44)
    e3 = e2 |translate(y=-4) | scale(x=0.8) | rotate(10) 
    e4 = ellipse(w=9 , h=10 , fill="#b0232a" , stroke="#b0232a") | translate(x=20 , y=-45)
    e5 = ellipse(w=7 , h=10 , fill="#b0232a" , stroke="#b0232a") | translate(x=-18 , y=-45)
    e6 = e2 | rotate(10)| translate(x=-3 , y=-4) | scale(x=-1 , y=1)
    l1 = line(x1=-2 , y1=-45 , x2=13 , y2=-46 , stroke="#a3020a")
    l1_1 = line(x1=-15 , y1=-45 , x2=10 , y2=-46 , stroke="#a3020a")
    l2= line(x1=5 , y1=-47 , x2=10 , y2=-47 , stroke="#a3020a") | rotate(10) 
    lipcorr = ellipse(w=5 , h=7 , fill="#208016" , stroke="#208016") | translate(x=-1 , y=-39)
    lips = e1 + e2 + e3 +  e4 + e5 + e6 + l1_1 + l1 + l2 + lipcorr
    return lips | translate(x=-5)

#jawmask
def jawmask():
    #RIGHT
    jr1 = ellipse(w=130 , h=75 , fill="#d5e6d7" , stroke="#d5e6d7" ) | rotate(3) | translate(x=25 , y=-40)
    jr = (jr1) 
    #LEFT
    jl1 = ellipse(w=130 , h=65 , fill="#d5e6d7" , stroke="#d5e6d7" ) | translate(x=5 , y=-45)
    jl = (jl1)
    #DARK LAYER
    jDark = ellipse(w=110 , h=55 , fill="#b5c9b7" , stroke="#b5c9b7" )  |translate(x=12 , y=-45)
    j = jl + jr + jDark
    return combine([j , greenface()])


#eyebrow
def eyeline():
    e1 = ellipse(w=40 , h=20 , fill="black" , stroke="black" ) | translate(x=20)| rotate(10)
    e2 = ellipse(w=40 , h=25 , fill="black" , stroke="black" ) | translate(x=33) |rotate(-10) | scale(-0.8)
    e3 = ellipse(w=45 , h=17  , fill="black") | rotate(25) | translate(x=30 , y=5)
    return (e1+e2+e3) | translate(y=-5) | scale(x=1)

def eyes():
    e1 = ellipse(w=20 , h=8 , fill="white" , stroke="white" ) | rotate(5) | translate(x=15 , y=-3)
    e2 = e1 |rotate(5) | translate(x=10 ) | scale(x=-0.9, y=0.9)
    eballR = ellipse(w=8 , h=10 , fill="black") | translate(x=20, y=-1)
    eyeR = e1 + eballR
    eballL = ellipse(w=8 , h=10 , fill="black") | translate(x=-19 , y=-1)
    return eyeR + e2 + eballL

def nose():
    #side
    e1b = ellipse(w=4, h=8, fill="black") | translate(x=1 , y=-26)
    e1g = ellipse(w=4 , h=8 , fill="#208016" , stroke="#208016") | translate(y=-25)
    n1s = e1b + e1g | rotate(3)
    n2s = n1s | translate(x=12) | scale(x=-1 , y=1)
    #hole
    h1b = ellipse(w=6, h=2, fill="black")| rotate(6) | translate(x=-2 , y=-29) 
    wrinkle= line(x1=8 , y1=-25 , x2=15 , y2=-36 , stroke="#154707" )
    nose = n1s + n2s + h1b + wrinkle
    return nose

def kuri():
    s1 = rectangle(w=25 , h=20 , fill="#f7ff03" , stroke="#f7ff03")
    s2 = s1 | rotate(45) | translate(y=-12) | scale(0.83)
    r1 = ellipse(w=6 , h=10, fill="#e3000b" , stroke="black") |  translate(x=-2)
    kuri = s1+s2 + r1
    kuri = kuri |rotate(1)| translate(x=-2 , y=39)
    return kuri
    
def earpiece():
    e1 = ellipse(w=20 , h=40 , fill="yellow" , stroke="#9c3f02" )| repeat(3 , scale(0.8)) | rotate(2)| translate(x=-45) 
    e2 = ellipse(w=30 , h=50 , fill="yellow" , stroke="#9c3f02" )| repeat(3 , scale(0.8)) | rotate(2)| translate(x=55) 
    e3 = ellipse(w=15 , h=30 , fill="yellow" , stroke="#9c3f02" )| repeat(3 , scale(0.8)) | rotate(2)| translate(x=-45 , y=-20) 
    e4 = ellipse(w=25 , h=40 , fill="yellow" , stroke="#9c3f02" )| repeat(3 , scale(0.8)) | rotate(2)| translate(x=55 , y=-20) 
    
    return  e3 + e4 + e1 + e2 



def crown():
    frontA = ellipse(w=100 , h=120 , fill="#e00d26" , stroke="orange" ) |rotate(-3) | translate(x=13 , y=10)| repeat(15 , scale(0.95))
    frontB = ellipse(w=100 , h=120 , fill="orange" , stroke="yellow" ) |rotate(-3) | translate(x=19 , y=20)
    frontC = ellipse(w=100 , h=120 , fill="yellow" , stroke="orange" )|rotate(-3) | translate(x=23 , y=30)| repeat(15 , scale(0.97))
    plate = ellipse(w=180, h=180 , fill="yellow" , stroke="#9c3f02" ) | translate(x=35 , y=35) | repeat(20 , scale(0.98))
    plate_design = circle(r=20 , fill=color(r=240, g=197, b=5 , a=0.7))
    des1 = ellipse(w=6 , h=8, fill=color(r=255 , g=85 , b=0 , a=0.8) , stroke="grey")|translate(x=70)|repeat(10 , rotate(36)) | translate(x=30 , y=40)
    plate= plate + plate_design  | scale(x=0.9)
    plate = plate + des1
    return plate + frontC + frontB + frontA 
    
    
def getKadhakali():
    return combine([crown(),jawmask(),eyeline() , eyebrow() , lips() , eyes(), nose() , kuri() , earpiece()])



#HILLS
def hills(color="#9dd4b6"):
    maxwidth = 200
    maxheight = 20
    p0 = point(x=-maxwidth, y=0)
    p1 =  point(x=-maxwidth, y=maxheight)
    p2 = point(x=100,y=0)
    p3 = point(x=maxwidth , y=maxheight-10)
    p4 = point(x=maxwidth ,y= 0)
    poly = polygon([p0,p1,p2,p3,p4] , fill=color , stroke="none")
    return poly




#HOME
def house( w=0 , h=0):
    roof_stack_width=10
    roof_top_h = 20
    roof_top_w= (2*roof_stack_width)
    def roof():
        p1=point(x=-w/2 , y=0)
        p2=point(x=w/2 , y=0)
        p3=point(x=(w/2)-roof_stack_width , y=h)
        p4=point(x=(-w/2)+roof_stack_width , y=h)
        return polygon([p1,p2,p3,p4], fill="#a67341" , stroke="none")
    def walls():
        wall = rectangle(w=(w-roof_top_w) , h=h , x=0 , y=0 , fill="#f7f5f0" , stroke="none")
        return wall
    roofing = roof() | translate(x=0 , y=h/2)
    wall = walls() 
    rect = rectangle(w=5 ,h=10,fill="#a67341" , stroke="none") 
    return roofing + wall + rect

def home():
    home_floor1 = house(w=200 , h=15)
    home_floor2 = house(w=150 , h=15) | translate(y=30)
    return home_floor1 + home_floor2





#ONATHAPPPAN GROUP
def onathappan(height): #>>>HELPER
        p1 = point(x=-10 , y=2)
        p2 = point(x=0 , y=height)
        p3 = point(x=5 , y=0)
        poly1 = polygon([p1,p2,p3] , fill="#964100" , stroke="#964100") | rotate(-2)
        p1 = point(x=5 , y=0)
        p2 = point(x=14 , y=5)
        p3 = point(x=0 , y=height)
        poly2 = polygon([p1,p2,p3] , fill="#e36402" , stroke="#e36402") | rotate(-2)
        poly = poly1 + poly2
        return poly

def appan_group():
    appan2 = onathappan(75) | translate(x=-10)
    appan1 = onathappan(100) | translate(x=5 , y=5)
    appan3 = onathappan(80) | translate(x=20)
    return appan1+appan2+appan3





def p(x,y):
    return point(x=x,y=y)
    

def Vallom():
    heads = circle(r=2 ,x=30 , y=18 ,fill="black") | repeat(8 , scale(0.9) | translate(25))
    body = ellipse(h=10 , w=3 ,x=30 , y=15 ,fill="#e8dec1") | repeat(8 , scale(0.9) | translate(25))
    sticks = line(x2=40 , y2=-5 ,x1=25 , y1=25 ,fill="#e8dec1") | repeat(8 , scale(0.9) | translate(25))
    poly = polygon([ 
                     p(0,25),
                     p(5 , 10),
                     p(8 , 5),
                     p(13 , 0),
                     p(18 , -3),
                     p(25 , -5),
                     p(150 , 0),
                     p(150 , 2),
                     p(20 , 10)
                   ] , fill="#615b48" , stroke="#615b48")
    return poly + body + heads + sticks



#COMPOSING
kadhak = getKadhakali() | translate(x=-23 , y=-20) | scale(0.39)



def  innerkalam():
    cowdung_base = circle(r=130 , fill=color(r=19, g=43, b=23 , a=1) ,  stroke="#00540e")
    cowdung = Flower(type="ROSE" , fill=color(r=19, g=43, b=23 , a=0.8) , stroke="#00540e") | translate(108) | repeat(40 , rotate(10))
    c0 = Flower(type="ROSE" , fill=color(r=201, g=0, b=47 , a=0.8) , stroke="#750126")| scale(1.05) | translate(60) | repeat(40 , rotate(10))
    c1 = Flower(type="ROSE" , fill=color(r=245, g=17, b=89 , a=0.8) , stroke="#ad0037") | scale(1.05)| translate(70) | repeat(40 , rotate(10))
    c1_1 = Flower(type="ROSE" , fill=color(r=255, g=154, b=3 , a=0.8) , stroke="#f51616")| scale(1.05) | translate(80) | rotate(5) | repeat(40 , rotate(10))
    c2 = Flower(type="ROSE" , fill=color(r=255, g=121, b=3 , a=0.7) , stroke=color(r=250, g=185, b=5 , a=0.8)) | scale(1.05)| translate(90) | repeat(40 , rotate(10))
    c2_1 = Flower(type="ROSE" , fill=color(r=250, g=176, b=5 , a=0.6) , stroke=color(r=255, g=230, b=0 , a=0.8)) | scale(1.05) | translate(98) | rotate(5) | repeat(40 , rotate(20))
    c0_1 = Petal_Stroke_Circle(flower="JAMANTHI" , r=40 , joints=10 , angle=10 , size = 0.6 , fill=color(r=73 ,g=4, b=112 , a=0.6) , stroke="lightgrey") | repeat(4 , rotate(90)) 
    c0_0 = Petal_Stroke_Circle(flower="JAMANTHI" , r=50 , joints=11 , angle=36 , size = 0.3 ,fill="white", stroke="lightgrey") | translate(25) | repeat(10 , rotate(36))
    return cowdung_base + cowdung + c0 + c0_1 + c1 + c1_1 + c2 + c0_0 + c2_1




def lamp():
    circ = circle(r=20 , fill="#944710" , stroke="none")
    re = rectangle(w=35 , h=35 , fill="#944710" , stroke="none") | rotate(45)
    circ1 = circle(r=15 , fill="#4a2406" , stroke="none")
    idinjil = circ + re + circ1
    fire1 = circle(r=4 , fill=color(r=255,g=153,b=0, a=0.6) , stroke=color(r=255,g=153,b=0, a=0.6))
    fire2 = circle(r=2 , fill=color(r=255,g=221,b=0, a=0.6) , stroke=color(r=255,g=221,b=0, a=0.6))
    fire1 += fire2 | translate(x=3)
    fire1 = fire1 | translate(x=25) | repeat(4 , rotate(90))
    return idinjil + fire1


if(_3D==False):
    bg = Petal_Fill(flower_type="ROSE" , side=150 , petal_fill="green" , petal_stroke="grey", columns=15)
    lamps = lamp() | scale(0.5) | translate(x=130 , y=130) | repeat(4 , rotate(90))
    pookkalam =  innerkalam() + getOuterPookkalam()+getInnerPookkalam()+kadhak
    show(bg+ pookkalam + lamps)
else:
    pookkalam = innerkalam() + getOuterPookkalam() + getInnerPookkalam()+kadhak | translate(y=-250)|scale(y=0.3)
    hill = hills(color="#5bb384") | scale(x=-1 , y=1)
    show(hills() + hill)
    show(home())
    appangrp = appan_group() | translate(x=0 , y=-135) | scale(0.6)
    show(pookkalam)
    show(appangrp)

#show(kadhak)