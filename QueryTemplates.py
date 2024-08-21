class QueryTemplates:
    # SPARQL查询穴位定位并返回结果
    # 示例语句：天府的定位在哪里
    XueWei_location = """
        PREFIX blcu: <http://www.blcu.edu.cn/qinmeiping/ontologies/xuewei/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?location
        WHERE {{
            ?point a blcu:AcupuncturePoint ;
                    rdfs:label ?pointLabel ;
                    blcu:location ?location;
            FILTER (?pointLabel = "{}")
        }} 
    """

    # SPARQL查询穴位主治并返回结果
    # 示例语句：天府可以主治什么？
    XueWei_main_indication = """
        PREFIX blcu: <http://www.blcu.edu.cn/qinmeiping/ontologies/xuewei/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?mainIndication
        WHERE {{
            ?point a blcu:AcupuncturePoint ;
                    rdfs:label ?pointLabel ;
                    blcu:mainIndication ?mainIndication;
            FILTER (?pointLabel = "{}")
        }} 
    """

    # SPARQL查询穴位刺灸手法并返回结果
    # 示例语句：天府的刺灸手法是什么？
    XueWei_acupuncture_method = """
        PREFIX blcu: <http://www.blcu.edu.cn/qinmeiping/ontologies/xuewei/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?acupunctureMethod
        WHERE {{
            ?point a blcu:AcupuncturePoint ;
                    rdfs:label ?pointLabel ;
                    blcu:acupunctureMethod ?acupunctureMethod;
            FILTER (?pointLabel = "{}")
        }} 
    """

    # SPARQL查询穴位配伍并返回结果
    # 示例语句：天府的配伍是什么？
    XueWei_complementary_points = """
        PREFIX blcu: <http://www.blcu.edu.cn/qinmeiping/ontologies/xuewei/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?complementaryPoints
        WHERE {{
            ?point a blcu:AcupuncturePoint ;
                    rdfs:label ?pointLabel ;
                    blcu:complementaryPoints ?complementaryPoints;
            FILTER (?pointLabel = "{}")
        }} 
    """

    # 药品可以治疗哪些症状
    # 示例句子：元胡止痛片的功效是什么？
    Drug_efficacy_query = """
            PREFIX ns1: <http://example.org/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?Efficacy
            WHERE {{
                ?drug a ns1:Drug ;
                        rdfs:label ?drugLabel ;
                        ns1:hasEfficacy ?Efficacy;
                FILTER (?drugLabel = "{}")
            }} 
        """

    # 药品的原料有哪些
    # 示例句子：元胡止痛片的原料有哪些？
    Drug_ingredient_query = """
            PREFIX ns1: <http://example.org/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?Ingredient
            WHERE {{
                ?drug a ns1:Drug ;
                        rdfs:label ?drugLabel ;
                        ns1:hasIngredient ?Ingredient;
                FILTER (?drugLabel = "{}")
            }} 
        """
