#! /usr/bin/env python3

elfs = [[]]
elfnum = 0
elfs[elfnum] = []
with open("input.txt", "r") as fin:
    for line in fin:
        if line == "\n":
            elfnum = elfnum+1
            elfs.append([])
        else:
            nums = [int(s) for s in line.split() if s.isdigit()]
            for num in nums:
                elfs[elfnum].append(num)

sumcals = []
for elf in elfs:
    sumcals.append(sum(elf))
            
maxcals = [max(sumcals)]
print("maxcals: ", maxcals[0])

sumcals.remove(maxcals[0])
maxcals.append(max(sumcals))

sumcals.remove(maxcals[1])
maxcals.append(max(sumcals))

top3cals = sum(maxcals)
print("top3cals: ", top3cals)


