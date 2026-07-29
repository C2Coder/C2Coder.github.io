.PHONY: build serve serve-live

build:
	python build.py

serve: build
	python -m http.server 8000 --directory dist

serve-live:
	python build.py --serve
