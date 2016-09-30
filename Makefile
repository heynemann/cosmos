# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies (do not forget to create a virtualenv first)
setup:
	@npm install -g nodemon babel-cli webpack
	@npm install

services: services-shutdown
	@docker-compose -p cosmos -f ./docker/docker-compose.yml up -d

services-shutdown:
	@docker-compose -p cosmos -f ./docker/docker-compose.yml stop
	@docker-compose -p cosmos -f ./docker/docker-compose.yml rm -f

# test your application (tests in the tests/ directory)
#test: test-redis unit

#unit:

# show coverage in html format
#coverage-html: unit
	#@coverage html

# get a redis instance up for your unit tests (localhost:4448)
test-redis: test-redis-shutdown
	@redis-server ./redis.tests.conf; sleep 1
	@redis-cli -p 4448 info > /dev/null

# kill the test redis instance (localhost:4448)
test-redis-shutdown:
	@-redis-cli -p 4448 shutdown

run: services
	@nodemon --exec babel-node --presets=es2015 -- src/main.js
