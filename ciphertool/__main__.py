import click

from ciphertool.identifier import main as identifier
import ciphertool.ciphers.vigenere_cipher as vigenere

ciphers = {"vigenere": vigenere}


def cipher_name_argument(function):
    function = click.argument(
        "cipher_name",
        type=click.Choice(tuple(ciphers.keys()), case_sensitive=False),
        required=True,
    )(function)
    return function


def input_options(function):
    function = click.option(
        "-t",
        "--text",
        "raw_text",
        type=str,
        default=None,
        help="Text to be processed.",
    )(function)
    function = click.option(
        "-i",
        "--input",
        "text_file",
        type=click.File(),
        default=None,
        help="File containing text to be processed.",
    )(function)
    return function


def output_options(function):
    function = click.option(
        "-o",
        "--output",
        "output_file",
        type=click.File(mode="wt"),
        default=None,
        help="File for output text to be written to. Stdout used if no file specified.",
    )(function)
    return function


def key_option(function):
    function = click.option(
        "-k",
        "--key",
        type=str,
        default=None,
        help="Key to be used in encoding/decoding.",
    )(function)
    return function


def get_text(raw_text, text_file):
    if raw_text is not None:
        text = raw_text
    elif text_file is not None:
        text = text_file.read()
    else:
        text = click.prompt("Text")
    return text


def get_key(key):
    if key is None:
        key = click.prompt("Key")
    return key


def handle_cipher_output(ciphertext=None, plaintext=None, output_file=None):
    if ciphertext is None and plaintext is None:
        raise TypeError("At least one of ciphertext and plaintext must be passed")
    else:
        text = ciphertext if ciphertext is not None else plaintext
        text_type = "Ciphertext" if ciphertext is not None else "Plaintext"
        if output_file is not None:
            output_file.write(text)
            click.echo(f"{text_type} saved to {output_file.name}")
        else:
            click.echo(f"{text_type}: {text}")


@click.group()
def cli():
    """
    Utility for encoding, decoding, and cracking text using common ciphers.
    See help pages for each command for more information.
    """


@cli.command()
@cipher_name_argument
@input_options
@output_options
@key_option
def encode(cipher_name, raw_text, text_file, output_file, key):
    """
    Encode plaintext with a key and choice of cipher.
    """
    text = get_text(raw_text, text_file)
    key = get_key(key)
    ciphertext = ciphers[cipher_name].encode(text, key)
    handle_cipher_output(ciphertext=ciphertext, output_file=output_file)


@cli.command()
@cipher_name_argument
@input_options
@output_options
@key_option
def decode(cipher_name, raw_text, text_file, output_file, key):
    """
    Decode ciphertext with a known key and cipher.
    """
    text = get_text(raw_text, text_file)
    key = get_key(key)
    plaintext = ciphers[cipher_name].decode(text, key)
    handle_cipher_output(plaintext=plaintext, output_file=output_file)


@cli.command()
@cipher_name_argument
@input_options
@output_options
def crack(cipher_name, raw_text, text_file, output_file):
    """
    Crack ciphertext with an unknown key but known cipher.
    """
    text = get_text(raw_text, text_file)
    plaintext = ciphers[cipher_name].crack(text)
    handle_cipher_output(plaintext=plaintext, output_file=output_file)


@cli.command()
@input_options
def identify(raw_text, text_file):
    """
    Identify the cipher used to encode some ciphertext.
    """
    text = get_text(raw_text, text_file)
    identifier(text)


if __name__ == "__main__":
    cli()
