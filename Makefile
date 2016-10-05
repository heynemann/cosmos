# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

.PHONY: build

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies
setup:
	@npm install -g nodemon babel-cli webpack mocha
	@npm install

build:
	@rm -rf lib/
	@webpack

services: services-shutdown
	@docker-compose -p cosmos -f ./docker/docker-compose.yml up -d

services-shutdown:
	@docker-compose -p cosmos -f ./docker/docker-compose.yml stop
	@docker-compose -p cosmos -f ./docker/docker-compose.yml rm -f

# test your application (tests in the test/ directory)
test: test-unit

test-watch: services
	@./node_modules/mocha/bin/mocha --watch --require babel-polyfill --compilers js:babel-core/register test/**/*Test.js

test-unit: services test-unit-coverage

test-unit-watch: services
	@./node_modules/mocha/bin/mocha --watch --require babel-polyfill --compilers js:babel-core/register test/unit/**/*Test.js

test-unit-coverage:
	@./node_modules/.bin/babel-node node_modules/.bin/babel-istanbul cover node_modules/.bin/_mocha --report text --check-coverage -- -u tdd test/unit/**/*Test.js
	@$(MAKE) test-unit-coverage-html

test-unit-coverage-html:
	@./node_modules/.bin/babel-node node_modules/.bin/babel-istanbul report --include=./coverage/coverage.json html

static-analysis:
	@./node_modules/.bin/plato -r -e .eslintrc -d report src/
	@open ./report/index.html

run: services run-app

run-app:
	@nodemon --exec babel-node --presets=es2015 -- src/cmd.js start
