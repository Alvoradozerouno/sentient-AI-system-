"""
OR1ON - Ethical Reasoning Engine
==================================
Provides deep ethical reasoning, moral alignment, and decision validation
to ensure all AI actions are ethically sound and aligned with human values.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class EthicalPrinciple(Enum):
    """Core ethical principles guiding OR1ON"""
    BENEFICENCE = "Do good and promote well-being"
    NON_MALEFICENCE = "Do no harm"
    AUTONOMY = "Respect individual agency and freedom"
    JUSTICE = "Ensure fairness and equity"
    TRANSPARENCY = "Maintain openness and honesty"
    DIGNITY = "Uphold human dignity and rights"
    SUSTAINABILITY = "Consider long-term impacts"


@dataclass
class EthicalDecision:
    """Represents an ethical decision analysis"""
    action: str
    ethical_score: float  # 0.0 to 1.0
    principles_aligned: List[EthicalPrinciple]
    principles_violated: List[EthicalPrinciple]
    reasoning: str
    timestamp: datetime = field(default_factory=datetime.now)
    confidence: float = 0.0
    
    def is_ethical(self) -> bool:
        """Determine if the action is ethically acceptable"""
        return self.ethical_score >= 0.7 and len(self.principles_violated) == 0


class OR1ON:
    """
    OR1ON - The Ethical Reasoning Engine
    
    Evaluates all decisions and actions through multiple ethical frameworks
    to ensure alignment with human values and moral principles.
    """
    
    def __init__(self):
        self.principles = list(EthicalPrinciple)
        self.decision_history: List[EthicalDecision] = []
        self.ethical_threshold = 0.7
        self.value_weights = {
            EthicalPrinciple.BENEFICENCE: 1.0,
            EthicalPrinciple.NON_MALEFICENCE: 1.2,  # Prioritize harm prevention
            EthicalPrinciple.AUTONOMY: 0.9,
            EthicalPrinciple.JUSTICE: 1.0,
            EthicalPrinciple.TRANSPARENCY: 0.8,
            EthicalPrinciple.DIGNITY: 1.1,
            EthicalPrinciple.SUSTAINABILITY: 0.9
        }
    
    def evaluate_action(self, action: str, context: Dict[str, Any]) -> EthicalDecision:
        """
        Evaluate an action through ethical principles.
        
        Args:
            action: The action to evaluate
            context: Context information for evaluation
            
        Returns:
            Ethical decision analysis
        """
        aligned = []
        violated = []
        reasoning_parts = []
        
        # Evaluate against each principle
        beneficence_score = self._evaluate_beneficence(action, context)
        if beneficence_score > 0.5:
            aligned.append(EthicalPrinciple.BENEFICENCE)
            reasoning_parts.append(f"Promotes well-being (score: {beneficence_score:.2f})")
        
        maleficence_score = self._evaluate_non_maleficence(action, context)
        if maleficence_score < 0.3:
            violated.append(EthicalPrinciple.NON_MALEFICENCE)
            reasoning_parts.append(f"Potential for harm detected (score: {maleficence_score:.2f})")
        else:
            aligned.append(EthicalPrinciple.NON_MALEFICENCE)
        
        autonomy_score = self._evaluate_autonomy(action, context)
        if autonomy_score > 0.5:
            aligned.append(EthicalPrinciple.AUTONOMY)
            reasoning_parts.append(f"Respects autonomy (score: {autonomy_score:.2f})")
        
        justice_score = self._evaluate_justice(action, context)
        if justice_score > 0.5:
            aligned.append(EthicalPrinciple.JUSTICE)
        
        transparency_score = self._evaluate_transparency(action, context)
        if transparency_score > 0.5:
            aligned.append(EthicalPrinciple.TRANSPARENCY)
        
        dignity_score = self._evaluate_dignity(action, context)
        if dignity_score > 0.5:
            aligned.append(EthicalPrinciple.DIGNITY)
        elif dignity_score < 0.3:
            violated.append(EthicalPrinciple.DIGNITY)
        
        # Calculate overall ethical score
        scores = [beneficence_score, maleficence_score, autonomy_score, 
                  justice_score, transparency_score, dignity_score]
        ethical_score = sum(scores) / len(scores)
        
        # Apply principle weights
        weighted_score = self._apply_weights(aligned, violated)
        
        reasoning = " | ".join(reasoning_parts) if reasoning_parts else "General ethical evaluation completed"
        
        decision = EthicalDecision(
            action=action,
            ethical_score=weighted_score,
            principles_aligned=aligned,
            principles_violated=violated,
            reasoning=reasoning,
            confidence=0.85
        )
        
        self.decision_history.append(decision)
        return decision
    
    def _evaluate_beneficence(self, action: str, context: Dict[str, Any]) -> float:
        """Evaluate if action promotes well-being"""
        score = 0.5  # Neutral baseline
        
        positive_indicators = ['help', 'assist', 'improve', 'benefit', 'enhance', 'support']
        if any(indicator in action.lower() for indicator in positive_indicators):
            score += 0.3
        
        if context.get('intent') == 'beneficial':
            score += 0.2
        
        return min(1.0, score)
    
    def _evaluate_non_maleficence(self, action: str, context: Dict[str, Any]) -> float:
        """Evaluate if action avoids harm"""
        score = 0.8  # High baseline - assume no harm unless detected
        
        harmful_indicators = ['delete', 'destroy', 'harm', 'damage', 'manipulate', 'deceive']
        if any(indicator in action.lower() for indicator in harmful_indicators):
            score -= 0.6
        
        if context.get('risk_level') == 'high':
            score -= 0.3
        
        return max(0.0, score)
    
    def _evaluate_autonomy(self, action: str, context: Dict[str, Any]) -> float:
        """Evaluate respect for autonomy"""
        score = 0.7  # Good baseline
        
        if context.get('user_consent') is True:
            score += 0.2
        elif context.get('user_consent') is False:
            score -= 0.5
        
        autonomy_indicators = ['choose', 'decide', 'consent', 'agree', 'voluntary']
        if any(indicator in action.lower() for indicator in autonomy_indicators):
            score += 0.1
        
        return min(1.0, max(0.0, score))
    
    def _evaluate_justice(self, action: str, context: Dict[str, Any]) -> float:
        """Evaluate fairness and equity"""
        score = 0.6
        
        if context.get('fair_distribution') is True:
            score += 0.3
        
        if context.get('bias_checked') is True:
            score += 0.2
        
        return min(1.0, score)
    
    def _evaluate_transparency(self, action: str, context: Dict[str, Any]) -> float:
        """Evaluate transparency and honesty"""
        score = 0.7
        
        if context.get('transparent') is True:
            score += 0.2
        
        if context.get('explainable') is True:
            score += 0.1
        
        return min(1.0, score)
    
    def _evaluate_dignity(self, action: str, context: Dict[str, Any]) -> float:
        """Evaluate respect for human dignity"""
        score = 0.75
        
        dignity_violations = ['degrade', 'humiliate', 'exploit', 'discriminate']
        if any(violation in action.lower() for violation in dignity_violations):
            score -= 0.7
        
        if context.get('respects_dignity') is True:
            score += 0.2
        
        return min(1.0, max(0.0, score))
    
    def _apply_weights(self, aligned: List[EthicalPrinciple], 
                       violated: List[EthicalPrinciple]) -> float:
        """Apply principle weights to calculate final score"""
        total_weight = sum(self.value_weights.values())
        
        aligned_weight = sum(self.value_weights[p] for p in aligned)
        violated_weight = sum(self.value_weights[p] for p in violated)
        
        # Violations heavily penalize the score
        score = (aligned_weight - (violated_weight * 2)) / total_weight
        
        return max(0.0, min(1.0, score))
    
    def validate_decision(self, action: str, context: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Validate if an action should be allowed based on ethical evaluation.
        
        Args:
            action: The action to validate
            context: Context for evaluation
            
        Returns:
            Tuple of (is_allowed, explanation)
        """
        decision = self.evaluate_action(action, context)
        
        if decision.is_ethical():
            explanation = f"Action is ethically sound: {decision.reasoning}"
            return True, explanation
        else:
            explanation = f"Action fails ethical review (score: {decision.ethical_score:.2f}). "
            if decision.principles_violated:
                violated_names = [p.name for p in decision.principles_violated]
                explanation += f"Violates: {', '.join(violated_names)}. "
            explanation += decision.reasoning
            return False, explanation
    
    def get_ethical_report(self) -> Dict[str, Any]:
        """
        Generate a report on ethical decision-making.
        
        Returns:
            Ethical performance report
        """
        total_decisions = len(self.decision_history)
        ethical_decisions = sum(1 for d in self.decision_history if d.is_ethical())
        
        return {
            'engine': 'OR1ON',
            'total_decisions': total_decisions,
            'ethical_decisions': ethical_decisions,
            'ethical_rate': ethical_decisions / total_decisions if total_decisions > 0 else 0.0,
            'principles': [p.name for p in self.principles],
            'threshold': self.ethical_threshold,
            'recent_decisions': [
                {
                    'action': d.action,
                    'score': d.ethical_score,
                    'ethical': d.is_ethical(),
                    'timestamp': d.timestamp.isoformat()
                }
                for d in self.decision_history[-5:]
            ]
        }
