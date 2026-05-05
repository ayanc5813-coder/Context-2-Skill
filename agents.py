# ==========================================
# CELL 2: THE CTX2SKILL AGENTS
# ==========================================

def challenger_agent(context, current_skills):
    """Generates a task and a rubric based on the context and current skills."""
    system_prompt = """You are the Challenger Agent. Your goal is to test the reasoning capabilities of another AI. 
    Output ONLY a JSON object with two keys: "task" (a complex question based on the context) and "rubric" (criteria to grade the answer)."""
    
    user_prompt = f"""
    CONTEXT: {context}
    CURRENT SKILLS: {current_skills}
    
    Create a challenging task that requires applying the context, and a strict grading rubric.
    """
    return call_llm(system_prompt, user_prompt)


def reasoner_agent(context, current_skills, task):
    """Attempts to solve the task using the context and its evolved skills."""
    system_prompt = """You are the Reasoner Agent. Use the provided context and your current skill set to solve the task.
    Output ONLY a JSON object with one key: "solution" (your detailed answer)."""
    
    user_prompt = f"""
    CONTEXT: {context}
    CURRENT SKILLS: {current_skills}
    TASK: {task}
    
    Solve the task. Rely heavily on your 'CURRENT SKILLS' to guide your reasoning.
    """
    return call_llm(system_prompt, user_prompt)


def judge_agent(task, rubric, solution, current_skills):
    """Evaluates the solution and updates the skills to improve future performance."""
    system_prompt = """You are the Judge Agent. Evaluate the solution against the rubric. 
    More importantly, refine the 'skills' (rules, procedures, heuristics) the Reasoner should use next time to do better.
    Output ONLY a JSON object with three keys: "score" (1-10), "feedback" (brief explanation), and "updated_skills" (a refined list/description of skills)."""
    
    user_prompt = f"""
    TASK: {task}
    RUBRIC: {rubric}
    SOLUTION: {solution}
    CURRENT SKILLS: {current_skills}
    
    Grade the solution. Then, rewrite and improve the 'CURRENT SKILLS' based on what the Reasoner missed or did well.
    """
    return call_llm(system_prompt, user_prompt)

print("✅ Agents Initialized!")
