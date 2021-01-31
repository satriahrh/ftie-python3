# Resolving Known Plaintext Attack on FTIE-RT-ACM

![System Block Diagram](docs/assets/system-block-diagram.png)
Project description


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
Python 3.6
Virtualenv
```
pip install virtualenv
```

### Installing

Steps to follow:
1. Clone this repo from master branch https://github.com/hafizhme/ftie-rt-acm
2. From the root project directory, Create a directory for virtual environment
3. Create virtual environment by `virtualenv your-env`
4. Activate the virtual environment.
	for linux : `source your-env/bin/activate`
	for windows : `your-env\Scripts\activate.bat`
5. Install all requirements by `pip install -r requirements.txt`
6. Do command `nosetests` and make sure all test case passed.

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [astroid==1.6.1](https://github.com/PyCQA/astroid) - Abstract syntax tree for Python
* [isort==4.3.3](https://github.com/timothycrosley/isort) - Python library to sort Python imports
* [lazy-object-proxy==1.3.1](https://github.com/ionelmc/python-lazy-object-proxy) - A fast and thorough lazy object proxy.
* [mccabe==0.6.1](https://github.com/pycqa/mccabe) -  Complexity checker for Python
* [nose==1.3.7](https://github.com/nose-devs/nose) - nicer testing for python
* [numpy==1.14.0](http://www.numpy.org/) - Array processing for numbers, strings, records, and objects.
* [Pillow==5.0.0](https://python-pillow.org/) - Python Imaging Library
* [pylint==1.8.2](https://www.pylint.org/) - Python code static checker
* [six==1.11.0](https://github.com/benjaminp/six) - Python 2 and 3 compatibility utilities
* [wrapt==1.10.11](https://github.com/GrahamDumpleton/wrapt) - Provide a transparent object proxy for Python

## Authors

* **Satria H R Harsono** - *Initial work* - [hafizhme](https://github.com/hafizhme)

See also the list of [contributors](https://github.com/hafizhme/ftie-rt-acm/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

