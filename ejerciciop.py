import codecs
import json
archivo = codecs.open("datos.txt", "r")
lin = archivo.readlines()

lin_dicc = [json.loads(l) for l in lin]
# Se filtran las posciiones de los jugadores que tengan mas de 3 goles
filt1 =  list(filter(lambda x: list(x.items())[1][1] > 3, lin_dicc))
# Se filtran los jugadores de paises
filt2 = list(filter(lambda x: list(x.items())[0][1] == "Nigeria", lin_dicc))
#Se extraen los conceptos de la posicion de los valores max y min
col3 = list(map(lambda x: list(x.items())[2][1], lin_dicc))
# Se extraen los valores max y min 
filt3 = list(filter(lambda x: list(x.items())[2][1]==max(col3), lin_dicc))
filt4 = list(filter(lambda x: list(x.items())[2][1]==min(col3), lin_dicc))
# Se imprimen
print(filt1)
print(filt2)
print(list(filt3))
print(list(filt4))