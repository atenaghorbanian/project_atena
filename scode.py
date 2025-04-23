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

# تقاطع (cross-over) - تک نقطه ای
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2



# جهش (mutation)
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # تعویض 0 به 1 و بالعکس
    return chromosome 