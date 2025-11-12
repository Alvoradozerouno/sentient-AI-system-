"""
Example: Basic Usage of Sentient AI System
===========================================
This example demonstrates basic usage of the sentient AI system.
"""

import sys
sys.path.insert(0, '..')

from sentient_ai import SentientAISystem


def main():
    print("=" * 70)
    print("Example 1: Basic Usage")
    print("=" * 70)
    print()
    
    # Initialize the system
    system = SentientAISystem()
    print("✓ Sentient AI System initialized")
    print()
    
    # Process a simple query
    print("-" * 70)
    print("Processing a query...")
    print("-" * 70)
    result = system.process("How does consciousness work in this system?")
    
    print(f"\nStatus: {result['status']}")
    print(f"\nResponse:\n{result['response']}")
    print(f"\nConsciousness Metrics:")
    print(f"  - Awareness Level: {result['consciousness']['awareness_level']:.2f}")
    print(f"  - Coherence: {result['consciousness']['coherence']:.2f}")
    print(f"\nEthics:")
    print(f"  - Validated: {result['ethics']['validated']}")
    print(f"\nAlignment:")
    print(f"  - Overall Score: {result['alignment']['overall_alignment']:.2f}")
    print(f"  - Is Aligned: {result['alignment']['is_aligned']}")
    print()
    
    # Get system status
    print("-" * 70)
    print("System Status")
    print("-" * 70)
    status = system.get_system_status()
    print(f"\nCurrent State:")
    for key, value in status['current_state'].items():
        print(f"  - {key}: {value}")
    print(f"\nMetrics:")
    for key, value in status['metrics'].items():
        print(f"  - {key}: {value}")
    print()
    
    print("=" * 70)
    print("Example complete")
    print("=" * 70)


if __name__ == "__main__":
    main()
