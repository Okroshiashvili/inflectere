# Work In Progress!!!

# Inflectere

Inflectere - From Latin to English - "to bend, to shape, to form"

Inflectere is a small Python library to inflect words in English.
Specifically, to convert a word from singular to plural, and vice versa.

## Installation

```bash
pip install inflectere
```

## Usage

```python
from inflectere import Inflectere

inflect = Inflectere()

inflect.pluralize("cat")  # cats
inflect.singularize("cats")  # cat
```

## Why Yet Another Inflector?

There are many inflectors out there, but I couldn't find one that
was simple, easy to use, and had a small footprint.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT

## Changelog

See the [CHANGELOG](CHANGELOG.md) file.

## Documentation

Inflectere documentation is built using [Sphinx](https://www.sphinx-doc.org) and is hosted on [Read the Docs](https://readthedocs.org/).

To build the documentation make sure you have the dependencies installed: from the root directory: `pip install -r docs/requirements.txt`.

Now you can build the docs using: `sphinx-build -b html docs build`

## Credits

This library is inspired by the following libraries:

- [inflect](https://github.com/jaraco/inflect)
- [pluralize](https://github.com/plurals/pluralize)
- [pluralizer-py](https://github.com/weixu365/pluralizer-py)
