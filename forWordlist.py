#!/usr/bin/python3

import sys

numbers = ["123","1234","12345","321","4321","54321"]
sim = ["@","!","#","/","$","%","!@#"]

for d in range(1900,2026):
    numbers.append(str(d))
param = sys.argv[1].split(",")

def items(a):
    i = 0
    b = 0
    c = 0
    while i < len(a):
        while c < len(numbers):
            word = a[i] + numbers[c]
            with open("words.txt","a") as f:
                f.write(word + "\n")
            c = c + 1
        c = 0
        i = i + 1
    i = 0
    b = 0
    c = 0
    while i < len(a):
        while b < len(sim):
            while c < len(numbers):
                word = a[i] + sim[b] + numbers[c]
                with open("words.txt","a") as f:
                    f.write(word + "\n")
                c = c + 1
            c = 0
            b = b + 1
        b = 0
        i = i + 1
    i = 0
    b = 0
    c = 0
    while i < len(a):
        while b < len(sim):
            while c < len(numbers):
                word = sim[b] + a[i] + numbers[c]
                with open("words.txt","a") as f:
                    f.write(word + "\n")
                c = c + 1
            c = 0
            b = b + 1
        b = 0
        i = i + 1
    i = 0
    b = 0
    c = 0
    v = 0
    while i < len(a):
        while b < len(sim):
            while c < len(numbers):
                while v < len(sim):
                    word = sim[v] + a[i] + sim[b] + numbers[c]
                    with open("words.txt","a") as f:
                        f.write(word + "\n")
                    v = v + 1
                v = 0
                c = c + 1
            c = 0
            b = b + 1
        b = 0
        i = i + 1
    i = 0
    b = 0
    c = 0
    v = 0
    while i < len(a):
        while b < len(sim):
            while c < len(numbers):
                while v < len(sim):
                    word = sim[v] + a[i] + numbers[c] + sim[b]
                    with open("words.txt","a") as f:
                        f.write(word + "\n")
                    v = v + 1
                v = 0
                c = c + 1
            c = 0
            b = b + 1
        b = 0
        i = i + 1

items(param)
