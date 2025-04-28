from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMapFermate = {}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def buildGraph(self):
        #aggiungiamo i nodi
        self._grafo.add_nodes_from(self._fermate)
        self.addEdges3()

    def addEdges1(self):
        """Aggiungo gli archi ciclando con doppio ciclo sui nodi
        e testando se per ogni coppia esiste una connessione"""
        for u in self._fermate:
            for v in self._fermate:
                if DAO.hasConnessione(u,v):
                    self._grafo.add_edge(u,v)
                    print("Aggiungo arco fra u e v", u, "e", v)


    def addEdges2(self):
        """Ciclo solo una volta e faccio una query per trovare
        tutti i vicini"""
        for u in self._fermate:
            for con in DAO.getVicini(u):
                v = self._idMapFermate[con.id_stazA]
                self._grafo.add_edge(u,v)

    def addEdges3(self):
        allEdges = DAO.getAllEdges()
        for e in allEdges:
            u = self._idMapFermate[e.id_stazP]
            v = self._idMapFermate[e.id_stazA]
            self._grafo.add_edge(u,v)


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    @property
    def fermate(self):
        return self._fermate