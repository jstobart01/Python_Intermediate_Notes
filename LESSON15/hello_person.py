# This function allows the user to input their name and preferred language (no prompt provided at terminal)
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)


# Only calls if this is the file being ran.
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language", required=True, choices=["English", "Spanish", "German"], help="The language of the greeting."
    )
    args = parser.parse_args()

    hello(args.name, args.lang)
