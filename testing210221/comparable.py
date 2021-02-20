import quantmark as qm
optimizer = qm.QMOptimizer()
backend = qm.QMBackend('qiskit')

import tequila as tq
active_orbitals = {'A1':[1], 'B1':[0]}
molecule = tq.chemistry.Molecule(geometry='H 0.0 0.0 0.0\nLi 0.0 0.0 1.6', basis_set='sto-3g', active_orbitals=active_orbitals)

U = tq.gates.Ry(angle='a', target=0) + tq.gates.X(target=[2,3])
U += tq.gates.X(target=1, control=0)
U += tq.gates.X(target=2, control=0)
U += tq.gates.X(target=3, control=1)

def test(rounds, repetitions):
	for _ in range(rounds):
		res = qm.VQEbenchmark(molecule=molecule, circuit=U, optimizer=optimizer, backend=backend, repetitions=repetitions)
		accuracy = res.accuracy_history
		print(*accuracy, sep="\t")

test(100, 1000)
