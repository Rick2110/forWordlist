#!/usr/bin/python3

import sys

def combinacao1(nomes, nums):
    for nome in nomes:
        for num in nums:
            with open("words.txt", "a") as f:
                f.write(nome + num + "\n")

def combinacao2(nomes, nums, sims):
    for nome in nomes:
        for sim in sims:
            for num in nums:
                with open("words.txt", "a") as f:
                    f.write(nome + sim + num + "\n")

def combinacao3(nomes, nums, sims):
    for nome in nomes:
        for sim in sims:
            for num in nums:
                with open("words.txt", "a") as f:
                    f.write(sim + nome + num + "\n")

def combinacao4(nomes, nums, sims):
    for nome in nomes:
        for sim1 in sims:
            for num in nums:
                for sim2 in sims:
                    with open("words.txt", "a") as f:
                        f.write(sim1 + nome + sim2 + num + "\n")

def combinacao5(nomes, nums, sims):
    for nome in nomes:
        for sim1 in sims:
            for num in nums:
                for sim2 in sims:
                    with open("words.txt", "a") as f:
                        f.write(sim1 + nome + num + sim2 + "\n")
def help():
    print("Help Menu")
    print("\tSyntax to use:")
    print("\t./forWordlist <words;separeted;list> <complexity level>")
    print("\tExample:")
    print("\t./forWordlist rich;richard;1207 2\n\n")

def main():
    nums = ["123", "1234", "12345", "321", "4321", "54321"] + [str(d) for d in range(1900, 2026)]
    sims = ["@", "!", "_", "#", "/", "$", "%", "!@#"]
    try:
    	param = sys.argv[1].split(",")
    	nomes = [q for q in param if not q.isdigit()]
    	nomes += [q.capitalize() for q in nomes]
    	nums.extend([q for q in param if q.isdigit()])

    	match int(sys.argv[2]):
            case 1:
            	combinacao1(nomes,nums)
            case 2:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums,sims)
            case 3:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums,sims)
            	combinacao3(nomes,nums,sims)
            case 4:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums,sims)
            	combinacao3(nomes,nums,sims)
            	combinacao4(nomes,nums,sims)
            case 5:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums,sims)
            	combinacao3(nomes,nums,sims)
            	combinacao4(nomes,nums,sims)
            	combinacao5(nomes,nums,sims)
    except IndexError:
    	help()
if __name__ == "__main__":
    main()
