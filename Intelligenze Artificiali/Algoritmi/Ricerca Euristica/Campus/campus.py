from math import sqrt

class Campus:

    __grafo_degli_stati = {

        "Bus Stop": ["Library"],
        "Library": ["Bus Stop", "Car Park", "Student Center"],
        "Car Park": ["Library", "Maths Building", "Store"],
        "Maths Building": ["Car Park", "Canteen"],
        "Student Center": ["Library", "Store" , "Theater"],
        "Store": ["Student Center", "Car Park", "Canteen", "Sports Center"],
        "Canteen": ["Maths Building", "Store", "AI Lab"],
        "AI Lab": ["Canteen"],
        "Theater": ["Student Center", "Sports Center"],
        "Sports Center": ["Theater", "Store"]

    }

    __coordinate = {

        "Bus Stop": [2, 8],
        "Library": [4, 8],
        "Car Park": [1, 4],
        "Maths Building": [4, 1],
        "Student Center": [6, 8],
        "Store": [6, 4],
        "Canteen": [6, 1],
        "AI Lab": [6, 0],
        "Theater": [7, 7],
        "Sports Center": [7, 5]

    }

    def __init__(self, stato_iniziale: str):
        self.stato_iniziale = stato_iniziale

    def ottieni_stati_successori(self, stato: str):
        return self.__grafo_degli_stati[stato]
    
    def ottieni_valore_euristico(self, stato: str):
        x_stato, y_stato = self.__coordinate[stato]
        x_obiettivo, y_obiettivo = self.__coordinate['AI Lab']

        diffX = (x_obiettivo - x_stato) ** 2
        diffY = (y_obiettivo - y_stato) ** 2

        return sqrt(diffX + diffY)
    
    def ottieni_distanza(self, stato1: str, stato2: str):
        x_stato1, y_stato1 = self.__coordinate[stato1]
        x_stato2, y_stato2 = self.__coordinate[stato2]

        diffX = (x_stato2 - x_stato1) ** 2
        diffY = (y_stato2 - y_stato1) ** 2

        return sqrt(diffX + diffY)
    
    def verifica_stato_obiettivo(self, stato: str):
        return stato == 'AI Lab'