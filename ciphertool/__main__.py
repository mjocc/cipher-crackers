import click

import ciphertool.ciphers.vigenere_cipher as vignere

ciphers = {"vignere": vignere}


@click.command()
@click.argument(
    "operation",
    type=click.Choice(("encode", "decode", "crack"), case_sensitive=False),
    required=True,
)
@click.argument(
    "cipher",
    type=click.Choice(tuple(ciphers.keys()), case_sensitive=False),
    required=True,
)
@click.option(
    "-t",
    "--text",
    required=True,
    prompt=True,
    help="Text to be processed.",
)
@click.option(
    "-k",
    "--key",
    default=None,
    prompt=True,
    prompt_required=False,
    help="Key to be used in encoding/decoding.",
)
def cli(operation, cipher, text, key):
    """
    Utility for encoding, decoding, and cracking text using common ciphers.
    """
    click.echo("Hello World!")


if __name__ == "__main__":
    cli()
