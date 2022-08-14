# passcrash
CLI Password Cracker and Hasher

## Installation
```bash
pip install https://github.com/H3r1CH/passcrash/releases/download/v0.1.0/passcrash-0.1.0-py3-none-any.whl
```

### Help
```bash
passcrash --help

 Usage: passcrash [OPTIONS] COMMAND [ARGS]...

 Callback function to get the version

┌─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ --version                     Show current version of hashcrash                                                 │
│ --install-completion          Install completion for the current shell.                                         │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.  │
│ --help                        Show this message and exit.                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
┌─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ hash        Hash a given string with a specified hash type.                                                     │
│ list        List the available hash types to use.                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## List

### Example
```bash
passcrash list
-------
md5
sha1
sha224
sha256
sha384
sha512
-------
```

## Hash

### Help
```bash
passcrash hash --help

 Usage: passcrash hash [OPTIONS] ALGO TEXT

 Hash a given string with a specified hash type.

┌─ Arguments ─────────────────────────────────────────────────────────────────────────────────────┐
│ *    algo      TEXT  Specify the hashing algorithm to use [default: None] [required]            │
│ *    text      TEXT  Specify the text you want to hash. [default: None] [required]              │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
┌─ Options ───────────────────────────────────────────────────────────────────────────────────────┐
│ --help          Show this message and exit.                                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Example
```bash
passcrash hash md5 password123
482c811da5d5b4bc6d497ffa98491e38
```
