"""
Character Creation System

Description:
    Create a game character by validating the character's
    name and starting attributes. If all validation rules
    are satisfied, display the character's statistics
    using filled and empty dots.

Author:
    Aashutosh Bakhrel (आशुतोष बाख्रेल)

Python Version:
    Python 3.12.3

Keywords:
    Python, Character Creation, Input Validation,
    Conditional Statements, Functions, Strings,
    Unicode Characters, RPG

Technologies / Concepts Used:
    - Python 3
    - Functions
    - Type Hints
    - Docstrings
    - Variables
    - String Operations
    - Conditional Statements (if-elif-else)
    - Input / Output (I/O)
    - PEP 8

Complexity:
    Time : O(1)
    Space: O(1)
"""

full_dot = "●"
empty_dot = "○"


def create_character(
    name: str,
    strength: int,
    intelligence: int,
    charisma: int,
) -> str:
    """
    Validate the character information and create
    a formatted character sheet.

    Args:
        name: Character name.
        strength: Strength stat.
        intelligence: Intelligence stat.
        charisma: Charisma stat.

    Returns:
        Character sheet if validation succeeds,
        otherwise an error message.
    """

    if not isinstance(name, str):
        return "The character name should be a string"

    elif name == "":
        return "The character should have a name"

    elif len(name) > 10:
        return "The character name is too long"

    elif " " in name:
        return "The character name should not contain spaces"

    elif not (
        isinstance(strength, int)
        and isinstance(intelligence, int)
        and isinstance(charisma, int)
    ):
        return "All stats should be integers"

    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    elif (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    a = name + "\n"
    b = (
        "STR "
        + strength * full_dot
        + (10 - strength) * empty_dot
        + "\n"
    )
    c = (
        "INT "
        + intelligence * full_dot
        + (10 - intelligence) * empty_dot
        + "\n"
    )
    d = (
        "CHA "
        + charisma * full_dot
        + (10 - charisma) * empty_dot
    )

    return a + b + c + d


def main() -> None:
    """
    Create a sample character and display
    the generated character sheet.
    """

    character = create_character(
        "f",
        4,
        1,
        2,
    )

    print(character)


if __name__ == "__main__":
    main()
