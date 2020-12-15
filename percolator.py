
import random
from util import *

def getOppositeVertex(vertex,edge):
    if edge.x == vertex:
        return edge.y
    else:
        return edge.x

def getAttachedEdges(vertex, graph):
    edgesList = []
    for e in graph.E:
        if e.x == vertex:
            edgesList.append(x)
        elif e.y == vertex:
            edgesList.append(y)
    return edgesList


class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
# Should return a vertex `v` from graph.V where v.color == -1
def ChooseVertexToColor(graph, player):
    bestvertex = None
    maxdegreevertex = -100

    for vertex in graph.V:
        if vertex.color == -1:
            degreevertex = len(getEdges(graph, vertex))
            valid = False
            for edge in getEdges(graph, vertex):
                if getOtherVertex(edge, vertex).color == player or getOtherVertex(edge, vertex).color != -1:
                    degreevertex -= 1
                    if getOtherVertex(edge, vertex).color == player:
                        valid = True
            if degreevertex >= maxdegreevertex and valid == True:
                maxdegreevertex = degreevertex
                bestvertex = vertex
    if bestvertex == None:
        maxEdges = 0
        maxEdgeVertex = None
        for vertex in graph.V:
            if vertex.color == -1:
                if len(getEdges(graph, vertex)) >= maxEdges:
                    maxEdges = len(getEdges(graph, vertex))
                    maxEdgeVertex = vertex
        return maxEdgeVertex

    return bestvertex

# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
# Should return a vertex `v` from graph.V where v.color == player
def ChooseVertexToRemove(graph, player):
    bestvertex = None

    vertices = []
    for vertex in graph.V:
        if vertex.color == player:
            if getEdges(graph, vertex) == list(graph.E):
                return vertex
            opponentvertices = 0
            allyvertices = 0
            for edge in getEdges(graph, vertex):
                if getOtherVertex(edge, vertex).color != player:
                    opponentvertices += 1
                else:
                    allyvertices += 1

            vertices.append(opponentvertices - allyvertices)

    vertices.sort()

    if vertices[len(vertices) - 1] < 0:
        maxdifference = -10000000
        for vertex in graph.V:
            if vertex.color == player:
                if getEdges(graph, vertex) == list(graph.E):
                    return vertex
                opponentvertices = 0
                allyvertices = 0
                for edge in getEdges(graph, vertex):
                    if getOtherVertex(edge, vertex).color != player:
                        opponentvertices += 1
                    else:
                        allyvertices += 1

                if (opponentvertices - allyvertices) >= maxdifference:
                    maxdifference = opponentvertices - allyvertices
                    bestvertex = vertex

    else:
        maxdifference = 10000000
        for vertex in graph.V:
            if vertex.color == player:
                if getEdges(graph, vertex) == list(graph.E):
                    return vertex
                opponentvertices = 0
                allyvertices = 0
                for edge in getEdges(graph, vertex):
                    if getOtherVertex(edge, vertex).color != player:
                        opponentvertices += 1
                    else:
                        allyvertices += 1

                if (opponentvertices - allyvertices) < maxdifference and (opponentvertices - allyvertices) >= 0:
                    maxdifference = opponentvertices - allyvertices
                    bestvertex = vertex

    return bestvertex

# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()
