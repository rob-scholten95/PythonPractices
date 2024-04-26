class Project:
    def __init__(self, title, category, year):
        self.title = title
        self.category = category
        self.year = year


project1 = Project("Hengelo Stationsgebouw", "Modeling", 2023)

print(project1.title)

