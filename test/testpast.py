from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
"http://localhost:8010/sparql"
)
sparql.setReturnFormat(JSON)

# gets the first 3 geological ages
# from a Geological Timescale database,
# via a SPARQL endpoint
sparql.setQuery("""
PREFIX blcu: <http://www.blcu.edu.cn/qinmeiping/ontologies/xuewei/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?label ?pinyin ?anatomy ?location ?mainIndication ?method
WHERE {
  ?acupuncturePoint a blcu:AcupuncturePoint ;
                    rdfs:label "三角灸" ;
                    blcu:pinyin ?pinyin ;
                    blcu:anatomy ?anatomy ;
                    blcu:location ?location ;
                    blcu:mainIndication ?mainIndication ;
                    <http://www.blcu.edu.cn/qinmeiping/ontologies/xuewei/操作:> ?method .
  BIND("三角灸" AS ?label)
}

    """
)



ret = sparql.queryAndConvert()
print(ret)