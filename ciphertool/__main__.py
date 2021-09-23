import click

from .identifier import main as identify
import ciphertool.ciphers.vigenere_cipher as vigenere

ciphers = {"vigenere": vigenere}


@click.command()
@click.argument(
    "operation",
    type=click.Choice(("encode", "decode", "crack", "identify"), case_sensitive=False),
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
@click.option(
    "-o",
    "--output",
    "output_file",
    type=click.File(mode="wt"),
    default=None,
    help="File for output text to be written to."
)
def cli(operation, cipher_name, raw_text, text_file, key, output_file):
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
        output_text = cipher.encode(text, key)
    elif operation == "decode":
        output_text = cipher.decode(text, key)
    elif operation == "crack":
        output_text = cipher.crack(text)
    elif operation == "identify":
        identify()
    else:
        click.echo("Something went wrong. Please try again.")

    text_type = 'Ciphertext' if operation == 'encode' else 'Plaintext'

    if output_file is not None:
        output_file.write(output_text)
        click.echo(f'{text_type} saved to {output_file.name}')
    else:
        click.echo(f"{text_type}: {output_text}")

if __name__ == "__main__":
    cli()
