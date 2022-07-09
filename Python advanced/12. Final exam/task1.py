from collections import deque

eggs_size = deque([int(x) for x in input().split(", ")])
papers_size = [int(x) for x in input().split(", ")]

filled_boxes = 0
box_size = 50

while eggs_size and papers_size:
    current_egg = eggs_size.popleft()
    current_paper = papers_size.pop()

    if current_egg <= 0:
        papers_size.append(current_paper)
        continue
    if current_egg == 13:
        first_paper = papers_size[0]
        papers_size.pop(0)
        papers_size.insert(0,current_paper)
        papers_size.append(first_paper)
        continue
    sum_of_them = current_egg + current_paper
    if sum_of_them <= box_size:
        filled_boxes += 1

if filled_boxes >= 1:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_size])}")
if papers_size:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers_size])}")