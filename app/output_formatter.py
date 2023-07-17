from collections import defaultdict
from typing import DefaultDict, List


def get_formatted_output(data: DefaultDict[str, List[str]]) -> str:
    output = ""
    for group, members in data.items():
        output += f"Group: {group}\n"
        output += f"Number of members: {len(members)}\n"
        output += f"Members: {', '.join(members)}\n\n"

    return output
