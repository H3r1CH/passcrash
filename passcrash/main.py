"""Provides a way to identify a hash, create a hash, and crack a hash"""
import hashlib
import typer


app = typer.Typer()


__version__ = "0.1.0"


def version_callback(value: bool):
    """Version callback function to get the version"""
    if value:
        typer.echo(f"hashcrash: {__version__}")
        raise typer.Exit()


@app.callback()
def main(version: bool = typer.Option(None, "--version", 
callback=version_callback, is_eager=True, help="Show current version of hashcrash")):
    """Callback function to get the version"""
    return version


@app.command("list")
def list_hashes():
    """List the available hash types to use."""
    hash_list = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
    print('-' * 7)
    for i in hash_list:        
        print(i)
    print('-' * 7)


@app.command("hash")
def hash_time(algo: str = typer.Argument(..., help="Specify the hashing algorithm to use"),
 text: str = typer.Argument(..., help="Specify the text you want to hash.")):
    """Hash a given string with a specified hash type."""
    if algo == 'md5':
        print(hashlib.md5(text.encode('utf-8')).hexdigest())
    elif algo == 'sha1':
        print(hashlib.sha1(text.encode('utf-8')).hexdigest())
    elif algo == 'sha224':
        print(hashlib.sha224(text.encode('utf-8')).hexdigest())
    elif algo == 'sha256':
        print(hashlib.sha256(text.encode('utf-8')).hexdigest())
    elif algo == 'sha384':
        print(hashlib.sha384(text.encode('utf-8')).hexdigest())
    elif algo == 'sha512':
        print(hashlib.sha512(text.encode('utf-8')).hexdigest())
    else:
        print('[-] Not a valid hash type.')
        print('[+] Available hashes:')
        list_hashes()


if __name__ == "__main__":
    app()
