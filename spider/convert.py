import json
import pandas as pd

data_path="aaaa.txt"

def read_file (path):
    with open (path,"r", encoding="utf8") as f:
        #print(json.loads(f.read()))
        dict=json.loads(f.read())
    return dict

def reload(dic):
    list=[]
    """    dict={}
    dict["subject"]=[]
    dict["relation"]=[]
    dict["object"]=[]"""
    for a,b in dic.items():

        main= a[a.index("）")+2:].split(" ")
        name=main[0]
        #print (len(main))
        print ("\n"+name)
        if (len(main)>1):
            label=main[1]
            dict={}
            dict["subject"]=name
            dict["relation"]="拼音"
            dict["object"]= label
            list.append(dict)
            print("拼音 |||||||| "+label)
        for relation in b.split("%"):
            if (relation==""):
                continue
            relationli=relation.split(" ")
            fun=relationli[0][1:-1]
            discribe="".join(relationli[1:])
            dict={}
            dict["subject"]=name
            dict["relation"]=fun
            dict["object"]=discribe
            list.append(dict)
            print (fun,"||||||||",discribe)
    return list


dic = read_file(data_path)

dict=reload(dic)
print (dict)


df=pd.DataFrame(data=dict)
df.to_csv("out.csv",index=False)