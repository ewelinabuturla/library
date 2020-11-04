#!/bin/sh                                                                                                              
pytest --ds=library.settings --cov=library_apps --capture=no --nomigrations --cov-config=.coveragerc $@ && \
flake8 . --exclude=migrations --exclude=venv --max-line-length=100
