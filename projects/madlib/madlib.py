import random

class MadLibsGame:
    def __init__(self):
        self.stories = {
            "Hobbit": self.hobbit_input,
            "Willy Wonka": self.willy_input,
            "Cat and the Hat": self.cat_input
        }

    def main(self):
        choice = random.choice(list(self.stories.keys()))
        print(f"\nYou got: {choice}!\n")
        print(self.stories[choice]()) 

    def hobbit_input(self):
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter a species: ")
        adj1 = input("Enter an adjective: ")
        adj2 = input("Enter another adjective: ")
        adj3 = input("Enter another adjective: ")
        adj4 = input("Enter another adjective: ")
        verb1 = input("Enter a verb: ")
        return self.hobbit_story(noun1, noun2, adj1, adj2, adj3, adj4)

    def willy_input(self):
        noun1 = input("Enter a name: ")
        adj1 = input("Enter an adjective: ")
        adj2 = input("Enter another adjective: ")
        noun2 = input("Enter a type of job: ")
        verb1 = input("Enter a verb: ")
        noun3 = input("Enter a noun: ")
        return self.willy_story(noun1, adj1, adj2, noun2, verb1, noun3)

    def cat_input(self):
        noun1 = input("Enter a noun: ")
        verb1 = input("Enter a verb: ")
        adj1 = input("Enter a wet adjective: ")
        verb2 = input("Enter another verb: ")
        noun2 = input("Enter another noun: ")
        adj2 = input("Enter another adjective: ")
        return self.cat_story(noun1, verb1, adj1, verb2, noun2, adj2)

    def hobbit_story(self, noun1, noun2, adj1, adj2, adj3, adj4, verb1):
        return f"""
In a {noun1} in the ground there lived a {noun2}.
Not a {adj1}, {adj2}, {adj3} {noun1}, filled with the ends of worms and an oozy smell,
nor yet a {adj4}, bare, sandy {noun1} with nothing to sit down on or to {verb1}:
it was a {noun2}-{noun1}, and that means comfort.

-- The Hobbit, J.R.R. Tolkien
"""

    def willy_story(self, noun1, adj1, adj2, noun2, verb1, noun3):
        return f"""
Mr. {noun1} was the most {adj1}, the most {adj2},
the most extraordinary {noun2} the world had ever {verb1}!
And did you know that he had a tremendous {noun3}?

-- Charlie and the Chocolate Factory, Roald Dahl
"""

    def cat_story(self, noun1, verb1, adj1, verb2, noun2, adj2):
        return f"""
The {noun1} did not {verb1}. It was too {adj1} to play.
So we {verb2} in the {noun2} all that {adj2}, {adj2} wet day.
I {verb2} there with Sally. We {verb2} there, we two.
And I said, 'How I wish we had something to do!'

-- The Cat in the Hat, Dr. Seuss
"""


if __name__ == "__main__":
    game = MadLibsGame()
    game.main()

