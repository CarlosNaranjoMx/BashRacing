'''
import sys

while(True):
	line = sys.stdin.readline().split()
	if line == []:
		break
'''
arrayhash = []
#total = 0

d = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}

n = int(input())

def arrhash():
    global n
    for i in range(n):
        l = int(input())
        total = 0
        for j in range(l):
            arrayhash = input()
        for k in range(len(arrayhash)):
            total += int(d.get(arrayhash[k])) + j + k 
        print(total)


arrhash()



