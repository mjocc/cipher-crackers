import click

import ciphertool.ciphers.vigenere_cipher as vigenere

ciphers = {"vignere": vigenere}


@click.command()
@click.argument(
    "operation",
    type=click.Choice(("encode", "decode", "crack"), case_sensitive=False),
    required=True,
)
@click.argument(
    "cipher_name",
    type=click.Choice(tuple(ciphers.keys()), case_sensitive=False),
    required=True,
)
@click.option(
    "-t",
    "--text",
    "raw_text",
    type=str,
    default=None,
    help="Text to be processed.",
)
@click.option(
    "-tf",
    "--textfile",
    "text_file",
    type=click.File(),
    default=None,
    help="File containing text to be processed.",
)
@click.option(
    "-k",
    "--key",
    type=str,
    default=None,
    help="Key to be used in encoding/decoding.",
)
def cli(operation, cipher_name, raw_text, text_file, key):
    """
    Utility for encoding, decoding, and cracking text using common ciphers.
    """
    if raw_text is not None:
        text = raw_text
    elif text_file is not None:
        text = text_file.read()
    else:
        text = click.prompt('Text')

    if (operation == "encode" or operation == "decode") and key is None:
        key = click.prompt('Key')

    cipher = ciphers[cipher_name]

    if operation == "encode":
        cipher.encode(text, key)
    elif operation == "decode":
        cipher.decode(text, key)
    elif operation == "crack":
        cipher.crack(text)
    else:
        click.echo("Something went wrong. Please try again.")


if __name__ == "__main__":
    cli()
