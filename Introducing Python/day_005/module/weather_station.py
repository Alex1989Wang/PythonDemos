
def get_description():
    """return today's weather's description"""
    possibilities = ["rain", "snow", "sleet",
            "fog", "sun", "who knows"]
    from random import choice
    return choice(possibilities)

