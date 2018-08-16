""" CREATED BY BOYD BIGDATA RPG -- DATA SCIENTIST

    FUNCTION USE FOR GENERATING THE CUSTOMZIED BEST K-NN CF-RECOMMENDATION
    USING K-LIST INTO THE GRIDSEARCH FOR HYPER PARAMETER TUNING
    THEN THE RESULT WE CAN GET THE BEST K THAT LOWER THE RMSE THE BEST
"""


import pandas as pd
from surprise import KNNBasic
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import GridSearchCV
import timeit

def testKNNBestResult():

    """CREATED BY BOYD BIGDATA RPG -- DATA SCIENTIST

        HYPER PARAMETER TUNING:
            USING K-NN, CROSS-VALIDATION 5 FOLD
    """

    # START TIME TO MONITOR THE TIME CONSUMING
    start = timeit.default_timer()

    dfRatings = pd.read_csv("/Users/redthegx/PycharmProjects/recommendation-services/resources/input/movie_ratings_data_set.csv")

    # SETTING THE RANGE OF RATTING IN THE PARAMETER NAME READER
    setRangeRatings = Reader(rating_scale=(1, 5))

    # TURN DF TO DATA FORM FOR PUT INTO THE FUNCTION OF ALGORITHM
    dataRatings = Dataset.load_from_df(dfRatings, reader=setRangeRatings)


    print("#################################################################################")
    print("#####                      START COMPUTING GRIDSEARCH                       #####")
    print("#################################################################################")

    # SETTINGS THE LIST OF K FOR FINDING THE BEST RMSE AND HOW MANY K IS THE BEST
    param_grid = {'k': [10, 13, 15, 17, 20, 23, 25, 27, 30, 33, 36, 39, 42, 45, 48, 50]}
    gs = GridSearchCV(KNNBasic, param_grid, measures=['rmse', 'mae'], cv=5)
    gs.fit(dataRatings)

    print("\n")
    print("#################################################################################")
    print("#####                          GETTING BEST RESULT                          #####")
    print("#####                 BEST RMSE: = " + "{}".format(gs.best_score['rmse']) + "                        #####")
    print("#####                 BEST K:  = " + "{}".format(gs.best_params['rmse']['k']) + "                                         #####")
    print("#################################################################################")

    print('\n')
    print("#################################################################################")
    print("#####                             FINISH PROCESS                            #####")
    stop = timeit.default_timer()
    print("#####                      TIME CONSUMED: " + "{}".format(stop - start) + "                #####")
    print("#################################################################################")

    return gs.best_params['rmse']['k']

if __name__ == "__main__":
    testKNNBestResult()