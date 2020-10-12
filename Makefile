.PHONY: prepare run

prepare:
	pyenv install

run:
	echo 'Loading Beige'

server:
	cd api && python server.py
