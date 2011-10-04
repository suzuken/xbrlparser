# /usr/bin/python
import logging

from rdflib import ConjunctiveGraph
from rdflib.graph import Graph
from rdflib.term import URIRef, Literal, BNode
from rdflib.namespace import Namespace, RDF

FOAF = Namespace("http://xmlns.com/foaf/0.1/")
DC = Namespace("http://purl.org/dc/elements/1.1/")

graph = ConjunctiveGraph()

john = BNode()
graph.add((john, RDF.type, FOAF['Person']))
graph.add((john, FOAF['nick'], Literal('john')))
graph.add((john, FOAF['name'], Literal('John Doe')))

for s, p, o in store:
    print s,p,o
