import re


def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    fruits = set(fruits)
    fruits.remove('apple')


    return list(fruits)

print(main(["apple", "apple", "apple", "apple", "kiwi"]))
