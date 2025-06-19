install:
	@python -m pip install -r requirements.txt |\
	python3 -m pip install -r requirements.txt

test:
	pytest test.py

serve:
	@uvicorn main:app --reload --port 8080 |\
	echo "INFO:     8080 port was busy, switched to 8085"
	@uvicorn main:app --reload --port 8085