# Goal Stack Planning Algorithm

This Python code implements the Goal Stack Planning algorithm. Goal Stack Planning is a method used in Artificial Intelligence and Robotics for planning and problem-solving. It involves breaking down a complex problem into subgoals and solving them step by step.

## Description

The code consists of the following components:

1. `tab`: A list to represent the table where blocks can be placed.

2. `result`: A list to represent the current result stack.

3. `goalList`: A list of goals to achieve.

4. `parSolution(N)`: A function to check if a partial solution is reached.

5. `Onblock(index, count)`: A recursive function to stack blocks on the result stack and check for partial solutions.

6. `Ontab(problem)`: A function to move blocks from the problem to the tab.

7. `goal_stack_planing(problem)`: The main function that performs goal stack planning.

## How It Works

1. The code starts with a `problem`, which represents the initial state of blocks on the table.

2. It checks the `goalList`, which represents the desired final state.

3. The `goal_stack_planing(problem)` function is called to plan and achieve the goals.

4. The code uses a goal stack to achieve each subgoal by stacking and unstacking blocks.

## Usage

To use this code, follow these steps:

1. Define the `problem` variable with the initial state of blocks.

2. Run the code, and it will print the goal problem, perform goal stack planning, and print the result solution.

## Example

```python
if __name__ == "__main__":
    problem = ["c", "a", "e", "d", "b"]
    print("Goal Problem:")
    for k, j in zip(goalList, problem):
        print(k + " " + j)
    goal_stack_planing(problem)
    print("Result Solution:")
    print(result)
