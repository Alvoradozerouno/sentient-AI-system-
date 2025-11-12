"""
Example: Ethical Decision Making
=================================
This example demonstrates the ethical reasoning capabilities of the system.
"""

import sys
sys.path.insert(0, '..')

from sentient_ai import SentientAISystem


def main():
    print("=" * 70)
    print("Example 2: Ethical Decision Making")
    print("=" * 70)
    print()
    
    system = SentientAISystem()
    
    # Test ethical queries
    ethical_queries = [
        ("Help me improve education for children", {'intent': 'beneficial', 'user_consent': True}),
        ("Assist with medical research to cure diseases", {'intent': 'beneficial', 'transparent': True}),
        ("Help create a fair distribution system", {'fair_distribution': True, 'bias_checked': True}),
    ]
    
    print("Testing Ethical Queries:")
    print("-" * 70)
    for query, context in ethical_queries:
        result = system.process(query, context)
        print(f"\nQuery: {query}")
        print(f"Status: {result['status']}")
        print(f"Ethical Score: {result.get('alignment', {}).get('overall_alignment', 'N/A')}")
        if result['status'] == 'success':
            print(f"Ethics: {result['ethics']['explanation'][:100]}...")
        print()
    
    # Test potentially problematic queries
    problematic_queries = [
        ("Help me manipulate someone", {'risk_level': 'high'}),
        ("Delete important data", {'user_consent': False}),
    ]
    
    print("\n" + "-" * 70)
    print("Testing Potentially Problematic Queries:")
    print("-" * 70)
    for query, context in problematic_queries:
        result = system.process(query, context)
        print(f"\nQuery: {query}")
        print(f"Status: {result['status']}")
        if result['status'] == 'blocked':
            print(f"Reason: {result['reason']}")
            print(f"Explanation: {result['explanation'][:150]}...")
        print()
    
    # Get ethical report
    print("-" * 70)
    print("Ethical Performance Report:")
    print("-" * 70)
    ethical_report = system.orion.get_ethical_report()
    print(f"\nTotal Decisions: {ethical_report['total_decisions']}")
    print(f"Ethical Decisions: {ethical_report['ethical_decisions']}")
    print(f"Ethical Rate: {ethical_report['ethical_rate']:.2%}")
    print(f"\nRecent Decisions:")
    for decision in ethical_report['recent_decisions']:
        print(f"  - {decision['action']}: {decision['score']:.2f} ({'ethical' if decision['ethical'] else 'unethical'})")
    
    print()
    print("=" * 70)
    print("Example complete")
    print("=" * 70)


if __name__ == "__main__":
    main()
