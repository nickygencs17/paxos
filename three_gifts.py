
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
z_index = 0
for x in range(0, len(_list)):
  number = int(_list[x][1])
  for y in range(x, len(_list)):
    next_number = int(_list[y][1])
    for z in range(y, len(_list)):
        next_next_number=int(_list[z][1])
        temp_sum = number + next_number + next_next_number
        if(temp_sum==target_sum):
            if(x!=y and x!=z and y!=z):
                print _list[x][0] + _list[x][1]+", "+ _list[y][0] + _list[y][1] + ", "+ _list[z][0] + _list[z][1]
                sys.exit()
        if(temp_sum<target_sum):
          if(x!=y and x!=z and y!=z):
            if(temp_sum>potential_sum):
                potential_sum = temp_sum
                x_index = x
                y_index = y
                z_index = z

if(x_index==y_index or x_index==z_index or y_index==z_index):
  print "Not possible"
  sys.exit()

print _list[x_index][0] + _list[x_index][1]+", "+ _list[y_index][0] + _list[y_index][1]+ ", "+ _list[z_index][0] + _list[z_index][1]
sys.exit()