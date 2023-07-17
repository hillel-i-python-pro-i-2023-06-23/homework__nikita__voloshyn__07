from collections import defaultdict
from typing import DefaultDict, List


def organize_data(humans: List[dict]) -> DefaultDict[str, List[str]]:
    organized_data = defaultdict(list)
    for human in humans:
        organized_data[human['group']].append(human['name'])

    return organized_data
