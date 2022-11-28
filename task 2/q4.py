input = input()
list = input.split()

noDubs = [*set(list)]
noDubs.sort()
print(noDubs)