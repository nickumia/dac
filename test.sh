pip3 install -e /app -r /app/dev-requirements.txt

cd /app
pytest -s --cov=dac tests
