#pookkalam
from joy import *

#outer circle
c2=circle(r=151,fill="#fc9802",stroke="none")
c1=circle(r=147,fill="#a60202",stroke="none")
show(c2,c1)

#outer design layer
rect1=rectangle(w=150,h=150,fill="#820a0a",stroke="none")|repeat(20,rotate(50))
rect2=rectangle(w=170,h=170,fill="#ce0606",stroke="none")|rotate(15)|repeat(20,rotate(50))
rect3=rectangle(w=190,h=190,fill="#fc9802",stroke="none")|repeat(20,rotate(50))
rect4=rectangle(w=210,h=210,fill="#fceb02",stroke="none")|rotate(15)|repeat(20,rotate(50))|scale(0.98)
show(rect4,rect3,rect2,rect1)

#middle layer
c1 =ellipse(w=190,h=30,fill="#fc9802",stroke="none")|repeat(8,rotate(50))
c2 =ellipse(w=190,h=30,fill="#fc9802",stroke="none")|repeat(9,rotate(40))
c3 =ellipse(w=190,h=30,fill="#fc9802",stroke="none")|repeat(100,rotate(10))
show(c3,c2,c1)

#inner circle
c4=circle(r=80,fill="orange",stroke="none")
c3=circle(r=70,fill="#EDA63D",stroke="none")
c2=circle(r=65,fill="#f2b707",stroke="none")
c1=circle(r=60,fill="#fac528",stroke="none")
show(c4,c3,c2,c1)

#inner circle
#kodi
k1=ellipse(x=-7,y=40,h=35,w=80,fill="#732304",stroke="none")| rotate(25)
k2=ellipse(x=-7,y=40,h=32,w=80,fill="#BE6A26",stroke="none")| rotate(25)
k3=ellipse(x=-7,y=40,h=25,w=80,fill="#732304",stroke="none")| rotate(25)
k4=ellipse(x=-7,y=40,h=22,w=80,fill="#663402",stroke="none")| rotate(25)
k5=ellipse(x=-7,y=40,h=15,w=80,fill="#732304",stroke="none")| rotate(25)
k6=ellipse(x=-7,y=40,h=12,w=80,fill="#311400",stroke="none")| rotate(25)
k=k1+k2+k3+k4+k5+k6
show(k)
l1=line(x1=-30,y1=30,x2=0,y2=-20,stroke_width=3,stroke="#311400")
l2=line(x1=-26,y1=27,x2=0,y2=-20,stroke_width=3,stroke="#663402")
show(l1,l2)
#kiridam
c1=circle(x=10,y=15,r=25,fill="#EAB431",stroke="#DF9739")
c2=circle(x=10,y=14,r=20,fill="#E49F0A",stroke="none")
c3=circle(x=10,y=10,r=15,fill="#DD890F",stroke="none")
show(c1,c2,c3)
p1=ellipse(w=30,h=15,x=10,y=10,fill="#FBDE47",stroke="none")
p2=ellipse(w=20,h=15,x=10,y=20,fill="#FBDE47",stroke="none")
p3=ellipse(w=10,h=10,x=10,y=30,fill="#FBDE47",stroke="none")
p4=ellipse(w=25,h=15,x=12,y=10,fill="#f2be00",stroke="none")
p5=ellipse(w=15,h=15,x=12,y=20,fill="#f2be00",stroke="none")
p6=ellipse(w=5,h=10,x=12,y=30,fill="#f2be00",stroke="none")
p=p1+p2+p3+p6+p5+p4
show(p)
#maveli
e1=ellipse(w=50,h=35,x=10,y=-40,fill="#EEAC82",stroke="#b06b04")
e2=ellipse(w=33,h=25,x=10,y=-20,fill="#EEAC82",stroke="#b06b04")
e3=ellipse(w=20,h=20,x=10,y=0,fill="#EEAC82",stroke="#b06b04")
e4=ellipse(w=23,h=25,x=14,y=-22,fill="#eda06f",stroke="none")
e5=ellipse(w=40,h=35,x=14,y=-40,fill="#eda06f",stroke="none")
show(e1,e5,e2,e4,e3)

#mund
s1=rectangle(w=50,h=20,x=10,y=-60,fill="#d68202",stroke="#ffd391")
s2=rectangle(w=40,h=20,x=5,y=-60,fill="#d68202",stroke="#ffd391")
show(s1,s2)
