#%% Annotation
'''
Auction Revenues and Reported Usage: https://www.eea.europa.eu/data-and-maps/figures/auctioning-revenues-and-reported-usage
ETS_Database_v51_May23, 
EU emission trading system, deepcheck
Global Environmental Indicators, deepcheck
Greenhouse Gas emission, deepcheck

'''
#%%
from rdflib.namespace import DCTERMS
import rdflib

graph = rdflib.Graph()
graph.parse(".//Potential Dataset//dat-21-en.rdf", format="xml")

query = """
SELECT ?subject ?title
WHERE {
  ?subject dct:title ?title .
}
"""

for row in graph.query(query, initNs={'dct': DCTERMS}):
    print(f"Subject: {row.subject}, Title: {row.title}")
# %%
