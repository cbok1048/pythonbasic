def search4vowels(phrase:str) -> set:
    '''Return a boolean based on any vowels found'''
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str,letters:str) -> set:
    """return a set of the 'letters' found in 'phrase'"""
    return set(letters), intersection(set(phrase))

search4letters('hitch - hiker','aeiou')
search4letters('galaxy','xyz')
search4letters('life, the universe', 'and everything', 'o')