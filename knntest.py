import knnAlgorithm as a1


def test_what_occure_most():
    example_list = ['test1', 'test2', 'test3', 'test1']
    algorithm = al.Algorithm_kNN(4, [], [])
    result = algorithm.get_most_occurrences(example_list)
    assert result == 'test1'

