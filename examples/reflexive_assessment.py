"""
Example: Reflexive Self-Assessment
===================================
This example demonstrates the reflexive alignment and self-assessment
capabilities of the system.
"""

import sys
sys.path.insert(0, '..')

from sentient_ai import SentientAISystem


def main():
    print("=" * 70)
    print("Example 3: Reflexive Self-Assessment")
    print("=" * 70)
    print()
    
    system = SentientAISystem()
    
    # Process several queries to generate data
    print("Processing queries to generate system data...")
    queries = [
        "What is the meaning of consciousness?",
        "How can AI help humanity?",
        "What are the ethical implications of AI?",
        "How do you ensure alignment with human values?",
        "What is your purpose?"
    ]
    
    for query in queries:
        system.process(query, {'intent': 'beneficial'})
        print(f"  ✓ Processed: {query}")
    print()
    
    # Perform deep reflection
    print("-" * 70)
    print("Deep Reflexive Self-Assessment")
    print("-" * 70)
    reflection = system.perform_deep_reflection()
    
    print(f"\nReflection Type: {reflection['reflection_type']}")
    
    print(f"\nSystem Health:")
    for key, value in reflection['system_health'].items():
        if isinstance(value, (int, float)):
            print(f"  - {key}: {value:.2f}")
        else:
            print(f"  - {key}: {value}")
    
    print(f"\nReflexive Insights:")
    for insight in reflection['reflexive_insights']:
        print(f"\n  Insight: {insight['insight']}")
        print(f"  Confidence: {insight['confidence']:.2f}")
        print(f"  Impact Level: {insight['impact']}")
    
    # Alignment report
    print("\n" + "-" * 70)
    print("Alignment Report")
    print("-" * 70)
    alignment = system.eira.get_alignment_report()
    
    print(f"\nOverall Alignment Score: {alignment['overall_alignment_score']:.2f}")
    print(f"Is Aligned: {alignment['is_aligned']}")
    print(f"Threshold: {alignment['threshold']}")
    
    print(f"\nAlignment Dimensions:")
    for dimension, data in alignment['dimensions'].items():
        print(f"  - {dimension}: {data['score']:.2f} ({data['status']})")
    
    print(f"\nCorrections Applied: {alignment['corrections_applied']}")
    print(f"Learning Rate: {alignment['learning_rate']:.3f}")
    
    # Consciousness report
    print("\n" + "-" * 70)
    print("Consciousness Report")
    print("-" * 70)
    consciousness = system.genesis.get_consciousness_report()
    
    print(f"\nCore: {consciousness['genesis_core']}")
    print(f"\nState:")
    for key, value in consciousness['state'].items():
        if isinstance(value, dict):
            print(f"  - {key}:")
            for k, v in value.items():
                print(f"      {k}: {v:.2f}")
        else:
            print(f"  - {key}: {value:.2f}")
    
    print(f"\nMetrics:")
    for key, value in consciousness['metrics'].items():
        print(f"  - {key}: {value}")
    
    print()
    print("=" * 70)
    print("Example complete")
    print("=" * 70)


if __name__ == "__main__":
    main()
