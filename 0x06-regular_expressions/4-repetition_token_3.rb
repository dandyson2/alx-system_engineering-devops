#!/usr/bin/env ruby
#Ruby script that accepts one argument and pass it to a regular expression matching method
#Regex should not contain square brackets
pattern = ARGV[0]
matches = pattern.scan(/hbt*n/)
puts matches.join
