"""
qlever test
"""

from SPARQLWrapper import SPARQLWrapper, JSON

import time

endpoint = "http://localhost:7041"


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

sparql = SPARQLWrapper(endpoint)


start = time.perf_counter()

sparql.setQuery(q)

sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result)

end = time.perf_counter()
elapsed_ms = (end - start) * 1000  # convert seconds → milliseconds

print(f"Elapsed time: {elapsed_ms:.3f} ms")
