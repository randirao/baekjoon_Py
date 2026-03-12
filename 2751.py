import sys

N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort()
sys.stdout.write('\n'.join(map(str, lst)))