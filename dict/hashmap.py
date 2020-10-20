from operator import gt, eq, concat
from itertools import count
from functools import reduce

from numpy import log2
from numpy import full as full_block
from numpy import empty as empty_block
from toolz import take, curry, compose, first, second


gt = curry(gt)
eq = curry(eq)


def take_while(predicate, iterable):
    for element in iterable:
        if predicate(element):
            yield element
        else:
            break


def take_one_above(predicate, iterable):
    for element in iterable:
        if not predicate(element):
            return element


def smaller_unsigned_integer_that_fits_(n):
    return "uint" + str(
        2 ** take_one_above(lambda i: 2**(2**i) - 1 < n, count(start=3))
    )

class HashMap:
    """A reimplementation of dictionaries using numpy arrays."""

    def __init__(self, *args, **kwargs):
        """Multiple Dispatch"""
        keys, values = self.parse_input(*args, **kwargs)
        self.allocate_memory(keys, values)

    def parse_input(self, *args, **kwargs):
        keys: list
        values: list
        if len(args) > 0:
            if isinstance(pairs := args[0], list):
                if isinstance(pairs[0], tuple) and len(pairs[0]) == 2:
                    keys, values = zip(*args[0])
                else:
                    raise ValueError(f"Invalid input format.")
            elif isinstance(string := args[0], str):
                keys, values = self.parse(string)
            elif isinstance(dict_ := args[0], dict):
                keys, values = zip(*dict_.items())
            else:
                raise ValueError(f"Invalid input format.")
        elif len(kwargs) > 0:
            keys, values = zip(*kwargs.items())
        else:
            raise ValueError(f"Invalid input format.")
        return keys, values

    @staticmethod
    def parse(string: str):
        string = string.strip()
        if "{" not in string:
            string = "{" + string + "}"
        if "=>" in string:
            string = string.replace("=>", ":")

        d = eval(string)

        return zip(*d.items())

    def allocate_memory(self, keys, values):
        size = len(keys)
        self.number_of_slots = 3*size if size > 5 else 15

        data_type = smaller_unsigned_integer_that_fits_(self.number_of_slots)
        self.placeholder = 2**int(data_type[4:]) - 1
        self.hash_array = full_block(self.number_of_slots, self.placeholder, dtype=data_type)
        self.pairs_array = empty_block(self.number_of_slots * 2 // 3 + 1, dtype=object)

        self.insert(keys, values)
                
    def insert(self, keys, values):
        for i, (key, value) in enumerate(zip(keys, values)):
            index = hash(key) % self.number_of_slots

            key_in_array = self.hash_array[index]
            if key_in_array == self.placeholder:
                self.hash_array[index] = i
            else:
                i = key_in_array

            pair_in_array = self.pairs_array[i]
            if pair_in_array is None:
                self.pairs_array[i] = (key, value)
            elif isinstance(pair_in_array, tuple):
                self.pairs_array[i] = [pair_in_array, (key, value)]
            elif not any(p[0] == key for p in pair_in_array):
                self.pairs_array[i].append((key, value))

    def __str__(self):
        return reduce(concat, (f"# {repr(key)} => {repr(value)},\n" for key, value in self.items()))[:-2]
    
    def keys(self):
        for pair in self.pairs_array:
            if pair is None:
                continue
            elif isinstance(pair, tuple):
                yield pair[0]
            else:
                yield from map(first, pair)

    def values(self):
        for pair in self.pairs_array:
            if pair is None:
                continue
            elif isinstance(pair, tuple):
                yield pair[1]
            else:
                yield from map(second, pair)

    def items(self):
        for pair in self.pairs_array:
            if pair is None:
                continue
            elif isinstance(pair, tuple):
                yield pair
            else:
                yield from pair

    def display_internals(self):
        print(f"""HashMap:
==============
{self}

--> Hash Array <--
{self.hash_array}

--> Pairs Array <--
{self.pairs_array}
----------------------------------------------------------------------------
""".replace(x := str(self.placeholder), len(x) * "_"))

    def __getitem__(self, key):
        hash_index = hash(key) % self.number_of_slots
        pair_index = self.hash_array[hash_index]

        pair = self.pairs_array[pair_index]
        if isinstance(pair, tuple):
            return pair[1]
        elif isinstance(pair, list):
            return next(p[1] for p in pair if p[0] == key)
        else:
            raise KeyError("Map key not found")


hashmap = HashMap("""
    "a" => 2,
    "b" => 3,
     1  => 9,
    16  => 10
""")

hashmap.display_internals()
print(hashmap[1])
print(hashmap[16])
