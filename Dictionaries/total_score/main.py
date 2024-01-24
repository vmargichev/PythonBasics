def merge(dict1, dict2):
    return dict1 | dict2


def total_score(score_dict):
    total_score_sum = 0
    for score in score_dict:
        total_score_sum += score_dict[score]
    return total_score_sum