from itertools import chain, groupby, starmap, takewhile
from pathlib import Path


def main():
    def toc_level(contents, level=0):
        def get_key(init):
            return tuple(Path(init).parents)[-2]

        def inner(key, group):
            return group
            toc_level()
        # f'{ count }. { title_name }'
        # f'''{
        #     " " * level * 4
        # }- [{
        #     kabob_case
        # }]({
        #     relative_folder
        # }) {
        #     description
        # }'''
        return chain.from_iterable(starmap(inner, groupby(contents, get_key)))
    this_file = Path(__file__)
    readme = this_file.resolve().with_name('README.md')
    toc_line = '# Table of Contents\n'
    with readme.open() as istream:
        lines = tuple(takewhile(lambda line: line != toc_line, istream))
    contents = sorted(map(
        lambda init: f'./{ init.resolve().relative_to(readme.parent) }',
        filter(
            lambda init: 'site-packages' not in str(init),
            this_file.parent.rglob('**/__init__.py'))))
    with readme.open('w') as ostream:
        ostream.writelines(lines)
        ostream.write(toc_line)
        ostream.writelines(toc_level(contents))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
