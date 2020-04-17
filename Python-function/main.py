song = 'Song'
year = 2018
artist = 'artist'
genere = 'genere'
length = 3.5
duration, publisher = 10, 'publisher'
isHitSong = True

def Genre():
    return genere

def Artist():
    return artist

def Year():
    return year

def IsHitSong():
    return isHitSong

result = 'Test'
def MultiplyByTwo(input):    
    result1 = input *2
    print(result1)
    return result1

MultiplyByTwo(2)
print(result)

def max(a, b):
    if a > b:
        print('a is the max')
    else:
        print('b is the max')

max(1,2)
