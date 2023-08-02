#!/usr/bin/env ruby
#Ruby script that accepts one argument and pass it to a regular expression matching method
regex = /h.n/
input_string = ARGV[0]

matches = input_string.scan(regex)
puts matches.join
