from fastapi import FastAPI
import uvicorn
from EndPoint import EndPoint

ep=FastAPI()

def sparql_router():
    endpoint=EndPoint("data/movies_cn.ttl")

def run(self):
    ep.include_router(sparql_router, prefix="/sparql")
    uvicorn.run(ep, host="localhost", port=8010)