class ProgrammingLanguage:
    """Creates a class about about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initiates a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name} : {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns True/False if the programming language is dynamically typed or not"""
        return self.typing == "Dynamic"

if __name__ == '__main__':

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print(languages[1])
