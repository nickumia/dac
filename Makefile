
build:
	docker build -t dac .

lint:
	docker run -ti --rm -v "$(shell pwd)":/app dac:latest bash -c "pip3 install flake8; cd /app && flake8 . --count --show-source --statistics"

test:
	docker run -ti --rm -v "$(shell pwd)":/app dac:latest bash -c "/app/test.sh "
