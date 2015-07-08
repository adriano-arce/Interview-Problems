import re


def get_domain_names(html):
    pattern = r"https?:\/\/(?:w{3}\.)?([a-zA-Z\d\-]+(?:\.[a-zA-Z\d\-]+)+)"
    regex = re.compile(pattern)
    domain_names = set(regex.findall(html))
    return sorted(domain_names)


def main():
    with open("input.html", "r") as f:
        html = f.read()
    print(get_domain_names(html))

if __name__ == "__main__":
    main()