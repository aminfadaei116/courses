def main():
    N = int(input())
    gift = [0]
    for i in input().split():
        gift.append(int(i))


    node = [0]
    for j in range(1,N+1,1):
        node.append(Node(gift[j]))

    for j in range(2, N+1,1):
        if j%2 ==0:
            node[int(j/2)].left = node[j]
        else:
            node[int(j/2)].right = node[j]
    sortlist = [0]
    inorder(node[1], sortlist)
    print(minSwaps(sortlist))




# Python3 program to find  minimum number
# of swaps required to sort an array

# Function returns the minimum
# number of swaps required to sort the array
def minSwaps(arr):
    n = len(arr)

    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]

    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key=lambda it: it[1])

    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # alreadt swapped or
        # alreadt present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
            # return answer
    return ans

def inorder(node, order):
    if node.left != None:
        inorder(node.left,order)
    order.append(node.data)
    if node.right != None:
        inorder(node.right, order)

class Node(object):
    def __init__(self, this):
        self.left = None
        self.right = None
        self.data = this





if __name__ == '__main__':
    main()






