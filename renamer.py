import click
import os
import re

@click.command()
@click.argument("directory")
@click.argument("regex")
@click.option("--replace", "-r", "pattern", type=(str, str), multiple=True)
@click.option("--prefix", "-p", "prefix")
@click.option("--suffix", "-s", "suffix")
@click.option("--low-memory", "low_memory", is_flag=True)
def rename(directory, regex, pattern, prefix, suffix, low_memory):
    # click.echo(f"Directory: {directory}.")
    # click.echo(f"regex: {regex}.")
    # click.echo(f"replace: {pattern}.")
    # click.echo(type(pattern))
    # click.echo(f"Prefix: {prefix}.")
    # click.echo(f"Suffix: {suffix}.")
    # click.echo(f"Low memory: {low_memory}.")

    if low_memory:
        return rename_low_memory(directory, regex, pattern, prefix, suffix)

    files = os.listdir(directory)

    matches = [f for f in files if os.path.isfile(f) and re.search(regex, f) is not None]
    matches_copy = matches[::]

    click.echo(f"Found {len(matches)} files!")

    if not matches:
        click.echo("No files found")
        return
    # click.echo(matches)

    if prefix:
        click.echo(f"Adding prefix={prefix}")
        matches = [add_prefix(match, prefix) for match in matches]

    if suffix:
        click.echo(f"Adding suffix={suffix}")
        matches = [add_suffix(match, suffix) for match in matches]

    if pattern:
        pattern = pattern[0]
        click.echo(f"Replacing pattern,with ={pattern}")
        matches = [replace_pattern(match, pattern) for match in matches]

    # click.echo(f"New files: {matches}")
    # click.echo(matches_copy)
    # click.echo(matches)

    # click.echo(list(map(os.rename, matches_copy, matches)))
    list(map(os.rename, matches_copy, matches))

    click.echo("Finished")

# TODO: Implement low memory option with generators os.walk
def rename_low_memory(directory, regex, pattern, prefix, suffix):

    click.echo("Welcome to the low memory option!")


def add_prefix(filename, prefix):
    return prefix + filename

def add_suffix(filename, suffix):

    filename = filename.split(".")
    ext = filename[-1] if len(filename) > 1 else None

    new_filename = filename[0] + suffix

    return new_filename + "." + ext if ext else new_filename

def replace_pattern(filename, pattern):
    pat, tern = pattern
    return re.sub(pat, tern, filename)
