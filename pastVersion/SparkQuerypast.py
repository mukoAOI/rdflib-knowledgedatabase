from SPARQLWrapper import SPARQLWrapper,JSON
from QueryTemplates import QueryTemplates
import jieba.posseg as pseg
import jieba



class Query:
    def __init__(self,url):
        self.wrapper=SPARQLWrapper(url)
        self.wrapper.setReturnFormat(JSON)
        jieba.initialize()

    # 分解出穴位的名字
    def First_noun(self,query):
        words = pseg.cut(query)  # 使用pseg进行分词和词性标注
        first_noun = None
        for word, flag in words:
            if flag == "n":  # 选择名词
                first_noun = word
                break  # 找到第一个名词就退出循环

        #print(AcupuncturePoint_name)
        return first_noun

    def link_query(self,tempalte,var):
        return tempalte.format(var)
    def other(self):
        res = "敬请期待！"
        return res

    def query(self,struct_query):
        self.wrapper.setQuery(struct_query)
        return self.wrapper.queryAndConvert()

    def all_query(self,sparql_query):



        first_noun=self.First_noun(sparql_query)

        struct_query=""
        if "穴位定位在哪里" in sparql_query:

            struct_query=self.link_query(QueryTemplates.XueWei_location,first_noun)
            #prompt = str(first_noun) + "的位置在："

        # ×
        elif "穴位主要治疗什么" in sparql_query:
            struct_query=self.link_query(QueryTemplates.XueWei_main_indication,first_noun)
            #prompt = str(first_noun) + "主要治疗：："
        # √
        elif "穴位的刺灸手法是什么" in sparql_query:
            struct_query=self.link_query(QueryTemplates.XueWei_acupuncture_method,first_noun)
            #prompt = str(first_noun) + "的刺灸手法是："
        # √
        elif "穴位的配伍是什么" in sparql_query:
            struct_query=self.link_query(QueryTemplates.XueWei_complementary_points,first_noun)
            #prompt = str(first_noun) + "的配伍是："
        # √
        elif "药品的功效有哪些" in sparql_query:
            struct_query=self.link_query(QueryTemplates.Drug_efficacy_query,first_noun)
            #prompt = str(first_noun) + "的功效有："
        # √
        elif "药品的原料有哪些" in sparql_query:
            print(first_noun)
            struct_query=self.link_query(QueryTemplates.Drug_ingredient_query,first_noun)
            #prompt = str(first_noun) + "的原料有："
        # √
        else:
            # 执行其他操作的函数
            result = self.other()
            return result

        result = self.query(struct_query)

        return result