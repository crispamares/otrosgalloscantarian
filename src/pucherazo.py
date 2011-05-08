from random import randint

class Pucherazo:
    # Distribuye los votos en blanco entre los partidos seleccionados 
    # por el usuario de forma aleatoria
    def darPucherazo(self,votos,blancos,caciques):
        # Asegurarse de que existe el candidato en la provincia
        toRemove = []
        for cacique in caciques:
            if cacique not in votos:
                toRemove += [cacique]
        for cacique in toRemove:
            caciques.remove(cacique)

        # Si no se pasaron caciques o no existen los solicitados
        # todos los partidos votados se convierten en caciques
        if caciques == [''] or caciques == []:
            caciques = votos.keys()

        numCaciques = len(caciques) - 1 # corregir indices en randint
        for i in range(0,blancos):
            cacique = caciques[randint(0,numCaciques)]
            votos[cacique] += 1
        return votos
