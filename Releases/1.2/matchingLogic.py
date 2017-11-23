
def isLowElo(rvalue):
    return rvalue <= 16

LOW_ELO_LIMITS = {
    "BRONZE": (0,10),
    "SILVER": (0,15),
    "GOLD":   (5,19),
    "PLATINUM":(10,20)
}

HIGH_ELO_LIMITS = {
    "PLATINUM III":(10,21),
    "PLATINUM II":(10,22),
    "PLATINUM I":(10,23),
    
    "DIAMOND V":(17,24),
    "DIAMOND IV":(18,25),
    "DIAMOND III":(19,26),
    "DIAMOND II":(20,26),
    "DIAMOND I":(21,26),
    
    "MASTER I":(22,26),
    "CHALLENGER I":"nope"
}

R_VALUES = {
    "BRONZE V":0,
    "BRONZE IV":1,
    "BRONZE III":2,
    "BRONZE II":3,
    "BRONZE I":4,

    "SILVER V":5,
    "SILVER IV":6,
    "SILVER III":7,
    "SILVER II":8,
    "SILVER I":9,

    "GOLD V":10,
    "GOLD IV":11,
    "GOLD III":12,
    "GOLD II":13,
    "GOLD I":14,

    "PLATINUM V":15,
    "PLATINUM IV":16,
    "PLATINUM III":17,
    "PLATINUM II":18,
    "PLATINUM I":19,

    "DIAMOND V":20,
    "DIAMOND IV":21,
    "DIAMOND III":22,
    "DIAMOND II":23,
    "DIAMOND I":24,

    "MASTER I":25,

    "CHALLENGER":9999
}

