import math

COLUMNS = 4
contributors = [
    'Aleksandra Apic',
    'Amelie Dorn',
    'András Barati',
    'Andreas Olschnögger',
    'Asil Çetin',
    'Britta Breuers',
    'Celestine Posch',
    'Clément Besnier',
    'Christof Rauchenberger',
    'Dalibor Pančić',
    'Daniel Kittel',
    'Ekaterini Mitsiou',
    'Enric Rodellas',
    'Eugen Hotwagner',
    'Johannes Preiser-Kapeller',
    'Judith Pucher',
    'Katharina Winckler',
    'Klaus Illmayer',
    'Laura Kremser',
    'Ludwig Maximilian Breuer',
    'Markus Pluschkovits',
    'Mihailo Popović',
    'Moritz Großfurtner',
    'Nicole Zehetmayer-Lorenz',
    'Omar Siam',
    'Peter Andorfer',
    'Petra Heinicker',
    'Roland Filzwieser',
    'Sandra Lehecka',
    'Samvel Grigoryan',
    'Saranya Balasubramanian',
    'Sebastian Majstorovic',
    'Selina Hofbauer',
    'Semra Kilic-Dinler',
    'Seta Štuhec',
    'Silvia Gómez-Senovilla',
    'Stefan Probst',
    'Vera Charvát',
    'Veronika Gründhammer',
    'Zachary Chitwood']


def get_contributor_lists() -> list[list[str]]:
    n = math.ceil(len(contributors) / COLUMNS)
    return list(contributors[i:i+n] for i in range(0, len(contributors), n))
