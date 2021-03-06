from pyquery import PyQuery
from textwrap import wrap

source = 'http://adventofcode.com/2016/day/10'

d = PyQuery(source)

for tag in ('code', 'em'):
    for node in d(tag).items():
        node.replace_with(node.text())

for node in d('p').items():
    content = node.text()
    if node.next() and node.next()[0].tag != 'ul':
        content += '\n'
    node.replace_with(content)

for node in d('li').items():
    node.replace_with('- ' + node.text())
for node in d('ul').items():
    node.replace_with(node.text() + '\n')

for node in d('h2').items():
    header = node.text()[4:-4]
    node.replace_with(header + '\n' + ('=' * len(header)) + '\n\n')

for node in d('pre').items():
    content = '\n'.join('    ' + row for row in node.text().split('\n'))
    node.replace_with(content + '\n')

final = []
margin = 80
for row in d('article').text().split('\n'):
    if row == '':
        final.append(row)
    elif row.startswith('- '):
        sub_rows = wrap(row, margin - 2)
        for i in range(1, len(sub_rows)):
            sub_rows[i] = '  ' + sub_rows[i]
        final.extend(sub_rows)
    else:
        final.extend(wrap(row, margin))

final.append('')
final.append('Part Two')
final.append('========')
final.append('')
final.append('Source: %s\n' % source)
print('\n'.join(final))
