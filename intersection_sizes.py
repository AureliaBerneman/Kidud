import itertools
import pprint


def get_radius1_l_ball(word: tuple) -> set:
    """
    The function receives a binary word in tuple form and returns its radius-1 l-ball as a set
    :param word: the binary word in tuple form
    :return: the radius-1 l-ball of the binary word
    """
    ball = {word}
    word_list = list(word)
    # insert 0 somewhere and delete one bit somewhere else
    for i in range(len(word_list) + 1):
        word_list.insert(i, 0)
        for j in range(len(word_list)):
            if j == i:
                continue
            tmp = word_list[j]
            word_list.pop(j)
            ball.add(tuple(word_list))
            word_list.insert(j, tmp)
        word_list = list(word)
    word_list = list(word)
    # insert 1 somewhere and delete one bit somewhere else
    for i in range(len(word_list) + 1):
        word_list.insert(i, 1)
        for j in range(len(word_list)):
            if j == i:
                continue
            tmp = word_list[j]
            word_list.pop(j)
            ball.add(tuple(word_list))
            word_list.insert(j, tmp)
        word_list = list(word)
    return ball


def get_intersection_dict(number_of_bits: int) -> dict:
    """
    The function receives an integer that represents the number of bits of binary words and returns a dictionary
    where the keys are tuples of 2 binary words (that have l-distance 1) and the values are tuples of:
    1) the size of the radius-1 l-ball of the first word
    2) the size of the radius-1 l-ball of the second word
    3) the size of the intersection of the radius-1 l-ball of the first word with the radius-1 l-ball of the second word
    :param number_of_bits: the number of bits for the binary words
    :return: the dictionary explained above
    """
    list_binary_words = list(itertools.product([0, 1], repeat=number_of_bits))
    intersection_dict = {}
    for word1 in list_binary_words:
        set1 = get_radius1_l_ball(word1)
        for word2 in set1:
            if word1 == word2:
                continue
            if (word2, word1) in intersection_dict:
                continue
            set2 = get_radius1_l_ball(word2)
            intersection = set1.intersection(set2)
            intersection_dict[word1, word2] = (len(set1), len(set2), len(intersection))
    return intersection_dict


def main():
    intersection_dict = get_intersection_dict(13)
    # print the pairs that have the biggest intersection
    sorted_dict = dict(sorted(intersection_dict.items(), key=lambda x: (x[1][2]), reverse=True))
    print("----pairs with biggest intersection----")
    pprint.pprint({A: N for (A, N) in [x for x in sorted_dict.items()][:6]}, sort_dicts=False)
    # print the pairs that have the biggest intersection for the word with the biggest ball
    sorted_dict = dict(sorted(intersection_dict.items(), key=lambda x: (x[1][0], x[1][2]), reverse=True))
    print("----pairs with biggest ball and intersection----")
    pprint.pprint({A: N for (A, N) in [x for x in sorted_dict.items()][:2]}, sort_dicts=False)


if __name__ == "__main__":
    main()
