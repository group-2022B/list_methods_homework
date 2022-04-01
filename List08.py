def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    if fruits[0] == 'apple':
        del fruits[0]
    if fruits[1] == 'apple':
        del fruits[1]
    if fruits[2] == 'apple':
        del fruits[2]
    if fruits[3] == 'apple':
        del fruits[3]
    if fruits[4] == 'apple':
        del fruits[4]


    return fruits

