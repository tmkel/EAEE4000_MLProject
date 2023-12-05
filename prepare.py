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
import pandas as pd

my_cols = [str(i) for i in range(42)] # create some col names
a = pd.read_csv(r".\Potential Dataset\International Greenhouse Gas\env_air_gge.tsv\env_air_gge.tsv", 
                sep="\t|,"
                names=my_cols,
                engine="python")
b = pd.read_csv(r".\Potential Dataset\ETS_Database_v51_May23\ETS_Database_Jul23.csv", sep="\t")
# %%
c = pd.read_csv(r"Potential Dataset\icap-graph-data-17-10-2023 (1).csv", sep=";")
# %%
