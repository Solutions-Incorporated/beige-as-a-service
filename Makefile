MAKEFLAGS += -j2

.PHONY: prepare run client

prepare:
	pyenv install
	cd api && pip install -r requirements.txt

run: server client
	@echo 'Loading Beige'


server:
	cd api && python server.py

client: 
	cd client && npm install && npm run dev
