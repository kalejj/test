import textgrid

text_grid = textgrid.TextGrid.fromFile('TextGrid/1.TextGrid')
text_grid
pha = text_grid[1]
phs = []
for iterator, interval in enumerate(pha.intervals):
    if interval.mark == "":
        interval.mark = " "
    mark = interval.mark
    phs.append(mark)
print("".join(phs))
print(len("".join(phs)))