#!/usr/bin/python
# -*- coding: utf-8 -*-


def devided_into_hourglasses(arr):
    hourglass_sum_list = []
    for a in xrange(4):
        for b in xrange(4):
            count_x = 0
            hourglass_sum = 0
            for x in range(a, a + 3):
                count_y = 0
                count_x += 1
                for y in range(b, b + 3):
                    count_y += 1

            	    # skip 2nd row's 1st col and 3rd col
                    if count_x == 2 and (count_y == 1 or count_y == 3):
                        continue
                    hourglass_sum += arr[x][y]
            hourglass_sum_list.append(hourglass_sum)

    max_hourglass_sum(hourglass_sum_list)


def max_hourglass_sum(hourglass_sums):
    print max(hourglass_sums)


arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

devided_into_hourglasses(arr)
			
