from surprise import KNNBasic
from surprise import Dataset
from surprise import Reader
from top_n_recommendations import getTopNBasedOnUserId
import pandas as pd

def returnAllResultRecommendation():

    # GET DATA AND COLLECT TO PANDAS FORM
    dfRatings = pd.read_csv("/Users/redthegx/PycharmProjects/recommendation-services/resources/input/movie_ratings_data_set.csv")

    # SETTING THE RANGE OF RATTING IN THE PARAMETER NAME READER
    setRangeRatings = Reader(rating_scale=(1, 5))

    # TURN DF TO DATA FORM FOR PUT INTO THE FUNCTION OF ALGORITHM
    dataRatings = Dataset.load_from_df(dfRatings, reader=setRangeRatings)

    trainSet = dataRatings.build_full_trainset()
    algo = KNNBasic(k=10)
    algo.fit(trainSet)

    testset = trainSet.build_anti_testset()
    predictions = algo.test(testset)
    top_n = getTopNBasedOnUserId(predictions, n=10)


    topNList = []
    for uid, user_ratings in top_n.items():
        obj = {
            'leadId': uid,
            'productId': ([iid for (iid, _) in user_ratings])
        }
        topNList.append(obj)

    return topNList


if __name__ == "__main__":
    returnAllResultRecommendation()