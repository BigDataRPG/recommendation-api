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
        "'Mathematics is the art of giving the same name to different things.' -- Henri Poincare",
        "'Computer science is no more about computers than astronomy is about telescopes.' --  Edsger Dijkstra",
        "'To understand Machine Learning you must first understand Machine Learning.' -- Unknown",
        "'Pure mathematics is, in its way, the poetry of logical ideas.' -- Albert Einstein",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Mathematics is the music of reason.' -- James Joseph Sylvester"]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]
    return render_template('index.html',**locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
