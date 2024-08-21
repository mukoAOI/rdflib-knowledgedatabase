from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from SparkQuery import Query
import uvicorn
import re





def get_values(strr):
    strout=""
    if (not type(strr)=="str"):
        strout=str(strr)
    else :
        strout=strr
    # 定义正则表达式来匹配value字段中的值
    pattern = r'\'value\':\s*\'(.*?)\''

    chinese_pattern = re.compile(r'[\u4e00-\u9fa5]+')
    # 使用正则表达式进行匹配
    match = re.findall(pattern, strout)
    match_list=[]
    for uri in match:
        if "http" in uri:
            out = chinese_pattern.search(uri)
            match_list.append(str(out.group()))
        else:
            match_list.append(uri)
    # 提取匹配到的值
    if len(match_list)!=0:
        return  match_list
    else:
        return ["未找到匹配的值"]


# Set up the SPARQL endpoint URL
sparql_endpoint = "http://localhost:8010/sparql/"
sparql = Query(sparql_endpoint)

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # 指定模板目录

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("test.html", {"request": request, "result": None})


@app.post("/submit")
async def submit_question(user_input: str = Form(...)):
    # 这里处理从表单提交过来的数据，user_input 是表单中输入的问题
    # Create a SPARQLWrapper instance and set the endpoint


    result = sparql.all_query(user_input)
    # 假设这里有个函数来获取答案，这里只是一个示例

    print(get_values(result))
    return {"result": f"您的问题答案是：{','.join(get_values(result))}"}



@app.get("/index", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})

# 处理问题并返回答案的路由
@app.post("/answer")
async def answer_question(user_input: str = Form(...)):
    result = sparql.all_query(user_input)
    # 假设这里有个函数来获取答案，这里只是一个示例



    return {"answer": ','.join(get_values(result))}
uvicorn.run(app, host="localhost", port=8011)