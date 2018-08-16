from flask import Flask, jsonify

from responseRecommendation import makeSuccessResponse, makeFailResponse
from createRecommendation import returnAllResultRecommendation

app = Flask("recommendation-services")

""" Prepapred to create function of Handler
and send them to each route
"""
topNList = returnAllResultRecommendation()
allProductResultFromUserCF = makeSuccessResponse(topNList)

"""ROUTE OF USER COLLABORATIVE-FILTERING
        RETURN ALL RESULT OF LEADID
        AND THEIR 10 PRODUCTS RELATED TO EACH LEADID
"""
@app.route('/usercf/leads', methods=['GET'])
def getAllLeadAndProductResultsByLeadIDUsingUserCFReccomendation():
    return jsonify(makeSuccessResponse(allProductResultFromUserCF))


@app.route('/usercf/leads/<int:leadId>', methods=['GET'])
def getOneLeadAndProductResultsByLeadIDUsingUserCFReccomendation(leadId):


    productResultByLeadId = [lead for lead in topNList if lead['leadId'] == leadId]
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
    return jsonify(makeSuccessResponse(allProductResultFromUserCF))


@app.route('/usercf/products/<int:productsId>', methods=['GET'])
def getOneProductAndProductResultsByProductIDUsingUserCFReccomendation(productsId):


    productResultByProductId = [product for product in topNList if product['leadId'] == productsId]
    if len(productResultByProductId) == 0:
        finalResponseGetOneProductAndProductResultsByProductIDUsingUserCFReccomendation = makeFailResponse(productResultByProductId)
    else:
        finalResponseGetOneProductAndProductResultsByProductIDUsingUserCFReccomendation = makeSuccessResponse(productResultByProductId)

    return jsonify(finalResponseGetOneProductAndProductResultsByProductIDUsingUserCFReccomendation)






if __name__ == "__main__":
  app.run(debug=True)
