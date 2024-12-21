class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return wrapper


character = AnimeCharacter("Goku", "Kame Hame Wave")

@character.introduce
def character_intro():
    print(f"I am {character.name} and I can use {character.ability}.")

character_intro()