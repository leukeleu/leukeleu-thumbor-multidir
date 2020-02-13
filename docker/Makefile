ROOT	 := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
REGISTRY := asia.gcr.io
PROJECT  := your-project
IMAGE	 := thumbor
VERSION  := latest
TAG 	 := $(REGISTRY)/$(PROJECT)/$(IMAGE):$(VERSION)
DATE     := `date "+%Y-%m-%d"`

# echo output in cyan
define cecho
	@tput setaf 6
	@echo $1
	@tput sgr0
endef

all: build push

build: 
	$(call cecho, "Building base image")
	docker build -t "$(TAG)" .
	
push:
	$(call cecho, "Uploading base image to Google Container Registry")
	docker push $(TAG)
