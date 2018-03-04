# This is an implementation of the mathematical algorithm

def highest_power(N):   # Calculates the highest power of two that is not large than N
    i=1
    while (1):
        if 2**i > N : return 2**(i-1)
        else: i += 1
    
def surviver(N):           # Returns the position of the surviver relative to the first killer, given N people 
    h = highest_power(N)
    return 2 * (N-h) + 1
    

# This is the main implementation  
# timeit 100n, N=41: 14.7 ms ± 372 µs

def circle_view(l, index):   # A little hack to refer a list as a looped datatype
    n = len(l)
    return ((n+index) % n)

N = int(input("How many people are standing in the circle? "))
circle_of_death = [i+1 for i in range(N)]
i = 0   # first killer (starting with 0, ie the first)
n = len(circle_of_death)
show_process = False  # Show all the killings or just the surviver

while (n > 1) :
    i = circle_view(circle_of_death, i+1)
    if (show_process):
        print(circle_of_death[i-1],"kills",circle_of_death[i])    # works even when i==0
    circle_of_death.pop(i)   # I use pop rather than del because it can be used directly in the print method
    n = len(circle_of_death)    

print("Number",circle_of_death[0],"survives")
circle_of_death[0] == surviver(N)
