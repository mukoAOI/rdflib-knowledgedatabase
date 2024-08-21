import jieba.posseg as pseg
from QueryTemplates import QueryTemplates

# 分解出穴位的名字
def AcupuncturePoint_name(query):
    words = pseg.cut(query)  # 使用pseg进行分词和词性标注
    AcupuncturePoint_name = None

    for word, flag in words:
        if flag == "n":  # 选择名词
            AcupuncturePoint_name = word
            break  # 找到第一个名词就退出循环

    print(AcupuncturePoint_name)
    return AcupuncturePoint_name


# SPARQL查询穴位定位并返回结果
# 示例语句：天府的定位在哪里
def Location(query):
    AcupuncturePoint = AcupuncturePoint_name(query)
    new_query=QueryTemplates.XueWei_location.format(AcupuncturePoint)
    """
        # 执行SPARQL查询
    
    # print(results)
    # 将结果转换为字符串列表
    result_list = list(results)

    result_list = [str(result) for result in results]
    # print("result_list", result_list)
    pattern = r"'(.+)'"
    words = [re.search(pattern, item).group(1) for item in result_list]
    print(words, AcupuncturePoint_name)
    
    """
    return new_query


def mainIndication(query):
    AcupuncturePoint = AcupuncturePoint_name(query)
    new_query = QueryTemplates.XueWei_location.format(AcupuncturePoint)



