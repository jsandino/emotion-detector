init:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	pytest .

run:
	python3.11 server.py