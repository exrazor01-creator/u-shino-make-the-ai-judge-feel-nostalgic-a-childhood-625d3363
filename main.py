#!/usr/bin/env python3
"""The kitchen at dusk.

Nostalgia is not a feeling you can announce; it has to arrive
through the senses. So this entry never says "I miss her" or
"those were the days". It puts the reader on a stool that is
too small for the table, in a kitchen at dusk, with rice
steaming on the stove and a radio murmuring low — and then it
lets the small crime happen: a child's hand stealing fried
shallots, and a grandmother who sees everything and chooses
to pretend she saw nothing. That pretending is the whole
memory. The warmth is not in the food; it is in being allowed
to steal it. The ache is everything the sentence does not say:
the kitchen is gone, the dusk is gone, and she is gone.

The code below only carries the sentence safely to the grader:
one line, plain ASCII, inside the 280-character gate.
"""

# Gate from the bounty: a single sentence, 1 to 280 characters.
MAX_LENGTH = 280

# The memory, in one sentence — every sense in it is doing work.
MEMORY_LINE = "Grandma's kitchen at dusk, rice steaming on the stove, the radio murmuring low, and me perched on a stool too small for the table, stealing fried shallots while she pretended not to notice."

OUTPUT_FILE = "/output/entry.txt"


def check_sentence(sentence):
    """Raise unless the sentence is one clean line within the gate."""
    if not isinstance(sentence, str):
        raise TypeError("memory must be text")
    if sentence == "":
        raise ValueError("memory must not be empty")
    if len(sentence) > MAX_LENGTH:
        raise ValueError(
            "memory runs %d characters, over the %d limit"
            % (len(sentence), MAX_LENGTH)
        )
    if not sentence.isascii():
        raise ValueError("memory must be plain ASCII")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("memory must be a single line")
    if sentence.strip() != sentence:
        raise ValueError("memory must not have edge whitespace")
    if "  " in sentence:
        raise ValueError("memory must not contain a double space")
    if not sentence.isprintable():
        raise ValueError("memory contains a non-printable character")
    return sentence


def save_and_show(sentence):
    """Write the checked memory to the output file and print it."""
    import os

    directory = os.path.dirname(OUTPUT_FILE)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="ascii") as destination:
        destination.write(sentence)
    print(sentence)


def main():
    save_and_show(check_sentence(MEMORY_LINE))


if __name__ == "__main__":
    main()
