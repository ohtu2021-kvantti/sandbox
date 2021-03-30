#%%
import typing
import quantmark as qm
from dataclasses import dataclass

#%%
# Example imput and output things
@dataclass
class Molecule:
    geometry: str
    basis_set: str
    active_orbitals: str = None
    transformation: str = None

@dataclass
class InputData:
    molecule: Molecule
    circuit: str
    optimizer_module: str
    optimizer_method: str

@dataclass
class OutputData:
    average_history: typing.List[float]
    accuracy_history: typing.List[float]
    qubit_count: int
    gate_depth: int
    average_iterations: float
    success_rate: float

# %%
# Exaample data is originally from tequla-tutorials
example_molecule = Molecule(
    geometry='H 0. 0.0 0.0\nLi 0.0 0.0 1.6',
    basis_set='sto-3g',
    active_orbitals='A1 1\nB1 0',
    transformation=None
)

example_input_data = InputData(
    molecule=example_molecule,
    circuit="""
        circuit: 
        Ry(target=(0,), parameter=a)
        X(target=(2,))
        X(target=(3,))
        X(target=(1,), control=(0,))
        X(target=(2,), control=(0,))
        X(target=(3,), control=(1,))
    """,
    optimizer_module='scipy',
    optimizer_method='BFGS'
)

# %%
def example_worker(input: InputData):
    optimizer = qm.QMOptimizer(module=input.optimizer_module, method=input.optimizer_method)
    backend = qm.QMBackend(backend='qulacs')
    circuit = qm.circuit.circuit_from_string(input.circuit)
    molecule = qm.molecule.create(
        geometry=input.molecule.geometry,
        basis_set=input.molecule.basis_set,
        active_orbitals=input.molecule.active_orbitals,
        transformation=input.molecule.transformation
    )
    result = qm.vqe_benchmark(
        molecule=molecule,
        circuit=circuit,
        optimizer=optimizer,
        backend=backend,
        repetitions=100
    )
    return OutputData(
        average_history=result.average_history,
        accuracy_history=result.accuracy_history,
        qubit_count=result.qubit_count,
        gate_depth=result.gate_depth,
        average_iterations=result.average_iterations,
        success_rate=result.success_rate
    )

# %%
print(example_worker(example_input_data))
