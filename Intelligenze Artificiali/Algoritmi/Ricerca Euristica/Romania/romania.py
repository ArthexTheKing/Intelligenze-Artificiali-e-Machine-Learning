class Romania:

    __grafo_degli_stati = {

        'Arad': [['Sibiu', 140], ['Timisoara', 118], ['Zerind',  75]],
        'Bucarest': [['Fagaras', 211], ['Giurgiu', 90], ['Pitesti', 101], ['Urziceni', 85]],
        'Craiova': [['Drobeta', 120], ['Pitesti', 138], ['Rimnicu Vilcea', 146]],
        'Drobeta': [['Craiova', 120], ['Mehadia', 75]],
        'Eforie': [['Hirsova', 86]],
        'Fagaras': [['Bucarest', 211], ['Sibiu', 99]],
        'Giurgiu': [['Bucarest', 90]],
        'Hirsova': [['Eforie', 86], ['Urziceni', 98]],
        'Iasi': [['Neamt', 87], ['Vaslui', 92]],
        'Lugoj': [['Mehadia', 70], ['Timisoara', 111]],
        'Mehadia': [['Drobeta', 75], ['Lugoj', 70]],
        'Neamt': [['Iasi', 87]],
        'Oradea': [['Sibiu', 151], ['Zerind', 71]],
        'Pitesti': [['Bucarest', 101], ['Craiova', 138], ['Rimnicu Vilcea', 97]],
        'Rimnicu Vilcea': [['Craiova', 146], ['Pitesti', 97], ['Sibiu', 80]],
        'Sibiu': [['Arad', 140], ['Fagaras', 99], ['Oradea', 151], ['Rimnicu Vilcea', 80]],
        'Timisoara': [['Arad', 118], ['Lugoj', 111]],
        'Urziceni': [['Bucarest', 85], ['Hirsova', 98], ['Vaslui', 142]],
        'Vaslui': [['Iasi', 92], ['Urziceni', 142]],
        'Zerind': [['Arad', 75], ['Oradea', 71]]  

    }

    __funzione_euristica = {

        'Arad': 366,
        'Bucarest': 0,
        'Craiova': 160,
        'Drobeta': 242,
        'Eforie': 161,
        'Fagaras': 176,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 100,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374

    }

    def __init__(self, stato_iniziale):
        self.stato_iniziale = stato_iniziale

    def stati_generati(self, stato: str):
        return self.__grafo_degli_stati[stato]
    
    def valore_euristico(self, stato: str):
        return self.__funzione_euristica[stato]
    
    def verifica_stato_obiettivo(self, stato: str):
        return stato == 'Bucarest'