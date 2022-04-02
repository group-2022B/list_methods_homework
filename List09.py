def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    answer = []

    answer.append(fruits.count("apple"))

    if 'apple' == fruits[0]:
        answer.append(0)
    if 'apple' == fruits[1]:
        answer.append(1)
    if 'apple' == fruits[2]:
        answer.append(2)
    if 'apple' == fruits[3]:
        answer.append(3)
    if 'apple' == fruits[4]:
        answer.append(4)
    return answer

print(main(["apple", "banana", "apple", "pear", "apple"]))