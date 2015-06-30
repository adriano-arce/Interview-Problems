import re


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year
    string followed by the name-rank strings in alphabetical order.

    The HTML file looks something like:
        ...
        <h3 align="center">Popularity in 1990</h3>
        ....
        <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
        <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
        <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
        ...

    The output should look something like:
        ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895',  ...]
    """
    year_pattern = r"<h3 align=\"center\">Popularity in (\d{4})</h3>"
    name_rank_pattern \
        = r"<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
    year_regex = re.compile(year_pattern)
    name_rank_regex = re.compile(name_rank_pattern)

    with open(filename, 'r') as f:
        html = f.read()

    year = -1
    year_match = year_regex.search(html)
    if year_match:
        years = year_match.groups()
        if len(years) == 1:
            year = years[0]

    name_dict = {}
    name_ranks = name_rank_regex.findall(html)
    for rank, boy, girl in name_ranks:
        add_name_rank(boy, rank, name_dict)
        add_name_rank(girl, rank, name_dict)

    data_list = [year]
    for name in sorted(name_dict):
        data_list.append("{} {}".format(name, name_dict[name]))
    return data_list


def add_name_rank(name, rank_str, name_dict):
    """
    Adds the (name, rank) key-value pair to the dictionary.
    If a repeated name is found, then we use the one with the smaller rank.
    """
    name_dict[name] = min(name_dict.get(name, float("Inf")), int(rank_str))


def main():
    data_list = extract_names("baby1990.html")
    print("\n".join(data_list))


if __name__ == "__main__":
    main()