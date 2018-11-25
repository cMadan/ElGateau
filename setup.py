# pip
# build instructions
#
# python setup.py sdist bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# twine upload dist/*

import setuptools

setuptools.setup(
    name="ElGateau",
    version="1.0.0",
    author="Christopher Madan",
    author_email="christopher.madan@nottingham.ac.uk",
    description="A Library for Using the Elgato Stream Deck for Experimental Psychology Research",
    long_description="In experimental psychology research, we often ask participants to press specific keys to correspond to responses in the experiment. For instance, one key for 'old' and another for 'new' in an old/new recognition memory test, 'word' and 'nonword' in a lexical decision task, or red/green/blue in a Stroop test. Sometimes we put stickers over keys on a keyboard to remind participants of these key mappings, but often they are merely included as part of the experiment instructions. What if we could easily just write 'old' and 'new' on the keys themselves? This approach could additionally lead to more manageable (and automatically logged) counterbalancing across participants, but we could further readily counterbalance key mappings across trials (or blocks of trials) if desired. In some cases, a whole experiment could be implemented on an LCD keypad. This project is the infrastructure for implementing experiments with an LCD keypad called the Elgato Stream Deck.",
    url="https://github.com/cMadan/ElGateau",
    install_requires = ['hidapi','Pillow'],
	platforms = "any",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
)
