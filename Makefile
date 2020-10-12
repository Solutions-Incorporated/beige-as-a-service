.PHONY: prepare run

prepare:
	pyenv install

server:
	cd api && python server.py
