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
	echo "Setting up all dependencies..."

# test your application (tests in the tests/ directory)
#test: test-redis unit

#unit:

# show coverage in html format
#coverage-html: unit
	#@coverage html

# get a redis instance up (localhost:4444)
redis: redis-shutdown
	redis-server ./redis.conf; sleep 1
	redis-cli -p 4444 info > /dev/null

# kill this redis instance (localhost:4444)
redis-shutdown:
	-redis-cli -p 4444 shutdown

# get a redis instance up for your unit tests (localhost:4448)
test-redis: test-redis-shutdown
	@redis-server ./redis.tests.conf; sleep 1
	@redis-cli -p 4448 info > /dev/null

# kill the test redis instance (localhost:4448)
test-redis-shutdown:
	@-redis-cli -p 4448 shutdown
