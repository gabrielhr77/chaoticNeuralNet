#QUARTO
'''
Docstring for src.plots

Objetivo: funções para gerar os gráficos exigidos: energia vs tempo e trajetórias.

Implementar funções:

plot_energy(times: np.ndarray, energies: np.ndarray, labels: dict=None, out_path=None)

plota energia total vs tempo. Aceita múltiplas séries (por exemplo, RK4 vs Leapfrog) — usar labels para legendas.

Salva PNG em figs/energy_<tag>.png se out_path fornecido.

plot_trajectories(positions: np.ndarray, masses: np.ndarray=None, out_path=None, show=True)

Para N corpos, plota trajetórias 2D (x vs y) — color different bodies, marker start/end.

plot_energy_error(times, energies, baseline_energy, out_path=None)

plota E(t) - E(0) ou relative error.

Requisitos:

Não definir cores fixas (mas ok usar matplotlib default).

Títulos, eixos, legends, grid.

Document where to save figs (e.g., figs/).

Test:

if __name__ == "__main__": load a sample .npz and produce 2 plots.
'''