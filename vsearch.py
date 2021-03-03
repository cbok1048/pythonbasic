def search4vowels(word):
    '''Return a boolean based on any vowels found'''
    vowels = set('aeiou')
    return vowels.intersection(set(word))

search4vowels('hitch-hiker')

search4vowels('galaxy')

search4vowels('life, the universe and everything')

search4vowels('sky')
