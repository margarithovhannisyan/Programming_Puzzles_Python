'''
TASK - You are given the noises made by different animals that you can hear in the dark.
Evaluate each noise to determine which animal it belongs to.
Lions say 'Grr', Tigers say 'Rawr', Snakes say 'Ssss', and Birds say 'Chirp'.
Input Format is a string that represent the noises that you hear with a space between them.
'''

animalsAndSounds = {
    'Grr': 'Lion',
    'Rawr': 'Tiger',
    'Ssss': 'Snake',
    'Chirp': 'Bird'
}


def get_animal_by_noise(animalNoises):
    animalName = []
    for animalNoise in animalNoises.split():
        if animalNoise in animalsAndSounds:
            animalName.append(animalsAndSounds[animalNoise])
    return ' '.join(animalName)


animalNoises = 'Grr Grr Chirp'
print(get_animal_by_noise(animalNoises))
