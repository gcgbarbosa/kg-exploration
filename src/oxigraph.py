"""
testing
"""

from pyoxigraph import RdfFormat, Store
import time

store = Store()


f = open("dump.rdf", "rb")

store.bulk_load(f, format=RdfFormat.TURTLE)

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

# print(q)

start = time.perf_counter()
result = store.query(q)

print(result)

for binding in result:
    print(binding)

# ex = NamedNode("http://example/")
# schema_name = NamedNode("http://schema.org/name")
# store.add(Quad(ex, schema_name, Literal("example")))
#
# result = store.query("SELECT ?name WHERE { <http://example/> <http://schema.org/name> ?name }")
#
#
# for binding in result:
#     print(binding["name"].value)
#

end = time.perf_counter()
elapsed_ms = (end - start) * 1000  # convert seconds → milliseconds

print(f"Elapsed time: {elapsed_ms:.3f} ms")
