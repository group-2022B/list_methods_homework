import re


def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    for i in fruits:
        if i == 'apple':
            fruits.remove(i)
    return fruits

print(main(["apple", "banana", "apple", "pear", "apple"]))
