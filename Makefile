VENV = .venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip

run: $(VENV)/Scripts/activate
	$(PYTHON) main.py

$(VENV)/Scripts/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

install:
	pip install -r requirements.txt

build-cf:
	python setup.py build

build-pi:
	pyinstaller --noconfirm --onefile --console --icon "./assets/Logo.ico" --name "vRY" "./main.py" --distpath "./build/pyinstaller" 