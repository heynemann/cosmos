# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

.PHONY: build

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | egrep -v '[_].*' | sort"
# required for list
no_targets__:

# install all dependencies
setup:
	@npm install -g nodemon babel-cli webpack mocha
	@npm install

build:
	@rm -rf lib/
	@webpack

_services: _services-shutdown
	@docker-compose -p cosmos -f ./docker/docker-compose.yml up -d

_services-shutdown:
	@docker-compose -p cosmos -f ./docker/docker-compose.yml stop
	@docker-compose -p cosmos -f ./docker/docker-compose.yml rm -f

# test your application (tests in the test/ directory)
test: _test-unit

test-watch: _services
	@./node_modules/mocha/bin/mocha --watch --require babel-polyfill --compilers js:babel-core/register test/**/*Test.js

_test-unit: _services _test-unit-coverage

_test-unit-watch: _services
	@./node_modules/mocha/bin/mocha --watch --require babel-polyfill --compilers js:babel-core/register test/unit/**/*Test.js

_test-unit-coverage:
	@./node_modules/.bin/babel-node node_modules/.bin/babel-istanbul cover node_modules/.bin/_mocha --report text --check-coverage -- -u tdd test/unit/**/*Test.js
	#@env NODE_ENV=test NODE_CONFIG_DIR=`pwd`/config ./node_modules/.bin/nyc ./node_modules/.bin/ava ./test/unit/**/*Test.js
	@$(MAKE) _test-unit-coverage-html

_test-unit-coverage-html:
	#@./node_modules/.bin/babel-node node_modules/.bin/babel-istanbul report --include=./coverage/coverage.json html
	@./node_modules/.bin/nyc report -r html

static-analysis:
	@./node_modules/.bin/plato -r -e .eslintrc -d report src/
	@open ./report/index.html

run: services _run-app

_run-app:
	@nodemon --exec babel-node --presets=es2015 -- src/cmd.js start
