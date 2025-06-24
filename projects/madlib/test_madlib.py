from madlib.madlib import main, hobbit_story, willy_story, cat_story

def test_hobbit_story():
    noun1 = "hole"
    noun2 = "hobbit"
    adj1 = "happy"
    adj2 = "small"
    adj3 = "green"
    adj4 = "big"
    verb1 = "run"
    
    expected_output = f"""
In a {noun1} in the ground there lived a {noun2}.
Not a {adj1}, {adj2}, {adj3} {noun1}, filled with the ends of worms and an oozy smell,
nor yet a {adj4}, bare, sandy {noun1} with nothing to sit down on or to {verb1}:
it was a {noun2}-{noun1}, and that means comfort.
-- The Hobbit, J.R.R. Tolkien
"""
    assert hobbit_story(noun1, noun2, adj1, adj2, adj3, adj4, verb1) == expected_output

def test_willy_story():
    ...
def test_cat_story():
    ...
