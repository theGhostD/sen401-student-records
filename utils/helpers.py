# helpers.py - utility functions for the student records demo app


def highest_score(data):
    best = data[0]
    for d in data:
        if d["score"] > best["score"]:
            best = d
    return best


def lowest_score(data):
    worst = data[0]
    for d in data:
        if d["score"] < worst["score"]:
            worst = d
    return worst
