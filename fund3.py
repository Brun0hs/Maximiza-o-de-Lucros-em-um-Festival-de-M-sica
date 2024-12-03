from scipy.optimize import linprog

# Coeficientes da função objetivo:
# Maximizar Z = 5000x1 + 3000x2 (lucro por bandas e DJs)
# Como o linprog resolve problemas de minimização, os coeficientes são multiplicados por -1.
c = [-5000, -3000]

# Coeficientes das restrições:
# 1ª restrição: 4x1 + 2x2 <= 50 (espaço disponível no palco)
# 2ª restrição: 2x1 + x2 <= 30 (limitação de técnicos disponíveis)
# 3ª restrição: 7000x1 + 6000x2 <= 100000 (orçamento disponível)
A = [
    [4, 2],        # Coeficientes da restrição de espaço no palco
    [2, 1],        # Coeficientes da restrição de técnicos disponíveis
    [7000, 6000]   # Coeficientes da restrição de orçamento
]

# Lados direitos das desigualdades:
# Corresponde aos limites das restrições.
b = [50, 30, 100000]  

# Limites para as variáveis de decisão (não-negatividade):
# x1 (número de bandas) >= 0
# x2 (número de DJs) >= 0
x0_bounds = (0, None)  # Limite para x1 (bandas)
x1_bounds = (0, None)  # Limite para x2 (DJs)

# Resolução do problema de programação linear usando o método 'simplex'
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='simplex')

# Exibindo o resultado
print("Solução ótima:")
print(f"Número de bandas (x1): {res.x[0]}")
print(f"Número de DJs (x2): {res.x[1]}")
print(f"Lucro total máximo: {-res.fun}")
