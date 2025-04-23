# تنظیمات
POPULATION_SIZE = 50
GENE_LENGTH = 10
MUTATION_RATE = 0.01
GENERATIONS = 100
# تابع هدف (fitness function) - اینجا یک مثال ساده است
def fitness(chromosome):
    # هر چه تعداد بیت های 1 بیشتر باشد، fitness بهتر است
    return sum(chromosome)


# ایجاد جمعیت اولیه
def create_population(size, gene_length):
    population = []
    for _ in range(size):
        chromosome = [random.randint(0, 1) for _ in range(gene_length)]
        population.append(chromosome)
    return population

    # انتخاب والدین (tournament selection)
def selection(population, fitness_function):
    tournament_size = 3
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        best = max(tournament, key=fitness_function)
        selected.append(best)
    return selected
