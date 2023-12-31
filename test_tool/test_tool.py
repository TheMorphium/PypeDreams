from PypeDreams import pype_dreamer
from PypeDreams.compress import compress
from PypeDreams.adjectives import adjectives
from PypeDreams.colors import colors
from PypeDreams.animals import animals
from PypeDreams.clothing import clothing


def describe_pype_dreamer():
    print('should turn arbitrary string input into an animal hash')
    expect_val = 'Virtual Pear Wombat Wearing a Caftan'
    print(pype_dreamer('my ugly input string') == expect_val)

    print('should use a specified separator')
    expect_val = 'Virtual-Pear-Wombat-Wearing-a-Caftan'
    print(pype_dreamer('my ugly input string', separator='-') == expect_val)

    print('should support lowercased style')
    expect_val = 'virtual pear wombat wearing a caftan'
    print(pype_dreamer('my ugly input string', style='lowercase') == expect_val)

    print('should support uppercased style')
    expect_val = 'VIRTUAL PEAR WOMBAT WEARING a CAFTAN'
    print(pype_dreamer('my ugly input string',style='uppercase') == expect_val)

    print('should throw an error if passed an unknown style')
    try:
        pype_dreamer('xyz', style='garbage')
    except:
        print('/Unknown style/')


def describe_compress():
    print('compresses an md5 hash into an array of requested length integers')
    bytes = [ 23, 45, 234, 111, 46, 165, 33, 58, 156, 140, 91, 138, 50, 245, 103, 210 ]
    compressed = [ 145, 174, 163 ]
    print(compress(bytes, 3) == compressed)

    print('should throw an error if given fewer bytes than requested output')
    try:
        compress([ 23 ], 3)
    except:
        print('/Fewer input bytes/')

def describe_wordlist():
    print('should contain no duplicate entries')
    word_lists = [adjectives, colors, animals, clothing]
    word_count = len(adjectives + colors + animals + clothing)
    for word_list in word_lists:
        test_list, dupes = [], False
        for word in word_list:
            if word not in test_list:
                test_list.append(word)
            else:
                dupes = True
                print(f'{word} is a duplicate')
    print(word_count)
    print(word_count == (256 * 4))
    if not dupes:
        print('No duplicates found')

    # There are in fact a number of duplicates.  In order to keep this library identical to the Helium library
    # Those duplicates will remain until that library is updated.


describe_pype_dreamer()
describe_compress()
describe_wordlist()