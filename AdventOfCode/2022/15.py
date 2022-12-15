file = open("input.txt")
lines = [line.strip() for line in file.readlines()]
file.close()


# part 1
def part_1():
    wrow = 2000000
    seen = set()
    for line in lines:
        tokens = line.split()
        sx, sy, bx, by = tokens[2], tokens[3], tokens[8], tokens[9]
        sx = int(sx[2:-1])
        sy = int(sy[2:-1])
        bx = int(bx[2:-1])
        by = int(by[2:])
        md = abs(sx - bx) + abs(sy - by)
        vd = abs(sy - wrow)
        if md >= vd:
            hd = md - vd
            for i in range(sx - hd, sx + hd + 1):
                seen.add(i)
    return len(seen)


# part 2
def part_2():
    boxes = []
    for line in lines:
        tokens = line.split()
        sx, sy, bx, by = tokens[2], tokens[3], tokens[8], tokens[9]
        sx = int(sx[2:-1])
        sy = int(sy[2:-1])
        bx = int(bx[2:-1])
        by = int(by[2:])
        md = abs(sx - bx) + abs(sy - by)
        boxes.append((sx, sy, md))
    for i in range(len(boxes)):
        sx, sy, md = boxes[i]
        for dx in range(md + 2):
            dy = (md + 1) - dx
            for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                x = sx + (dx * signx)
                y = sy + (dy * signy)
                if 0 <= x <= 4000000 and 0 <= y <= 4000000:
                    def good(xcoor, ycoor):
                        for j in range(len(boxes)):
                            ssx, ssy, mmd = boxes[j]
                            if abs(xcoor - ssx) + abs(ycoor - ssy) <= mmd:
                                return False
                        return True

                    if good(x, y):
                        return x * 4000000 + y


if __name__ == '__main__':
    print(part_1())
    print(part_2())
