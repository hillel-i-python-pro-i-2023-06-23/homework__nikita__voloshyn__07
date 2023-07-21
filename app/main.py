from app.data_provider import DataProvider
from app.data_organizer import organize_data
from app.output_formatter import get_formatted_output


def main():
    """
    You have a list of humans. Every human has a "name" and "group".
    Your task is to show all groups, with the amount and names of members of each group.
    """
    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    output = get_formatted_output(data=organized_data)
    print(output)


if __name__ == "__main__":
    main()
