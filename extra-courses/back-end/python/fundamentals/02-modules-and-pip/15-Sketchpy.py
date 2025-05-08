#instalar biblioteca sketchpy
# pip install sketchpy
#Funciona melhor em versões do python 3.9 ou 3.10
#Recomendavel usar em uma VM (maquina virtual)

from sketchpy import library
object = library.rdj()
object.draw()

from sketchpy import library
object= library.tom_holland()
object.draw()

from sketchpy import library
object= library.ironman_ascii()
object.draw()