import click
import renamer

@click.group()
def main():
    pass

main.add_command(renamer.rename)
