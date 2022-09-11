poem = ("'Jabberwocky'"
        "\n\n’Twas brillig, and the slithy toves\n    Did gyre and gimble in the wabe;"
        "\nAll mimsy were the borogoves,\n    And the mome raths outgrabe."
        "\n\n'Beware the Jabberwock, my son\n    The jaws gthat bite, the claws that catch!\n"
        "Beware the Jubjub bird, and shun\n    The frumious Bandersnatch!' "
        "\n\nHe took his vorpal sword in hand;\n    Long time the manxome for he sought-\n"
        "So rested he by the tumtunm tree,\n    And stood awhile in thought."
        "\n\nAnd, as in uffish thought he stood,\n    The Jabberwock, with eyes of flame,\n"
        "Came whiffling through the tulgey wood,\n    And burbled as it came!"
        "\n\nOne, two! One, two! And though and through\n    The vorpal blade went snicker-snack!"
        "\nHe left it dead, and with its head\n    He went galumphing back."
        "\n\n" ''"And hast thou slain the Jabberwock?\n      Come into my arms, my beamish boy!\n"
        "O frabjous day! Caollooh! Callay!\n    He chortled in his joy."
        "\n\n 'Twas brillid, and the slithy toves\n    Did gyre and gimble in the wabe;\n"
        "All mimsy were the borogoves,\n    And the mome raths outgrabe."
        "\n\n")

print(poem)  # Using the defined variable named 'poem', we can print the content above to the console at runtime.
"\n\n"  # enter a space in the code to allow for visual tidiness and readability.

Vowel_counter_lowercase = (poem.count("a")) + (poem.count("e")) + (poem.count("i")) + (poem.count("o")) + (
    poem.count("u"))  # We will the .count method operation on our string for the definined variable (lowercase vowels)
# which we will add together to give a sum of all lowercase vowels in the string
Vowel_counter_uppercase = (poem.count("A")) + (poem.count("E")) + (poem.count("I")) + (poem.count("O")) + (
    poem.count("U"))  # using the '+' operator for addition.

print("Lowercase Vowels in Lewis Carroll's 'Jabberwocky':",
      Vowel_counter_lowercase)  # Give a string title with a descriptive sentence for number we will print

print("Uppercase Vowels in Lewis Carroll's 'Jabberwocky':",
      Vowel_counter_uppercase)  # Give a string title for the Uppercase Vowels in the same fashion

# Run the program
# The poem will print
# The two strings ''Lowercase Vowels in Lewis Carroll's 'Jabberwocky':"
# and "Uppercase Vowels in Lewis Carroll's 'Jabberwocky':" will
# print at runtime with the numerical values that they have counted
# from the string in the 'poem' variable
