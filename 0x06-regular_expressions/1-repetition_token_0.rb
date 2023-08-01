#!/usr/bin/env ruby
#Ruby script that accepts one argument and pass it to a regular expression matching method
pattern = ARGV[0]
matches = pattern.scan(/hbt{2,5}n/)
puts matches.join
