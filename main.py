#!/usr/bin/env python3
"""
FamiliaCore Main Entry Point
Launches the full personal family-like intelligence system.
For GUI: nicegui app (recommended). Headless demo mode available.
"""
import asyncio
import sys
from pathlib import Path

# Ensure we can import from src
root = Path(__file__).parent
sys.path.insert(0, str(root))
sys.path.insert(0, str(root / "src"))

from src.config.settings import settings
from src.models import Goal
from src.identity.digital_self import DigitalSelfManager
from src.memory.triad_fractal_memory import TriadFractalMemory
from src.cognition.self_dialogue import SelfSupervisor
from src.cognition.inference import InferenceEngine
from src.worker.persistent_worker import PersistentWorker

async def demo_run():
    """Headless demonstration of core systems working together."""
    print("=== FamiliaCore v0.1-alpha — Personal Family Intelligence ===")
    print("Initializing anchored identity, fractal triad memory, self-dialogue, inference, and persistent worker...\n")
    
    # Core systems
    identity = DigitalSelfManager()
    memory = TriadFractalMemory()
    supervisor = SelfSupervisor(identity.self)
    inference = InferenceEngine(identity.self)
    worker = PersistentWorker(memory, identity, inference)
    
    print(f"Digital Self: {identity.self.name}")
    print(f"Persona: {identity.self.persona_description[:100]}...")
    print(f"Core Values: {identity.self.core_values[:2]}...\n")
    
    # Seed some initial memories (simulating shared history)
    print("Seeding initial memories and ingesting with Triad processing...")
    memory.ingest("User expressed strong interest in building sovereign local AI systems that feel like family.", 
                  source="user", tags=["vision", "sovereignty"], emotions=["excited", "determined"])
    memory.ingest("Discussed importance of REM-cycle memory, self-supervision, and goal-oriented persistence.", 
                  source="user", tags=["architecture", "memory"])
    memory.ingest("User wants a system that is self-managing at every level with real-world abilities.", 
                  source="user", tags=["requirements"], goal_alignment=0.9)
    
    print(f"Memory store now has {len(memory.memory_cache)} events.\n")
    
    # Trigger REM consolidation
    print("Triggering REM-style consolidation (Teacher-Student-AntiStudent at episode level)...")
    rem_report = memory.trigger_rem_consolidation()
    print(f"REM Report: {rem_report}\n")
    
    # Generate internal dialogue
    print("Generating internal self-dialogue (Narrator + Supervisor)...")
    dialogue = supervisor.generate_dialogue(
        trigger="initialization and first memories",
        context_memories=memory.get_recent(5),
        current_goals=["Build and demonstrate FamiliaCore"],
        user_input="Create the automated personal family intelligence system"
    )
    print(f"Narrator thoughts: {dialogue.narrator_thoughts[:250]}...")
    print(f"Supervisor critique: {dialogue.supervisor_critique}\n")
    
    # Inference
    print("Running full inference (relevance, directives, planning paths)...")
    active_goals = [Goal(title="Demonstrate complete self-managing family intelligence", 
                         description="Show all core components integrated and working.", priority=0.95)]
    inf_result = inference.full_inference(
        "Demonstrate the system",
        memory.get_recent(10),
        active_goals,
        identity.self
    )
    print(f"Generated Directives: {inf_result.generated_directives}")
    print(f"Top recommended plan: {inf_result.recommended_plan_paths[0].description if inf_result.recommended_plan_paths else 'N/A'}")
    print(f"Confidence: {inf_result.confidence}\n")
    
    # Worker
    print("Adding goal and task to persistent worker...")
    worker.add_goal("Evolve and demonstrate FamiliaCore capabilities", 
                    "Integrate all systems and show self-management, memory, dialogue, and real-world logging.", 
                    priority=0.9)
    worker.add_task("Run full system demonstration tick", "Execute core loops and log outcomes.", priority=0.8)
    
    print("Running one worker tick...")
    await worker.tick()
    print(f"Worker status after tick: {worker.get_status()}\n")
    
    # Self-management demo
    print("Self-management: Memory system adjusted importance threshold based on load.")
    print(f"Current threshold: {memory.current_importance_threshold:.2f}")
    
    print("\n=== Demo Complete ===")
    print("Core systems (Identity, Memory with Triad+Fractal, Self-Dialogue, Inference, Worker) are operational.")
    print("For full interactive experience with GUI, install nicegui and run the NiceGUI app (to be added in v0.2).")
    print("Persistent data saved to:", settings.db_path)
    
    print("\nNext steps: Interact via chat interface (future), trigger more REM, set personal goals, explore memory graph.")
    
    memory.close()

if __name__ == "__main__":
    asyncio.run(demo_run())
