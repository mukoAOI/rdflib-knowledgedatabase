from SPARQLWrapper import SPARQLWrapper,JSON
from QueryTemplates import QueryTemplates
import jieba


class Query:
    def __init__(self,url):
        self.wrapper=SPARQLWrapper(url)
        self.wrapper.setReturnFormat(JSON)
        jieba.initialize()

    # 分解出穴位的名字
    def Point_name(self,query):
        dict_path = 'dict_point.txt'
        jieba.load_userdict(dict_path)
        with open(dict_path, 'r', encoding='utf-8') as file:
            custom_point = [line.strip() for line in file]
        words = jieba.cut(query)
        point_names = []
        for word in words:
            if word in custom_point:
                point_names.append(word)
        if point_names:
            for i in point_names:
                return i
        else:
            #print("没有找到输入的穴位")
            pass
        return None
    # 分解出药品的名字
    def Drug_name(self,query):
        dict_path = 'dict_drug.txt'
        jieba.load_userdict(dict_path)
        with open(dict_path, 'r', encoding='utf-8') as file:
            custom_drug = [line.strip() for line in file]
        words = jieba.cut(query)
        drug_names = []
        for word in words:
            if word in custom_drug:
                drug_names.append(word)
        if drug_names:
            for i in drug_names:
                return i
        else:
            #print("没有找到输入的药品")
            pass
        return None
    
    #分解出关系
    def Relation(self,query):
        dict_path = 'dict_relation.txt'
        jieba.load_userdict(dict_path)
        with open(dict_path, 'r', encoding='utf-8') as file:
            custom_relation = [line.strip() for line in file]
        words = jieba.cut(query)
        relation_names = []
        for word in words:
            if word in custom_relation:
                relation_names.append(word)

        if relation_names:
            for i in relation_names:
                return i
        else:
            print("输入的关系不成立")
        return None

    def link_query(self,tempalte,var):
        return tempalte.format(var)
    def other(self):
        res = "敬请期待！"
        return res

    def query(self,struct_query):
        self.wrapper.setQuery(struct_query)
        return self.wrapper.queryAndConvert()

    def all_query(self,sparql_query):

        Point_name=self.Point_name(sparql_query)
        Drug_name=self.Drug_name(sparql_query)
        Relation = self.Relation(sparql_query)

        print(Drug_name)
        print(Relation)
        struct_query=""

        if Point_name!= None and Relation == "定位":

            struct_query=self.link_query(QueryTemplates.XueWei_location,Point_name)
            #prompt = str(first_noun) + "的位置在："

        # ×
        elif Point_name != None and Relation== "主治":
            struct_query=self.link_query(QueryTemplates.XueWei_main_indication,Point_name)
            
        # √
        elif Point_name != None and Relation == "刺灸手法":
            struct_query=self.link_query(QueryTemplates.XueWei_acupuncture_method,Point_name)
            
        # √
        elif Point_name != None and Relation == "配伍":
            struct_query=self.link_query(QueryTemplates.XueWei_complementary_points,Point_name)
            
        # √
        elif Drug_name != None and Relation == "功效":

            struct_query=self.link_query(QueryTemplates.Drug_efficacy_query,Drug_name)

            
        # √
        elif Drug_name!= None and Relation == "原料":
            struct_query=self.link_query(QueryTemplates.Drug_ingredient_query,Drug_name)
            
        # √
        else:
            result = self.other()
            return result
        #print(struct_query)
        result = self.query(struct_query)

        return result