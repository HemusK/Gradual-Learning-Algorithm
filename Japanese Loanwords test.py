import numpy as np
from GradualLearningAlgorithm import GradualLearningAlgorithm
from CandidateClass import Candidate

constraints = ["*DD", "*NT", "Ident(Voice)", "Ident(Nasal)"]

beddo = Candidate("beddo", constraints, [-1, 0, 0, 0])
betto = Candidate("betto", constraints, [0, 0, -1, 0])
tsundasu = Candidate("tsundasu", constraints, [0, 0,0, -1])
tsuddasu = Candidate("tsuddasu", constraints, [-1, 0, 0, 0])
sampo = Candidate("sampo", constraints, [0, -1, 0, 0])
sambo = Candidate("sampo", constraints, [0, 0, -1, 0])
sappo = Candidate("sappo", constraints, [0, 0, 0, -1])
roddo = Candidate("roddo", constraints, [-1, 0, 0, 0])
rotto = Candidate("rotto", constraints, [0, 0, -1, 0])
rondo = Candidate("rondo", constraints, [0, 0, 0, -1])
fundzukeru = Candidate("fundzukeru", constraints, [0, 0, -1, 0])
funtsukeru = Candidate("funtsukeru", constraints, [0, 0, 0, 0])

bed = {"Name":"bed", "Candidates":[beddo, betto]}
tsukdas = {"Name":"tsukdas", "Candidates":[tsundasu, tsuddasu]}
saNpo = {"Name":"sampo", "Candidates":[sampo, sambo, sappo]}
rod = {"Name":"rod", "Candidates":[roddo, rotto, rondo]}
fumtsukeru = {"Name":"fumtsukeru", "Candiatdes":[fundzukeru, funtsukeru]}

realwords = [[beddo], [tsundasu], [sampo], [fundzukeru]]
alternatives = [[betto], [tsuddasu], [sambo, sappo], [funtsukeru]]

underlying = [bed, tsukdas, saNpo, fumtsukeru]

test_epochs = [100]
GLA = GradualLearningAlgorithm(constraints, .001)
for epoch in test_epochs:
    for i in range(len(realwords)):
        GLA.fit(realwords[i], alternatives[i], epoch)


GLA.predict([rod])
