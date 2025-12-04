#SEGUNDO
'''
Docstring for src.integrators

Objetivo: implementar RK4 e Leapfrog/Velocity-Verlet com interface clara.

Implementar funções:

rk4_step(positions, velocities, masses, dt, accel_fn, **accel_args) -> (positions_new, velocities_new)

accel_fn é callable que aceita (positions, masses, **accel_args) e retorna accelerations.

Faça RK4 clássico adaptado a sistema de 2ª ordem (transforme em sistema 1ª ordem ou aplique fórmula padrão).

velocity_verlet_step(positions, velocities, masses, dt, accel_fn, **accel_args) -> (positions_new, velocities_new)

Implementação padrão: x_{n+1} = x_n + v_n dt + 0.5 a_n dt^2; compute a_{n+1}; v_{n+1} = v_n + 0.5 (a_n + a_{n+1}) dt.

integrate(positions0, velocities0, masses, dt, n_steps, method="rk4", accel_fn=..., save_every=1, **accel_args) -> dict

Roda N passos, salva arrays e retorna dicionário com:

positions: array shape (n_saved, N, dim)

velocities: same

times: array

energies: array (total energy per saved step)

save_every controle frequência de gravação.

Requisitos:

Cheque method válido.

Validate shapes.

Pequeno progresso/logging (print every 1000 steps or so).

Test:

Script minimal rodando 2-body, comparar energia inicial/final.
'''
