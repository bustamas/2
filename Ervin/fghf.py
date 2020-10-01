def kifest(kep, x, y):
    if y < 0 or x < 0 or y >= len(kep) or x >= len(kep[0]):
        return
    if kep[y][x] != ' ':
        return
    kep[y][x] = '*'
    kifest(kep, x, y - 1)
    kifest(kep, x, y + 1)
    kifest(kep, x - 1,y )
    kifest(kep, x + 1,y )
 
def main():
    z4qqq = [
        list("                               "),
        list("            xx   xx            "),
        list("       xxxx x xxx x xxxx       "),
        list("      xx  x x     x x  xx      "),
        list("    xxx  xx x     x xx  xxx    "),
        list("  xxx    x  x     x  x    xxx  "),
        list("  x      x  x     x  x      x  "),
        list(" xx       xx       xx       xx "),
        list(" x                           x "),
        list(" x                           x "),
        list(" x                           x "),
        list(" x                           x "),
        list(" x                           x "),
        list(" xx    xx             xx    xx "),
        list("  x   x  x xx     xx x  x   x  "),
        list("  xxx  x x x x   x x x x  xxx  "),
        list("    xx x xxx xx xx xxx x xx    "),
        list("     xxx      x x      xxx     "),
        list("              xxx              "),
        list("                               "),
    ]
 
    kifest(z4qqq, 1, 12);
    
    for sor in z4qqq:
        print("".join(sor))
 
main()