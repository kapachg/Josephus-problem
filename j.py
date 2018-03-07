# This is an implementation of the mathematical algorithm

def survivor(N):           # Returns the position of the survivor relative to the first killer, given N people 
    h = 2 ** int(math.log2(N))
    return 2 * (N-h) + 1
    
# This is the main implementation  
# timeit 100n, N=41: 14.7 ms ± 372 µs
# timeit 100n, N=41: 21.4 µs ± 220 ns (if show_process == false)

def circle_view(l, index):   # A little hack to refer a list as a looped datatype
    n = len(l)
    return ((n+index) % n)

def cod(N, show_process = False):     # show_process: show all the killings or just the survivor
    circle_of_death = [i+1 for i in range(N)]
    i = 0   # first killer (starting with 0, ie the first)
    n = len(circle_of_death)

    while (n > 1) :
        i = circle_view(circle_of_death, i+1)
        if (show_process):
            print(circle_of_death[i-1],"kills",circle_of_death[i])    # works even when i==0
        circle_of_death.pop(i)   # I use pop rather than del because it can be used directly in the print method
        n = len(circle_of_death)    

    return circle_of_death[0]

#This is a faster implementation, without showing the prcoess, based on slicing
# timeit 100n, N=41: 3.97 µs ± 50.2 ns 

def slice_cod(N):
    circle_of_death = [i+1 for i in range(N)]
    i = 1   # first victim (starting with 1, ie the second)
    n = len(circle_of_death)

    while (n > 1) :
        del circle_of_death[i::2]
        if (n % 2 == i) : i = 0
        else :i=1
        n = len(circle_of_death)    
    return circle_of_death[0]
