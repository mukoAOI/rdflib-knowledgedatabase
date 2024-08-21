import re

def Drug_name(query):
    drug_pattern = re.compile(r'[\u4e00-\u9fa5]+(?:丸|囊|剂|胶|片|膏|粒|浆|液|装)')

  
    match = drug_pattern.search(query)
    
    if match:
        print(match.group())
        return match.group()
    else:
       
        print("没有找到药品名称")
        return None


query = "七制香附丸的原料有哪些？"
extracted_drug_name = Drug_name(query)