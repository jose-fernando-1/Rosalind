def calculate_dominant_probability(k: int, m: int, n: int) -> float:
    total = k + m + n
    total_pairs = total * (total - 1)

    dominant = (k * (k - 1) + 2 * k * m + 2 * k * n + 0.75 * m * (m - 1) + m * n)
    return dominant / total_pairs

with open("C:/Users/josef/Downloads/rosalind_iprb (1).txt") as file:
    parameters = [int(x) for x in file.read().strip().split()]

print(calculate_dominant_probability(*parameters))

def probabilidade_condicional(k: int, m: int, n: int) -> float:
    total = k + m + n
    # probabilidade total = soma das probabilidades de cada par * a probabilidade condicional do fenótipo dominante (ponderamento das probabilidades)
    return 1 * ((k / total) * ((k - 1) / (total - 1))) + 1 * ((k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))) + 1 * ((k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))) + 0.75 * ((m / total) * ((m - 1) / (total - 1))) + 0.5 * ((m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))) + 0 * ((n / total) * ((n - 1) / (total - 1)))

print(probabilidade_condicional(*parameters))