#!/usr/bin/env ruby
#Script should output: [SENDER],[RECEIVER],[FLAGS]
pattern = /\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/

input_string = ARGV[0]

matches = input_string.scan(pattern)

puts matches.map { |match| match.join(',') }.join(',')
