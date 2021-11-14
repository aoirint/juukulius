.PHONY: build
build:
	docker buildx build . -t juukulius

.PHONY: run
run: build
	docker run --rm -it -v "$(PWD)/data:/data" juukulius $(O)
