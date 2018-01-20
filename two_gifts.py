
import csv
import sys

filename = sys.argv[1]
target_sum = int(sys.argv[2])


with open(sys.argv[1], 'r') as f:
  reader = csv.reader(f)
  _list = list(reader)

potential_sum = 0
x_index = 0
y_index = 0
for x in range(0, len(_list)):
  number = int(_list[x][1])
  for y in range(x, len(_list)):
      next_number = int(_list[y][1])
      temp_sum = number + next_number
      if(temp_sum==target_sum):
          if(x!=y):
            print _list[x][0] + _list[x][1]+", "+ _list[y][0] + _list[y][1]
            sys.exit()
      if(temp_sum<target_sum):
        if(temp_sum>potential_sum):
          potential_sum = temp_sum
          x_index = x
          y_index = y

if(x_index==y_index):
  print "Not possible"
  sys.exit()

print _list[x_index][0] + _list[x_index][1]+", "+ _list[y_index][0] + _list[y_index][1]
sys.exit()