#!/usr/bin/env lua

-- Read input
local n = io.read("*n", "*l")
local arr = {}

for i = 1, n do
  arr[i] = {}

  for token in string.gmatch(io.read("*l"), "[^%s]+") do
    table.insert(arr[i], tonumber(token:match("(.-)%s*$")))
  end
end

-- Sum the main diagonal of the matrix and substract the sum of the
-- off-diagonal
local sum = 0

for i = 1, n do
  sum = sum + arr[i][i] - arr[i][n + 1 - i]
end

sum = math.abs(sum)

-- Print the result
print(sum)
