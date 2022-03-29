import os

# Rules for bracket based off of https://www.boydsbets.com/whats-the-farthest-each-seed-has-gone-in-the-tournament/
#   Rule 1) Only pick from the top 3 seeds to win tournament
#   Rule 2) Best for seeds 4-7 is final four
#   Rule 3) Best for seeds 9-11 is elite eight
#   Rule 4) Best for seeds 12-16 is sweet sixteen

# Odds Nested Dictionary
#     Odds are round, then seed: oddsDict[2][12] is the odds of a 12th seed winning in the 2nd round
#     Odds are from https://www.betfirm.com/seeds-national-championship-odds/
oddsDict = {
# seed: {64teams: r1pct, 32teams: r2pct, sweet16: r3pct, elite8: r4pct, final4: r5pct, finals: r6pct}
    1:  {1: 0.993, 2: 0.860, 3: 0.813, 4: 0.590, 5: 0.610, 6: 0.640},
    2:  {1: 0.938, 2: 0.675, 3: 0.714, 4: 0.462, 5: 0.433, 6: 0.385},
    3:  {1: 0.847, 2: 0.615, 3: 0.493, 4: 0.459, 5: 0.647, 6: 0.364},
    4:  {1: 0.785, 2: 0.593, 3: 0.313, 4: 0.619, 5: 0.231, 6: 0.000},
    5:  {1: 0.646, 2: 0.527, 3: 0.200, 4: 0.780, 5: 0.428, 6: 0.000},
    6:  {1: 0.625, 2: 0.478, 3: 0.349, 4: 0.200, 5: 0.667, 6: 0.000},
    7:  {1: 0.604, 2: 0.322, 3: 0.357, 4: 0.300, 5: 0.000, 6: 0.000},
    8:  {1: 0.493, 2: 0.197, 3: 0.571, 4: 0.600, 5: 0.000, 6: 0.000},
    9:  {1: 0.507, 2: 0.096, 3: 0.571, 4: 0.250, 5: 0.000, 6: 0.000},
    10: {1: 0.396, 2: 0.403, 3: 0.347, 4: 0.125, 5: 0.000, 6: 0.000},
    11: {1: 0.375, 2: 0.444, 3: 0.375, 4: 0.556, 5: 0.000, 6: 0.000},
    12: {1: 0.354, 2: 0.431, 3: 0.091, 4: 0.000, 5: 0.000, 6: 0.000},
    13: {1: 0.215, 2: 0.194, 3: 0.000, 4: 0.000, 5: 0.000, 6: 0.000},
    14: {1: 0.153, 2: 0.100, 3: 0.000, 4: 0.000, 5: 0.000, 6: 0.000},
    15: {1: 0.063, 2: 0.222, 3: 0.000, 4: 0.000, 5: 0.000, 6: 0.000},
    16: {1: 0.007, 2: 0.000, 3: 0.000, 4: 0.000, 5: 0.000, 6: 0.000}
}

def main():
    # Do something here




if __name__ == '__main__':
    main();
