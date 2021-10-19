
build:
	docker build -t dac .

test:
	docker run -ti --rm -v "$(shell pwd)":/app dac:latest bash -c "/app/test.sh "
