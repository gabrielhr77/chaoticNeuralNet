#TERCEIRO

'''
Docstring for src.simulate

Objetivo: scripts para montar condições iniciais, rodar integrações em lote e salvar datasets.

Implementar funções / CLI script:

default_two_body() e default_three_body()

Geram positions0, velocities0, masses com comentários (ex.: circular orbit initial conditions).

run_simulation_case(case_name, positions0, velocities0, masses, dt, n_steps, method, save_path)

Usa integrate e salva resultado em data/raw/<case_name>.npz com arrays: positions, velocities, times, energies, masses, meta (dict serializado com params).

generate_dataset(n_cases, out_path, vary_params=True, seed=0)

Automatiza N simulações com variação de condições iniciais (masses, separações, small random perturbations, níveis de ruído).

Salva um único data/processed/dataset.npz contendo arrays stacked ou um índice para arquivos individuais. Estrutura sugerida:

dataset = {
  "positions": shape (num_cases, T, N, dim),
  "velocities": ...
  "masses": shape (num_cases, N),
  "times": shape (T,),
  "meta": list of dicts per case
}


Se memória for problema, salve arquivos separados por caso.

add_noise(data, snr) utility to create noisy versions.

Requisitos:

Use numpy.savez_compressed or h5py if large.

CLI guard: if __name__ == "__main__": permitir rodar gerar um pequeno dataset de teste.

Checkpoint:

Ao rodar python src/simulate.py --test, deve gerar um arquivo .npz em data/raw e imprimir stats (min/max energy drift).
'''