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
	@npm install -g nodemon babel-cli webpack mocha
	@npm install

services: services-shutdown
	@docker-compose -p cosmos -f ./docker/docker-compose.yml up -d

services-shutdown:
	@docker-compose -p cosmos -f ./docker/docker-compose.yml stop
	@docker-compose -p cosmos -f ./docker/docker-compose.yml rm -f

# test your application (tests in the tests/ directory)
test: test-unit

test-unit: services test-unit-run

test-unit-run:
	@./node_modules/mocha/bin/mocha --require babel-polyfill --compilers js:babel-core/register test/unit/**/*Test.js

# show coverage in html format
#coverage-html: unit
	#@coverage html

run: services run-app

run-app:
	@nodemon --exec babel-node --presets=es2015 -- src/cmd.js start
