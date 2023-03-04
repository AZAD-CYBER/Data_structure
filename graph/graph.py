'''
A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges

'''
# We can present this graph in a python program as below −

# Create the dictionary with graph elements
"""graph={

    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["a","d"],
    "d":["e"],
    "e":["d"]

}

print(graph)"""

# Display graph vertices #
"""
class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    
    #get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())
#create the dictionary with graph elements
graph_elements={
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["d"]
}  

g=graph(graph_elements)
print(g.getVertices())"""

# Display graph edges #
"""
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    
    def edges(self):
        edgename=[]
        for v in self.gdict:
            for nv in self.gdict[v]:
                if {nv,v} not in edgename:
                    edgename.append({v,nv})
        return edgename

# Create the dictionary with graph elements
graph_elements = { 

   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
print(g.edges())"""

#adding a vertex

"""class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    
    def getVertices(self):
        return list(self.gdict.keys())
    
    def addVertex(self,v):
        if v not in self.gdict:
            self.gdict[v]=[]

graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
g.addVertex("f")
print(g.getVertices())"""

#Adding an edge

class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
   def edges(self):
      return self.findedges()
# Add the new edge
   def AddEdge(self, edge):
      edge = set(edge)
      (vrtx1, vrtx2) = tuple(edge)
      if vrtx1 in self.gdict:
         self.gdict[vrtx1].append(vrtx2)
      else:
         self.gdict[vrtx1] = [vrtx2]
# List the edge names
   def findedges(self):
      edgename = []
      for vrtx in self.gdict:
         for nxtvrtx in self.gdict[vrtx]:
            if {nxtvrtx, vrtx} not in edgename:
               edgename.append({vrtx, nxtvrtx})
      return edgename
# Create the dictionary with graph elements
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.edges(),"\n", g.gdict)
