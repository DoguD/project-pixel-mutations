import random


def generate_dna(length, possible_characters):
    possible_characters_length = len(possible_characters)
    dna = ''
    for i in range(length):
        dna += possible_characters[random.randint(0, possible_characters_length-1)]
    print("Generated DNA: " + dna)
    return dna


def save_dna_to_file(path, dna):
    try:
        f = open(path, 'w')
        f.write(dna)
    finally:
        f.close()


save_dna_to_file('./gen0_dnas/0.txt', generate_dna(1000000, ['u','d','l','r','p','u']))
