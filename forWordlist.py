#!/usr/bin/python3

import sys

def combinacao1(nomes, nums):
    for nome in nomes:
        for num in nums:
            with open("words.txt", "a") as f:
                f.write(nome + num + "\n")

def combinacao2(nomes, nums):
    for nome in nomes:
        for num1 in nums:
            for num2 in nums:
                with open("words.txt", "a") as f:
                    f.write(nome + num1 + num2 + "\n")
                    f.write(num1 + nome + num2 + "\n")

def combinacao3(nomes, nums, sims):
    for nome in nomes:
        for sim in sims:
            for num in nums:
                with open("words.txt", "a") as f:
                    f.write(sim + nome + num + "\n")
                    f.write(nome + sim + num + "\n")
                    f.write(nome + num + sim + "\n")

def combinacao4(nomes, nums, sims):
    for nome in nomes:
        for sim1 in sims:
            for num in nums:
                for sim2 in sims:
                    with open("words.txt", "a") as f:
                        f.write(sim1 + nome + sim2 + num + "\n")
                        f.write(nome + sim1 + num + sim2 + "\n")
                        f.write(sim1 + nome + num + sim2 + "\n")

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
    print("\t./forWordlist.py <words,separeted,list> <complexity level>")
    print("\tExample:")
    print("\t./forWordlist.py rich,richard,1207 2\n\n")

def main():
    nums = ["123", "1234", "12345", "321", "4321", "54321"]
    if int(sys.argv[3]) == 2:
        nums.extend([str(d) for d in range(1900, 2026)])
    if int(sys.argv[3]) == 3:
        nums.extend([str(c) for c in range(0, 999)])
    if int(sys.argv[3]) == 4:
        nums.extend([str(d) for d in range(1900, 2026)])
        nums.extend([str(c) for c in range(0, 999)])
    sims = ["@", "!", "_", "#", "/", "$", "%", "!@#"]
    try:
    	param = sys.argv[1].split(",")
    	nomes = [q for q in param if not q.isdigit()]
    	nomes += [q.capitalize() for q in nomes]
    	nums.extend([q for q in param])

    	match int(sys.argv[2]):
            case 1:
            	combinacao1(nomes,nums)
            case 2:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums)
            case 3:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums)
            	combinacao3(nomes,nums,sims)
            case 4:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums)
            	combinacao3(nomes,nums,sims)
            	combinacao4(nomes,nums,sims)
            case 5:
            	combinacao1(nomes,nums)
            	combinacao2(nomes,nums)
            	combinacao3(nomes,nums,sims)
            	combinacao4(nomes,nums,sims)
            	combinacao5(nomes,nums,sims)
    except IndexError:
    	help()
if __name__ == "__main__":
    main()
