#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters
regex = /[A-Z]/
input_string = ARGV[0]

matches = input_string.scan(regex)
puts matches.join
