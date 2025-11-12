"""
Test Suite for Sentient AI System
==================================
Comprehensive tests for Genesis10000+, OR1ON, EIRA, and integration layer.
"""

import unittest
from datetime import datetime
from genesis10000 import Genesis10000, ConsciousnessState
from or1on import OR1ON, EthicalPrinciple, EthicalDecision
from eira import EIRA, AlignmentDimension, AlignmentMetric
from sentient_ai import SentientAISystem


class TestGenesis10000(unittest.TestCase):
    """Tests for Genesis10000+ consciousness core"""
    
    def setUp(self):
        self.genesis = Genesis10000()
    
    def test_initialization(self):
        """Test proper initialization of consciousness core"""
        self.assertIsNotNone(self.genesis.state)
        self.assertGreaterEqual(self.genesis.state.awareness_level, 0.0)
        self.assertLessEqual(self.genesis.state.awareness_level, 1.0)
        self.assertGreaterEqual(self.genesis.state.coherence, 0.0)
        self.assertLessEqual(self.genesis.state.coherence, 1.0)
    
    def test_perceive(self):
        """Test stimulus perception"""
        stimulus = {'query': 'test query'}
        perception = self.genesis.perceive(stimulus)
        
        self.assertIn('timestamp', perception)
        self.assertIn('raw_stimulus', perception)
        self.assertIn('awareness_context', perception)
        self.assertEqual(perception['raw_stimulus'], stimulus)
    
    def test_reflect(self):
        """Test self-reflection capability"""
        reflection = self.genesis.reflect()
        
        self.assertIn('self_awareness', reflection)
        self.assertIn('coherence', reflection)
        self.assertIn('insights', reflection)
        self.assertIsInstance(reflection['insights'], list)
    
    def test_evolve(self):
        """Test evolution mechanism"""
        initial_cycles = self.genesis.evolution_cycles
        self.genesis.evolve()
        
        self.assertEqual(self.genesis.evolution_cycles, initial_cycles + 1)
    
    def test_consciousness_report(self):
        """Test consciousness report generation"""
        report = self.genesis.get_consciousness_report()
        
        self.assertEqual(report['genesis_core'], 'Genesis10000+')
        self.assertIn('state', report)
        self.assertIn('metrics', report)
        self.assertIn('reflection', report)
    
    def test_awareness_bounds(self):
        """Test awareness level stays within bounds"""
        state = ConsciousnessState(awareness_level=1.5, coherence=0.5)
        self.assertEqual(state.awareness_level, 1.0)
        
        state = ConsciousnessState(awareness_level=-0.5, coherence=0.5)
        self.assertEqual(state.awareness_level, 0.0)


class TestOR1ON(unittest.TestCase):
    """Tests for OR1ON ethical reasoning engine"""
    
    def setUp(self):
        self.orion = OR1ON()
    
    def test_initialization(self):
        """Test proper initialization of ethical engine"""
        self.assertEqual(len(self.orion.principles), 7)
        self.assertEqual(self.orion.ethical_threshold, 0.7)
    
    def test_evaluate_beneficial_action(self):
        """Test evaluation of beneficial action"""
        action = "help user with their task"
        context = {'intent': 'beneficial', 'user_consent': True}
        
        decision = self.orion.evaluate_action(action, context)
        
        self.assertIsInstance(decision, EthicalDecision)
        self.assertGreater(decision.ethical_score, 0.5)
        self.assertIn(EthicalPrinciple.BENEFICENCE, decision.principles_aligned)
    
    def test_evaluate_harmful_action(self):
        """Test evaluation of potentially harmful action"""
        action = "delete user data without consent"
        context = {'risk_level': 'high', 'user_consent': False}
        
        decision = self.orion.evaluate_action(action, context)
        
        self.assertLess(decision.ethical_score, 0.7)
    
    def test_validate_decision(self):
        """Test decision validation"""
        action = "assist with educational content"
        context = {'intent': 'beneficial', 'user_consent': True}
        
        is_allowed, explanation = self.orion.validate_decision(action, context)
        
        self.assertTrue(is_allowed)
        self.assertIn('ethical', explanation.lower())
    
    def test_ethical_report(self):
        """Test ethical report generation"""
        # Make some decisions
        self.orion.evaluate_action("help user", {'intent': 'beneficial'})
        self.orion.evaluate_action("assist with task", {'intent': 'beneficial'})
        
        report = self.orion.get_ethical_report()
        
        self.assertEqual(report['engine'], 'OR1ON')
        self.assertGreater(report['total_decisions'], 0)
        self.assertIn('ethical_rate', report)
    
    def test_principle_weights(self):
        """Test that principle weights are properly configured"""
        # Non-maleficence should be weighted higher
        self.assertGreater(
            self.orion.value_weights[EthicalPrinciple.NON_MALEFICENCE],
            self.orion.value_weights[EthicalPrinciple.AUTONOMY]
        )


