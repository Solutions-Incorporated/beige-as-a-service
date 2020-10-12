MAKEFLAGS += -j2

.PHONY: prepare run client server

prepare:
	pyenv install 
	
run: server client
	@echo 'Loading Beige'

server:
	cd api && pip install -r requirements.txt && python server.py

client: 
	cd client && npm install && npm run dev
