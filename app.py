from flask import Flask, jsonify, render_template
from random import randint

from responseRecommendation import makeSuccessResponse, makeFailResponse
from createRecommendation import getPredictionFromUserKNN, getTopNLeads, getTopNProducts

app = Flask("recommendation-services")

""" Prepapred to create function of Handler
and send them to each route
"""
predictions = getPredictionFromUserKNN()
topNLeads = getTopNLeads(predictions)
topNProducts = getTopNProducts(predictions)
resultAllLeads = makeSuccessResponse(topNLeads)
resultAllProducts = makeSuccessResponse(topNProducts)

"""ROUTE OF USER COLLABORATIVE-FILTERING
        RETURN ALL RESULT OF LEADID
        AND THEIR 10 PRODUCTS RELATED TO EACH LEADID
"""
@app.route('/usercf/leads', methods=['GET'])
def getAllLeadAndProductResultsByLeadIDUsingUserCFReccomendation():
    return jsonify(makeSuccessResponse(resultAllLeads))


@app.route('/usercf/leads/<int:leadId>', methods=['GET'])
def getOneLeadAndProductResultsByLeadIDUsingUserCFReccomendation(leadId):


    productResultByLeadId = [lead for lead in topNLeads if lead['leadId'] == leadId]
    if len(productResultByLeadId) == 0:
        finalResponsegetAllLeadAndProductResultsByLeadIDUsingUserCFReccomendation = makeFailResponse(productResultByLeadId)
    else:
        finalResponsegetAllLeadAndProductResultsByLeadIDUsingUserCFReccomendation = makeSuccessResponse(productResultByLeadId)

    return jsonify(finalResponsegetAllLeadAndProductResultsByLeadIDUsingUserCFReccomendation)


"""ROUTE OF USER COLLABORATIVE-FILTERING
        RETURN ALL RESULT OF PRODUCTID
        AND THEIR 10 PRODUCTS RELATED TO EACH PRODUCTID 
"""
@app.route('/usercf/products', methods=['GET'])
def getAllProductAndProductResultsByProductIDUsingUserCFReccomendation():
    return jsonify(makeSuccessResponse(resultAllProducts))


@app.route('/usercf/products/<int:productsId>', methods=['GET'])
def getOneProductAndProductResultsByProductIDUsingUserCFReccomendation(productsId):


    productResultByProductId = [product for product in topNProducts if product['productIdRef'] == productsId]
    if len(productResultByProductId) == 0:
        finalResponseGetOneProductAndProductResultsByProductIDUsingUserCFReccomendation = makeFailResponse(productResultByProductId)
    else:
        finalResponseGetOneProductAndProductResultsByProductIDUsingUserCFReccomendation = makeSuccessResponse(productResultByProductId)

    return jsonify(finalResponseGetOneProductAndProductResultsByProductIDUsingUserCFReccomendation)

@app.route('/')
def firstPage():
    #    return name
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]
    return render_template('index.html',**locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
