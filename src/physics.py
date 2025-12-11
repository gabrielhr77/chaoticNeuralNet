#PRIMEIRO
'''
Docstring for src.physics

Objetivo: funções puras que definem a física — sem I/O, sem plotting.

Implementar funções:

acceleration(positions: np.ndarray, masses: np.ndarray, G: float = 1.0) -> np.ndarray

    positions: shape (N, 2) ou (N, 3) (use 2D inicialmente).

    masses: shape (N,)

    retorna accelerations: shape (N, 2)

    trate divisão por zero com epsilon.

potential_energy(positions: np.ndarray, masses: np.ndarray, G: float = 1.0) -> float

    calcule soma pairwise -G m_i m_j / r_ij.

kinetic_energy(velocities: np.ndarray, masses: np.ndarray) -> float

    0.5 * sum(m_i * v_i^2).

total_energy(positions, velocities, masses, G=1.0) -> float

    soma cinética + potencial.

(Opcional) center_of_mass(positions, masses) -> np.ndarray — útil para normalizar.



Requisitos:

Docstrings curtos.

Pequenas asserts de forma e tipo (por exemplo, shapes compatíveis).

Test: crie if __name__ == "__main__": com um pequeno 2-corpos e print das energias.
'''
'''
centro de massa de um sistema
R = (M1R1+M2R2+M3R3)/(M1+M2+M3)

força externa do Sol no sistema Terra-Lua
F=-GMsol((Mt/rt**2)^rt + (Ml/rl**2)^rl + )
'''