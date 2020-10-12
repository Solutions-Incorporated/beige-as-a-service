MAKEFLAGS += -j2

.PHONY: prepare run

prepare:
	pyenv install

run: server client
	@echo 'Loading Beige'


server:
	cd api && python server.py

client: 
	cd client && npm install && npm run dev