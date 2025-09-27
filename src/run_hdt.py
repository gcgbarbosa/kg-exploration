"""
HDT test

"""

from rdflib import Graph
from rdflib_hdt import HDTStore, optimize_sparql

import time

# Calling this function optimizes the RDFlib SPARQL engine for HDT documents
optimize_sparql()

graph = Graph(store=HDTStore("dump.hdt"))

q = (
    "PREFIX wikibase: <http://wikiba.se/ontology#> "
    "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "
    "SELECT ?property ?propertyLabel "
    "WHERE { "
    "  ?property a wikibase:Property . "
    '  OPTIONAL { ?property rdfs:label ?propertyLabel . FILTER(LANG(?propertyLabel) = "en") } '
    "} "
    "ORDER BY ?property "
    "LIMIT 100 "
)

start = time.perf_counter()

# You can execute SPARQL queries using the regular RDFlib API
qres = graph.query(q)

for row in qres:
    print(row)


end = time.perf_counter()
elapsed_ms = (end - start) * 1000  # convert seconds → milliseconds


print(f"Elapsed time: {elapsed_ms:.3f} ms")
