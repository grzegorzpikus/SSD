import datetime

class Towers:

    def __init__(self, disks=3):
        self.disks = disks
        self.towers = [[], [], []]
        self.towers[0] = [i for i in range(self.disks, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []

    def move(self, start_tower, end_tower):
        disk = self.towers[start_tower].pop()
        self.towers[end_tower].append(disk)


def Hanoi_towers(towers, n, start_tower, end_tower, mid_tower, count=0):

    if n == 0:
        return count

    count = Hanoi_towers(towers, n - 1, start_tower, mid_tower, end_tower, count)
    towers.move(start_tower, end_tower)
    count += 1
    count = Hanoi_towers(towers, n - 1, mid_tower, end_tower, start_tower, count)
    return count

print(datetime.datetime.now())
towers_x = Towers(26)
result_x = Hanoi_towers(towers_x, towers_x.disks, 0, 2, 1, 0)
print(result_x)
print(datetime.datetime.now())