from agent.core import run_agent
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        goal = " ".join(sys.argv[1:])
    else:
        goal = input("🎯 Goal: ")
    
    if not goal:
        print("No goal provided. Exiting.")
    else:
        run_agent(goal)
