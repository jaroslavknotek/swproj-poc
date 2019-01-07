import matplotlib.pyplot as plt

def visualize_pairs(pairs):
    x = [x for x,_ in pairs]
    y = [y for _,y in pairs]
    print(x)
    print(y)
    plt.plot(x, y, 'ro')
    plt.axis([0, max(x) +1, 0, max(y)+5])
    plt.show()