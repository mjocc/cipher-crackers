# cipher-crackers

## To install

### For production

Download latest release from releases on the right  
Install it with pip
```shell
$ pip install ciphertool-0.1.0.tar.gz
```

### For development

Create a virtual env and activate it
```shell
$ python -m venv env
$ source env/bin/activate
```

Install wheel
```shell
$ pip install wheel
```

Install package
```shell
$ pip install .
```

Build for production
```shell
$ python setup.py sdist
```

Publish to GitHub releases (only works with valid gh credentials and gh cli)
```shell
$ gh release create vx.x.x ./dist/*.tar.gz
```

## To run

Use the command `ciphertool`  
For how to use
```shell
$  ciphertool --help
```
