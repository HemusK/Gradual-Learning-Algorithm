import numpy as np
class candidate:
    def __init__(self, name, constraints, violations):
        self.name = name
        self.constraints = dict{zip(constraints, violations)}
        self.violations = violations
        self.score = 0
    def updateScore(self, update):
        self.score += update
    def updateConstraints(self, constraint, update):
        self.constraints[constraint] += update
    def returnviolation(self, constraint):
        return self.constraints[constraint]
    def returnViolationArray(self):
        return np.array(list(self.constraints.keys()))