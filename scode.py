# تنظیمات
POPULATION_SIZE = 50
GENE_LENGTH = 10
MUTATION_RATE = 0.01
GENERATIONS = 100
# تابع هدف (fitness function) - اینجا یک مثال ساده است
def fitness(chromosome):
    # هر چه تعداد بیت های 1 بیشتر باشد، fitness بهتر است
    return sum(chromosome)