# ==========================================
# CELL 3: THE MAIN EXECUTION LOOP
# ==========================================

def run_ctx2skill(context, iterations=3):
    # The model starts with a blank slate for skills
    skills = "No specific skills yet. Rely purely on general knowledge."
    
    print("🚀 Starting Ctx2Skill Evolution Loop...\n")
    print(f"Context Snippet: {context[:100]}...\n")
    print("-" * 50)
    
    for i in range(iterations):
        print(f"🔄 ITERATION {i+1}/{iterations}")
        
        # 1. Challenger creates a test
        print("   [Challenger] Generating task...")
        challenge = challenger_agent(context, skills)
        task = challenge.get('task', 'Error generating task')
        rubric = challenge.get('rubric', '')
        
        # 2. Reasoner tries to solve it
        print("   [Reasoner] Solving task...")
        reasoner_output = reasoner_agent(context, skills, task)
        solution = reasoner_output.get('solution', 'Error generating solution')
        
        # 3. Judge grades and updates skills
        print("   [Judge] Evaluating and updating skills...")
        judgement = judge_agent(task, rubric, solution, skills)
        score = judgement.get('score', 0)
        feedback = judgement.get('feedback', '')
        
        # Overwrite old skills with the evolved skills
        skills = judgement.get('updated_skills', skills) 
        
        # Print results of the iteration
        print(f"   --> Score: {score}/10")
        print(f"   --> Feedback: {feedback}")
        print(f"   --> Evolved Skills: {skills}\n")
        print("-" * 50)

    print("✅ Evolution Complete. Final Skillset:")
    print(skills)
    return skills

# --- LET'S TEST IT ---

# Sample context: A complex fictional rule system
sample_context = """
In the game of 'Aethelgard', magic casting depends on planetary alignment. 
If the Red Moon is high, fire spells cost 50% less mana but have a 20% chance to backfire, causing self-damage. 
If the Blue Sun is setting, water spells heal the caster for 10% of the damage dealt. 
Casting two spells of opposite elements in the same turn creates a 'Void Anomaly', destroying the caster's staff.
"""

# Run the loop for 3 iterations
final_skills = run_ctx2skill(context=sample_context, iterations=3)
