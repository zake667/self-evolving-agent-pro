from agent.brain import ask_ai
from agent.memory import load_memory, save_memory
from agent.evaluator import evaluate
from tools.shell import run
from tools.fs import read_file, write_file
from tools.logger import log_info, log_error, log_command

MAX_ITER = 15

def run_agent(goal):
    memory = load_memory()
    log_info(f"Starting agent with goal: {goal}")
    
    # Historial de errores para evitar bucles
    error_count = {}

    for i in range(MAX_ITER):
        log_info(f"Iteration {i+1}")

        # Contexto enriquecido para la IA
        history = memory.get('history', [])[-5:]
        prompt = f"""
You are an advanced autonomous coding agent.
Goal: {goal}
Current History: {history}

Task: Provide the next steps to achieve the goal.
Format Rules:
- Use 'run: <cmd>' for terminal commands.
- Use 'read: <path>' to see file content.
- Use 'write: <path> | <content>' to save files.
- Use 'thought: <text>' for your reasoning.
- If finished, write 'GOAL_ACHIEVED'.

Be surgical and efficient.
"""
        plan = ask_ai(prompt)
        log_info("AI processing plan...")

        steps = plan.split("\n")
        for step in steps:
            step = step.strip()
            if not step: continue

            log_info(f"Executing: {step[:50]}...")
            
            result = {"exit_code": 0, "output": ""}
            
            if step.lower().startswith("run:"):
                result = run(step[4:].strip())
                log_command(step[4:].strip(), result)
            elif step.lower().startswith("read:"):
                content = read_file(step[5:].strip())
                result = {"exit_code": 0, "output": content[:500]}
            elif step.lower().startswith("write:"):
                parts = step[6:].split("|", 1)
                if len(parts) == 2:
                    res = write_file(parts[0].strip(), parts[1].strip())
                    result = {"exit_code": 0, "output": res}
            elif step.lower().startswith("thought:"):
                continue # Solo es razonamiento

            # Evaluar progreso
            status = evaluate(result)
            if status == "error":
                log_error(f"Step failed: {step}")
                # Evitar bucles infinitos en el mismo error
                error_count[step] = error_count.get(step, 0) + 1
                if error_count[step] > 3:
                    log_error("Critical: Loop detected on same error. Stopping.")
                    return

        # Actualizar memoria
        if "history" not in memory: memory["history"] = []
        memory["history"].append(plan)
        save_memory(memory)

        if "GOAL_ACHIEVED" in plan:
            log_info("Agent reports: Goal achieved successfully.")
            break
