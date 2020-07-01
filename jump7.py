#!/usr/bin/env python3
for i in rang(1,101):
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        continue
    print(i)
