# youtube tag checker (made by Bazinga)

# imports
import requests 
import colorama
import random

def randomPattern(pattern) -> str:
    vowels: str = 'aeiou'
    consonants: str = 'bcdfghjklmnpqrstvwxyz'
    build: str = ''

    for i in pattern: # may be better
        if i == 'v': build += random.choice(list(vowels))
        if i == 'V': build += random.choice(list(vowels)).upper()
        
        if i == 'c': build += random.choice(list(consonants))
        if i == 'C': build += random.choice(list(consonants)).upper()

        if i == 'n': build += str(random.randrange(0, 10)) # numbers
    
    return build

# Variables (pattern to choose | regex matcher | generated nicks list)
pattern: str = 'Cvcv'
matcher: str = '....'
generated: list = []

# url variable
url = r'https://www.youtube.com/@'

# access function -> sends the request
access = lambda nick: requests.get(url + nick).text 

# generate the nicks
for i in range(1200):
    b = randomPattern(pattern)
    while b in generated:  b = randomPattern(pattern) # unique
    generated.append(b)

# checks
for i in generated:
    if '404 Not Found' in access(i): 
        print(f'✅ | Username {i} is {colorama.Fore.GREEN}available{colorama.Fore.RESET}!')
    else:
        # uncomment to show only "available" ones
        print(f'❌ | Username {i} is {colorama.Fore.RED}NOT {colorama.Fore.RESET}available!')
        pass
