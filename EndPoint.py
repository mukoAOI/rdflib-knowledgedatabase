import rdflib
from rdflib_endpoint import SparqlRouter
from rdflib import  ConjunctiveGraph, Literal
from rdflib.plugins.sparql.evalutils import _eval

from fastapi import FastAPI
import uvicorn

ep=FastAPI()


class EndPoint:
    def __init__(self,file_path):
        self.graph=ConjunctiveGraph()
        self.graph.parse(file_path,"turtle")
        self.graph.parse("data/outputGT.owl","owl")
        self.sparql_router=SparqlRouter(
            graph=self.graph,
            functions={
                "https://w3id.org/um/openpredict/most_similar": self.most_similar,
                "https://w3id.org/um/sparql-functions/custom_concat": self.custom_concat,
            },
            path="/",
            # Metadata used for the SPARQL service description and Swagger UI:
            title="中医药知识查询系统",
            description="zzzzy",
            version="0.1.0",
            public_url='https://localhost:8010/sparql',
        )

    def run(self):
        ep.include_router(self.sparql_router, prefix="/sparql")
        uvicorn.run(ep, host="localhost", port=8010)

    def custom_concat(query_results, ctx, part, eval_part):
        """
        Concat 2 string and return the length as additional Length variable
        \f
        :param query_results:   An array with the query results objects
        :param ctx:             <class 'rdflib.plugins.sparql.sparql.QueryContext'>
        :param part:            Part of the query processed (e.g. Extend or BGP) <class 'rdflib.plugins.sparql.parserutils.CompValue'>
        :param eval_part:       Part currently evaluated
        :return:                the same query_results provided in input param, with additional results
        """
        argument1 = str(_eval(part.expr.expr[0], eval_part.forget(ctx, _except=part.expr._vars)))
        argument2 = str(_eval(part.expr.expr[1], eval_part.forget(ctx, _except=part.expr._vars)))
        evaluation = []
        scores = []
        concat_string = argument1 + argument2
        reverse_string = argument2 + argument1
        # Append the concatenated string to the results
        evaluation.append(concat_string)
        evaluation.append(reverse_string)
        # Append the scores for each row of results
        scores.append(len(concat_string))
        scores.append(len(reverse_string))
        # Append our results to the query_results
        for i, result in enumerate(evaluation):
            query_results.append(
                eval_part.merge(
                    {part.var: Literal(result), rdflib.term.Variable(part.var + "Length"): Literal(scores[i])})
            )
        return query_results, ctx, part, eval_part

    def most_similar(query_results, ctx, part, eval_part):
        """
        Get most similar entities for a given entity

        PREFIX openpredict: <https://w3id.org/um/openpredict/>
        SELECT ?drugOrDisease ?mostSimilar ?mostSimilarScore WHERE {
            BIND("OMIM:246300" AS ?drugOrDisease)
            BIND(openpredict:most_similar(?drugOrDisease) AS ?mostSimilar)
        """
        # argumentEntity = str(_eval(part.expr.expr[0], eval_part.forget(ctx, _except=part.expr._vars)))
        # try:
        #     argumentLimit = str(_eval(part.expr.expr[1], eval_part.forget(ctx, _except=part.expr._vars)))
        # except:
        #     argumentLimit = None

        # Using stub data
        similarity_results = [{"mostSimilar": "DRUGBANK:DB00001", "score": 0.42}]

        evaluation = []
        scores = []
        for most_similar in similarity_results:
            evaluation.append(most_similar["mostSimilar"])
            scores.append(most_similar["score"])

        # Append our results to the query_results
        for i, result in enumerate(evaluation):
            query_results.append(
                eval_part.merge(
                    {part.var: Literal(result), rdflib.term.Variable(part.var + "Score"): Literal(scores[i])})
            )
        return query_results, ctx, part, eval_part