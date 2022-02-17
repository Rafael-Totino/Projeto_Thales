install:
	python -m pip install --upgrade pip setuptools virtualenv
	python -m virtualenv kivy_venv
	pip install tk
	kivy_venv\Scripts\activate