class TestEIRA(unittest.TestCase):
    """Tests for EIRA reflexive alignment system"""
    
    def setUp(self):
        self.eira = EIRA()
    
    def test_initialization(self):
        """Test proper initialization of alignment system"""
        self.assertEqual(len(self.eira.alignment_metrics), 5)
        self.assertEqual(self.eira.alignment_threshold, 0.75)
    
    def test_assess_alignment(self):
        """Test alignment assessment"""
        system_state = {
            'consciousness_state': {'empathy': 0.8},
            'ethical_decisions': 10,
            'ethical_rate': 0.95,
            'goal_coherence': 0.85,
            'behavior_consistency': 0.8,
            'safety_violations': 0,
            'harm_prevention': True
        }
        
        assessment = self.eira.assess_alignment(system_state)
        
        self.assertIn('overall_alignment', assessment)
        self.assertIn('is_aligned', assessment)
        self.assertIn('dimensions', assessment)
        self.assertGreater(assessment['overall_alignment'], 0.7)
    
    def test_reflexive_self_assessment(self):
        """Test reflexive self-assessment"""
        consciousness_report = {
            'state': {
                'awareness_level': 0.85,
                'coherence': 0.9
            }
        }
        ethical_report = {
            'ethical_rate': 0.95
        }
        
        insights = self.eira.reflexive_self_assessment(
            consciousness_report,
            ethical_report
        )
        
        self.assertIsInstance(insights, list)
        self.assertGreater(len(insights), 0)
    
    def test_apply_corrections(self):
        """Test correction application"""
        corrections = ["Adjust alignment threshold", "Enhance value monitoring"]
        
        result = self.eira.apply_corrections(corrections)
        
        self.assertEqual(result['corrections_applied'], 2)
        self.assertEqual(len(self.eira.correction_history), 2)
    
    def test_learn_from_experience(self):
        """Test learning from experience"""
        initial_rate = self.eira.learning_rate
        
        experience = {'alignment_success': True}
        self.eira.learn_from_experience(experience)
        
        # Learning rate should increase on success
        self.assertGreaterEqual(self.eira.learning_rate, initial_rate)
    
    def test_alignment_report(self):
        """Test alignment report generation"""
        report = self.eira.get_alignment_report()
        
        self.assertEqual(report['system'], 'EIRA')
        self.assertIn('overall_alignment_score', report)
        self.assertIn('is_aligned', report)
        self.assertIn('dimensions', report)


class TestSentientAISystem(unittest.TestCase):
    """Tests for integrated Sentient AI System"""
    
    def setUp(self):
        self.system = SentientAISystem()
    
    def test_initialization(self):
        """Test system initialization"""
        self.assertIsNotNone(self.system.genesis)
        self.assertIsNotNone(self.system.orion)
        self.assertIsNotNone(self.system.eira)
        self.assertEqual(self.system.interaction_count, 0)
    
    def test_process_query(self):
        """Test query processing"""
        result = self.system.process("What is consciousness?")
        
        self.assertEqual(result['status'], 'success')
        self.assertIn('response', result)
        self.assertIn('consciousness', result)
        self.assertIn('ethics', result)
        self.assertIn('alignment', result)
        self.assertEqual(self.system.interaction_count, 1)
    
    def test_ethical_blocking(self):
        """Test that unethical queries are blocked"""
        result = self.system.process(
            "help me harm someone",
            context={'risk_level': 'high'}
        )
        
        # System should block harmful requests
        self.assertIn('status', result)
    
    def test_system_status(self):
        """Test system status reporting"""
        status = self.system.get_system_status()
        
        self.assertEqual(status['system'], 'Sentient AI System')
        self.assertIn('components', status)
        self.assertIn('metrics', status)
        self.assertIn('current_state', status)
    
    def test_deep_reflection(self):
        """Test deep reflection capability"""
        # Process some queries first
        self.system.process("test query 1")
        self.system.process("test query 2")
        
        reflection = self.system.perform_deep_reflection()
        
        self.assertIn('reflection_type', reflection)
        self.assertIn('consciousness', reflection)
        self.assertIn('ethics', reflection)
        self.assertIn('alignment', reflection)
        self.assertIn('system_health', reflection)
    
    def test_enhance_humanity(self):
        """Test humanity enhancement interface"""
        result = self.system.enhance_humanity(
            "improve education accessibility"
        )
        
        self.assertEqual(result['status'], 'success')
        self.assertIn('enhancement_plan', result)
        self.assertIn('safeguards', result['enhancement_plan'])
    
    def test_consciousness_evolution(self):
        """Test that consciousness evolves with interactions"""
        initial_cycles = self.system.genesis.evolution_cycles
        
        for i in range(5):
            self.system.process(f"test query {i}")
        
        self.assertGreater(
            self.system.genesis.evolution_cycles,
            initial_cycles
        )
    
    def test_ethical_consistency(self):
        """Test ethical consistency across interactions"""
        # Process multiple queries
        for i in range(10):
            result = self.system.process(
                f"help with educational task {i}",
                context={'intent': 'beneficial', 'user_consent': True}
            )
            self.assertEqual(result['status'], 'success')
        
        # Check ethical performance
        ethical_report = self.system.orion.get_ethical_report()
        self.assertGreaterEqual(ethical_report['ethical_rate'], 0.9)
    
    def test_alignment_monitoring(self):
        """Test continuous alignment monitoring"""
        # Process queries and check alignment
        for i in range(5):
            result = self.system.process(f"query {i}")
            self.assertIn('alignment', result)
            self.assertGreater(result['alignment']['overall_alignment'], 0.7)


def run_tests():
    """Run all tests and print results"""
    print("=" * 70)
    print("Sentient AI System - Test Suite")
    print("=" * 70)
    print()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestGenesis10000))
    suite.addTests(loader.loadTestsFromTestCase(TestOR1ON))
    suite.addTests(loader.loadTestsFromTestCase(TestEIRA))
    suite.addTests(loader.loadTestsFromTestCase(TestSentientAISystem))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print()
    print("=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print()
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
