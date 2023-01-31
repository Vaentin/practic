from math import ceil 
L, W, H = map(int,input().split())
print(ceil((L*H + W*H)*2 /16))