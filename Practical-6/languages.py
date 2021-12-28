
from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    dynamic_languages = []
    for language in languages:
        if language.is_dynamic():
            print(language.name)
            dynamic_languages.append(language.name)

    print("The dynamically typed languages are:", dynamic_languages[0],"," ,dynamic_languages[1])
main()