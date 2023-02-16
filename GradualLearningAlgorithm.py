import numpy as np

class GradualLearningAlgorithm:
    def __init__(self, constraints, plasticity):
        self.weights = [1 for i in range(len(constraints))]
        self.constraints = dict(zip(constraints, self.weights))
        self.plasticity = plasticity
        
    def fit(self, real, alternative, epochs):
        for epoch in range(epochs):
            error_vector = {}
            error = 0
            for constraint in self.constraints:
                for word in real:
                    violation = word.returnViolation(constraint)
                    error += violation
                for word in alternative:
                    violation = word.returnViolation(constraint)
                    error -= violation
                error_vector.update({constraint:error})
            
            for constraint in error_vector:
                self.constraints[constraint] += self.plasticity*error_vector[constraint]
            weights = np.array(list(self.constraints.values()))
            noise = np.random.normal(size=np.size(weights))
            noisyweights = weights + noise
            for word in real:
                violations = word.returnViolationArray()
                word.updateScore(np.dot(noisyweights, violations))
            for word in alternative:
                violations = word.returnViolationArray()
                word.updateScore(np.dot(noisyweights, violations))
        print(self.constraints)

    def predict(self, inputs):
        print(self.constraints)
        results = {}
        for input in inputs:
            maxscore = -float("inf")
            output = ""
            for candidate in input["Candidates"]:
                candidatescore = candidate.getScore()
                if candidatescore > maxscore:
                    maxscore = candidatescore
                    output = candidate.getName()
            results.update({input["Name"]:output})
        print(results)
