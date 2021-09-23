import click

from .identifier import main as identifier
import ciphertool.ciphers.vigenere_cipher as vigenere

ciphers = {"vigenere": vigenere}


def cipher_name_argument(function):
    function = click.argument(
        "cipher_name",
        type=click.Choice(tuple(ciphers.keys()), case_sensitive=False),
        required=True,
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


@click.group()
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
    "-o",
    "--output",
    "output_file",
    type=click.File(mode="wt"),
    default=None,
    help="File for output text to be written to.",
)
@click.pass_context
def cli(ctx, raw_text, text_file, output_file):
    """
    Utility for encoding, decoding, and cracking text using common ciphers.
    """

    ctx.ensure_object(dict)

    if raw_text is not None:
        ctx["text"] = raw_text
    elif text_file is not None:
        ctx["text"] = text_file.read()
    else:
        pass
        # ctx["text"] = click.prompt("Text")


@cli.command()
@cipher_name_argument
@key_option
@click.pass_context
def encode(ctx, cipher_name, key):
    output_text = cipher.encode(text, key)


@cli.command()
@cipher_name_argument
@key_option
@click.pass_context
def decode(ctx, cipher_name, key):
    output_text = cipher.decode(text, key)


@cli.command()
@cipher_name_argument
@click.pass_context
def crack(ctx, cipher_name):
    output_text = cipher.crack(text)


@cli.command()
@click.pass_context
def identify(ctx):
    identifier()


if __name__ == "__main__":
    cli()
