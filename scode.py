 maryam mollaei changing in file 
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


    # اجرای الگوریتم ژنتیک
def genetic_algorithm():
    population = create_population(POPULATION_SIZE, GENE_LENGTH)

    for generation in range(GENERATIONS):
        # ارزیابی fitness
        fitness_scores = [fitness(chromosome) for chromosome in population]

        # انتخاب
        selected_parents = selection(population, fitness)

        # تولید نسل جدید از طریق تقاطع و جهش
        new_population = []
        for i in range(0, len(selected_parents), 2):
            parent1 = selected_parents[i]
            parent2 = selected_parents[i+1] if i+1 < len(selected_parents) else selected_parents[i] # Handle odd population size
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, MUTATION_RATE)
            child2 = mutate(child2, MUTATION_RATE)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population[:POPULATION_SIZE] # Keep population size constant

        # نمایش بهترین نتیجه در هر نسل
        best_chromosome = max(population, key=fitness)
        print(f"نسل {generation+1}: بهترین fitness = {fitness(best_chromosome)}, کروموزوم = {best_chromosome}")

    # نمایش بهترین نتیجه نهایی
    best_chromosome = max(population, key=fitness)
    print(f"بهترین کروموزوم نهایی: {best_chromosome}, fitness = {fitness(best_chromosome)}")

# اجرای الگوریتم
genetic_algorithm()
