def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        re_enter = input("Is your name {}? (Y/n) ".format(name)).upper()
        if re_enter != "Y" and re_enter != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    max_length = max(len(name) for name in email_to_name)

    for email, name in email_to_name.items():
        print("{:{}} ({})".format(name, max_length, email))

def extract_name(email):
    whole_name = email.split('@')[0]
    name_parts = whole_name.split('.')
    name = " ".join(name_parts).title()
    return name
main()