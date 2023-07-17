import random
from faker import Faker


class DataProvider:
    def __init__(self):
        self._faker = Faker()

    def _generate_group_names(self, amount=10):
        return [self._faker.unique.company() for _ in range(amount)]

    def _generate_human(self, group_name):
        return {"name": self._faker.unique.first_name(), "group": group_name}

    def _generate_humans(self, groups, amount_of_humans):
        members = []
        for _ in range(amount_of_humans):
            group_name = random.choice(groups)
            group_member = self._generate_human(group_name)
            members.append(group_member)
        return members

    def generate_group_members(self, amount_of_groups=None, amount_of_humans=None):
        amount_of_groups = amount_of_groups or random.randint(5, 10)
        amount_of_humans = amount_of_humans or random.randint(3, 30)

        groups = self._generate_group_names(amount_of_groups)
        group_members = self._generate_humans(groups, amount_of_humans)
        return group_members
