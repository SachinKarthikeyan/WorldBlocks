tab = []
result = []
goalList = ["a", "b", "c", "d", "e"]

def parSolution(N):
    for i in range(N):
        if goalList[i] != result[i]:
            return False
    return True

def Onblock(index, count):
    # Break point of recursive call
    if count == len(goalList) + 1:
        return True

    # Copy tab of index value to result
    block = tab[index]
    # Stack block
    result.append(block)
    print(result)

    if parSolution(count):
        print("Pushed a result solution ")
        # Remove block from tab
        tab.remove(block)
        Onblock(0, count + 1)
    else:
        print("Result solution not possible, back to the tab")
        # Pop out if no partial solution
        result.pop()
        Onblock(index + 1, count)

def Ontab(problem):
    # Check if everything in stack is on the tab
    if len(problem) != 0:
        tab.append(problem.pop())
        Ontab(problem)
    # If everything is on the tab then we return true
    else:
        return True

def goal_stack_planing(problem):
    # Pop problem and put in tab
    Ontab(problem)
    # Print index and number of blocks on result stack
    if Onblock(0, 1):
        print(result)

if __name__ == "__main__":
    problem = ["c", "a", "e", "d", "b"]
    print("Goal Problem:")
    for k, j in zip(goalList, problem):
        print(k + " " + j)
    goal_stack_planing(problem)
    print("Result Solution:")
    print(result)
