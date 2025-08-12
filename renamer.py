import click
import os
import re

@click.command()
@click.argument("directory")
@click.argument("regex")
@click.option("--replace", "-r", "pattern", type=(str, str))
@click.option("--prefix", "-p", "prefix")
@click.option("--suffix", "-s", "suffix")
@click.option("--low-memory", "low_memory", is_flag=True)
def rename(directory, regex, pattern, prefix, suffix, low_memory):

    if low_memory:
        return rename_low_memory(directory, regex, pattern, prefix, suffix)

    files = os.scandir(directory)

    matches = [file.name for file in files if file.is_file()
                                        and re.search(regex, file.name) is not None]
    matches_copy = matches[::]

    if not matches:
        click.echo("No files found")
        return

    # Generate new list of names in order
    if prefix:
        matches = [add_prefix(match, prefix) for match in matches]

    if suffix:
        matches = [add_suffix(match, suffix) for match in matches]

    if pattern:
        matches = [replace_pattern(match, pattern) for match in matches]

    # apply new names in order
    list(map(os.rename, matches_copy, matches))

def rename_low_memory(directory, regex, pattern, prefix, suffix):

    for file in rename_lm_generator(directory, regex):
        new_name = file.name

        if prefix:
            new_name = add_prefix(new_name, prefix)

        if suffix:
            new_name = add_suffix(new_name, suffix)

        if pattern:
            new_name = replace_pattern(new_name, pattern)

        os.rename(file.path, new_name)

def rename_lm_generator(directory, regex):
    for file in os.scandir(directory):
        if file.is_file() and re.search(regex, file.name) is not None:
            yield file

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
