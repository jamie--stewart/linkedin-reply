from jinja2 import Environment, FileSystemLoader, select_autoescape
import pyperclip
import sys

env = Environment(loader=FileSystemLoader(searchpath="./"), autoescape=select_autoescape())


TEMPLATE_FILENAME = "auto.txt"
TEMPLATE = env.get_template(TEMPLATE_FILENAME)


print("Input name (or empty string to exit)")
while True:
    name = input(f"\nAnother name:").strip()
    if not name:
        sys.exit(0)

    extra = input(f"\nPrefix?: ").strip()

    prefix = f"{extra}, but" if extra else "Right now"

    new_copy = TEMPLATE.render(name=name, prefix=prefix)
    pyperclip.copy(new_copy)
    print(f"Copy generated for {name}")
