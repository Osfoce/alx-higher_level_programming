#!/usr/bin/python3
for i in range(0, 10):
    for x in range(1, 10):
        if x != i or i == x:
             print(f"{i}{x}", end=', ')
