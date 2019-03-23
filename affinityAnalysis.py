from numpy import array
from collections import defaultdict
from operator import itemgetter

features = ["videoGames", "manga", "anime", "hockey"]
n_features = len(features)

X = array([[1, 1, 1, 1],
          [1, 1, 1, 0],
          [1, -1, -1, 1],
          [0, 0, 0, 1],
          [-1, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 1]])


def get_fans(index, array):
    fans = 0
    for sample in array:
        if sample[index] == 1:
            fans += 1
    return fans


def print_rule(premise, conclusion, support, confidence, features):
  premise_name = features[premise]
  conclusion_name = features[conclusion]
  print("rule: if someone likes {} they will also like {}".format(premise_name, conclusion_name))
  print("confidence: {0:.3f} : idx {1} vs. idx {2}".format(
    confidence[(premise, conclusion)], premise, conclusion))
  print("support:{}".format(support[(premise, conclusion)]))


videoGame_fans = get_fans(0, X)
print("{}: people love video games".format(videoGame_fans))

manga_fans = get_fans(1, X)
print("{}: people love manga".format(manga_fans))

anime_fans = get_fans(2, X)
print("{}: people love anime".format(anime_fans))

hockey_fans = get_fans(3, X)
print("{}: people love hockey".format(hockey_fans))

valid_rules = defaultdict(int)
num_occurrence = defaultdict(int)

for sample in X:
    for premise in range(n_features):
        if sample[premise] == 1:
            num_occurrence[premise] += 1
            for conclusion in range(n_features):
                if premise == conclusion:
                    continue
                if sample[conclusion] == 1:
                    valid_rules[(premise, conclusion)] += 1

support = valid_rules
confidence = defaultdict(float)
for (premise, conclusion) in valid_rules.keys():
    rule = (premise, conclusion)
    confidence[rule] = valid_rules[rule] / num_occurrence[premise]

sorted_support = sorted(support.items(),
                        key=itemgetter(1),
                        reverse=True)
sorted_confidence = sorted(confidence.items(),
                           key=itemgetter(1),
                           reverse=True)

for i in range(12):
    print("Associated Rule {}".format(i + 1))
    premise, conclusion = sorted_support[i][0]
    print_rule(premise, conclusion, support, confidence, features)