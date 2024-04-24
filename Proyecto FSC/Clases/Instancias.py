from Clases.ClasesGenerales import *


portero1 = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'Max.png')
portero2 = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'ben.png')
portero3 = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'Ava.png')

Max = Portero("Max", portero1)
Ben = Portero("Ben", portero2)
Ava = Portero("Ava", portero3)


artillero1 = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'dan.png')
artillero2 = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'leo.png')
artillero3 = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'sam.png')

Dan = Artillero("Dan", artillero1)
leo = Artillero("Leo", artillero2)
sam = Artillero("Sam", artillero3)

Escudo_MIL = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'emil.png')
Escudo_JUV = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'ejuv.png')
Escudo_RIV = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'erp.png')

MIL = Equipo("Milan", Escudo_MIL, [], [], [])
JUV = Equipo("Juventus", Escudo_JUV, [], [], [])
RIV = Equipo("River Plate", Escudo_RIV, [], [], [])


