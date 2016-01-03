import json


def get_total(doc, ignore=None):
    if isinstance(doc, list):
        return sum(get_total(item, ignore) for item in doc)
    if isinstance(doc, dict):
        if ignore is not None and ignore in doc.values():
            return 0
        return sum(get_total(value, ignore) for _, value in doc.items())
    if isinstance(doc, int):
        return doc
    return 0


def main():
    with open('input.txt') as f:
        raw_json = f.read()

    doc = json.loads(raw_json)

    print('The sum of all numbers is: %d.' % get_total(doc))
    print('Without red, the sum of all numbers is: %d.' % get_total(doc, 'red'))

if __name__ == '__main__':
    main()
