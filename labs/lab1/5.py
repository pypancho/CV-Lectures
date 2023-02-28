# Practice 5
# Time for some fake graphics! Let’s say we want to draw game boards.
def drawboard():
    size = input("What size do you want to draw?")
    size = int(size)
    i = 0
    ho = "--- "
    ve = "|   "
    ho = ho * size
    ve = ve * (size+1)
    while i < size+1:
        print (ho)
        if not (i == size):
            print (ve)
        i += 1

drawboard()