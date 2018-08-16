from collections import defaultdict


def getTopNBasedOnUserId(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    topNBasedOnUserId = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        topNBasedOnUserId[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in topNBasedOnUserId.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        topNBasedOnUserId[uid] = user_ratings[:n]

    return topNBasedOnUserId


def getTopNBasedOnProductId(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    topNBasedOnUserId = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        topNBasedOnUserId[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in topNBasedOnUserId.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        topNBasedOnUserId[uid] = user_ratings[:n]

    return topNBasedOnUserId