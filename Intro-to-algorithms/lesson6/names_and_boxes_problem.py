import random
from collections import Counter


def create_box_names_map(prisoners_number):
    names = [i for i in range(prisoners_number)]
    random.shuffle(names)
    return names


def random_choise_of_prisoners():

    for i in range(prisoners_number):
        if i not in random.sample([x for x in range(prisoners_number)], 50):
            return 0
    return 1


def choice_with_algorithm():

    def single_prisoner_algorithm():

        current_box = prisoners_order[prisoner]
        for attempt in range(50):
            name_in_box = names_in_boxes[current_box]
            if prisoner == name_in_box:
                all_attempts.append(attempt)
                return True
            else:
                current_box = prisoners_order[name_in_box]
            attempt += 1

        return False
    all_attempts = []
    prisoners_order = create_box_names_map(prisoners_number)
    for prisoner in range(prisoners_number):
        if single_prisoner_algorithm() is False:
            return 0
    return 1

prisoners_number = 100
names_in_boxes = create_box_names_map(prisoners_number)
experiments_number = 100
number_algorithm = 0
number_random = 0
for i in range(experiments_number):
    number_random += random_choise_of_prisoners()
    number_algorithm += choice_with_algorithm()

print 'random: %s/%s' % (number_random, experiments_number)
print 'algorithm: %s/%s' % (number_algorithm, experiments_number)