class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted

first_gratitude = Gratitudes()
first_gratitude.add("health")
first_gratitude.add("and youth")
print(first_gratitude.format())