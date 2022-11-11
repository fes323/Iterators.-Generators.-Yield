class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter = -1
        self.nest_counter = 0
        self.limit = len(self.list_of_list)

    def __iter__(self):
        self.counter += 1
        self.nest_counter = 0
        return self

    def __next__(self):
        while self.counter - self.limit and self.nest_counter == len(self.list_of_list[self.counter]):
            iter(self)
        if self.counter == self.limit:
            raise StopIteration
        self.nest_counter += 1
        item = self.list_of_list[self.counter][self.nest_counter - 1]
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item)
        print(check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()