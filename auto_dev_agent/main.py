from agents.planner import Planner
from agents.coder import Coder
from agents.tester import Tester
from agents.debugger import Debugger
from utils.parser import parse_plan

MAX_RETRY = 3

def main():
    task = "Write a Python function to compute Fibonacci numbers"

    planner = Planner()
    coder = Coder()
    tester = Tester()
    debugger = Debugger()

    plan_raw = planner.run(task)
    plan = parse_plan(plan_raw)

    print("PLAN:", plan)

    code = coder.run(task)
    print("\nINITIAL CODE:\n", code)

    for i in range(MAX_RETRY):
        result = tester.run(code)

        if result["success"]:
            print("\nSUCCESS OUTPUT:\n", result["output"])
            break

        print(f"\nERROR (Round {i+1}):\n", result["error"])
        code = debugger.run(code, result["error"])

    else:
        print("\nFAILED AFTER RETRIES")

    print("\nFINAL CODE:\n", code)

if __name__ == "__main__":
    main()
