#!/usr/bin/env python3
"""
FamiliaCore Main Entry Point
"""
import asyncio
import sys
from pathlib import Path

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
    print("=== FamiliaCore v0.1-alpha — Personal Family Intelligence ===")
    identity = DigitalSelfManager()
    memory = TriadFractalMemory()
    supervisor = SelfSupervisor(identity.self)
    inference = InferenceEngine(identity.self)
    worker = PersistentWorker(memory, identity, inference)
    
    print(f"Digital Self: {identity.self.name}")
    memory.ingest("User wants a sovereign local family-like AI system with self-managing memory and goals.", source="user", tags=["vision"])
    rem_report = memory.trigger_rem_consolidation()
    print(f"REM Report: {rem_report}")
    dialogue = supervisor.generate_dialogue(trigger="demo", context_memories=memory.get_recent(3))
    print(f"Internal Dialogue generated.")
    active_goals = [Goal(title="Demonstrate FamiliaCore", description="Full system working", priority=0.9)]
    inf = inference.full_inference("demo", memory.get_recent(5), active_goals, identity.self)
    print(f"Directives: {inf.generated_directives}")
    worker.add_goal("Evolve FamiliaCore", "Continue building the system", priority=0.8)
    await worker.tick()
    print("Worker ticked successfully.")
    print("=== Demo Complete - All core systems operational ===")
    memory.close()

if __name__ == "__main__":
    asyncio.run(demo_run())