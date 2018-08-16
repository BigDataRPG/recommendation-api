from createRecommendation import returnAllResultRecommendation
from responseRecommendation import makeSuccessResponse, makeFailResponse


lead_id = 20
topNList = returnAllResultRecommendation()
productResultByLeadID = [lead for lead in topNList if lead['leadId'] == lead_id]

print(productResultByLeadID)


# response = makeSuccessResponse(topNList)
# responseResult = response['results']
# responseResultLeadID15 = [lead for lead in responseResult if lead['leadID'] == 101]
#
# print(makeFailResponse(responseResultLeadID15))

# print(responseResult)