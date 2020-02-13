
all: build dist

.PHONY: build
build:
	rm -rf dist
	pipenv run python setup.py sdist bdist_wheel

.PHONY: dist
dist:
	pipenv run twine upload dist/*

.PHONY: setup
setup:
	pipenv run pip install --upgrade twine setuptools wheel
