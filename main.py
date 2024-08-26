import random
import string

words =[
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Fight Club",
    "Forrest Gump",
    #"Inception",
    "The Matrix",
    "The Lord of the Rings: The Fellowship of the Ring",
    "Star Wars: Episode IV - A New Hope",
    "Jurassic Park",
    "The Avengers",
    "Titanic",
    "The Lion King",
    "E.T. the Extra-Terrestrial",
    "Back to the Future",
    "Casablanca",
    "The Terminator",
    "Die Hard",
    #"Jaws",
    "Indiana Jones and the Last Crusade",
    "The Silence of the Lambs",
    "The Social Network",
    "Gone with the Wind",
    "The Great Gatsby",
    "Forrest Gump",
    "The Revenant",
    "Saving Private Ryan",
    "The Grand Budapest Hotel",
    "The Departed",
    "No Country for Old Men",
    "The Wolf of Wall Street",
    "A Beautiful Mind",
    "The Shape of Water",
    "Black Swan",
    "The Dark Knight Rises",
    "Django Unchained",
    #"Interstellar",
    "Mad Max: Fury Road",
    "The Green Mile",
    "The Good, the Bad and the Ugly",
    "Schindler's List",
    "The Godfather: Part II",
    "Blade Runner",
    "Inglourious Basterds",
    "The Shawshank Redemption",
    "The Social Network",
    "The Lord of the Rings: The Return of the King",
    "The Godfather: Part III",
    "A Clockwork Orange",
    "The Graduate",
    "2001: A Space Odyssey",
    "A Star Is Born",
    "The Wizard of Oz",
    "The Exorcist",
    "American Beauty",
    "Rain Man",
    "The Sound of Music",
    "Apocalypse Now",
    "Jurassic Park",
    "The Shining",
    "Good Will Hunting",
    "A Few Good Men",
    #"Inception",
    "The Matrix",
    "The Lion King",
    "The Terminator",
    "Die Hard",
    #"Jaws",
    "Indiana Jones and the Last Crusade",
    "The Silence of the Lambs",
    "The Social Network",
    "Gone with the Wind",
    "The Great Gatsby",
    "Forrest Gump",
    "The Revenant",
    "Saving Private Ryan",
    "The Grand Budapest Hotel",
    "The Departed",
    "No Country for Old Men",
    "The Wolf of Wall Street",
    "A Beautiful Mind",
    "The Shape of Water",
    "Black Swan",
    "The Dark Knight Rises",
    "Django Unchained",
    "Interstellar",
    "Mad Max: Fury Road",
    "The Green Mile",
    "The Good the Bad and the Ugly",
    "Schindler's List",
    #"Goodfellas",
    "The Godfather: Part II",
    "Blade Runner",
    "Inglourious Basterds",
    "The Shawshank Redemption",
    "The Social Network",
    "The Lord of the Rings: The Return of the King",
    "The Godfather: Part III",
    "A Clockwork Orange",
    "The Graduate",
    "2001: A Space Odyssey",
    "A Star Is Born",
    "The Wizard of Oz",
    "The Exorcist",
    "American Beauty",
    "Rain Man",
    "The Sound of Music",
    "Apocalypse Now",
]

def get_word(x):
    word = random.choice(words)
    return word


word = get_word(words).lower()
print(word)
word_letter = set(word)
alphabet = set(string.ascii_lowercase)
used_letter = set()
lives = 8
while len(word_letter)>0:
    print(lives)
    word_list = [letter if letter in used_letter else '_'for letter in word]
    if [word_letter] == word_list:
        print("YAY!!")
        print("\" " + word.upper(),"\" was the correct.")
        break
    print('Current word: ', ' '.join(word_list) )
    print('Your used letters are: ', ' '.join(used_letter))
    usr_letter = input('Guess a letter: ')[0].lower()
    if " " in word_letter:
        used_letter.add(" ")
    if "-" in word_letter:
        used_letter.add("-")
    if ":" in word_letter:
        used_letter.add(":")
    if usr_letter in used_letter:
        print("Already used that character")
    if (usr_letter not in used_letter) and (usr_letter not in word_letter):
        lives = lives - 1
        print("Invalid character") 
    if usr_letter in alphabet:
        used_letter.add(usr_letter)
        if usr_letter in word_letter:
            word_letter.remove(usr_letter)
    if lives == -1:
        print("OOPS")
        print("\" " + word.upper(),"\" was the correct.")
        break

