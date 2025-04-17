"""
"""

import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_len = 60  # Length of the progress bar
    for i, item in enumerate(lst, 1):
        percent = i / total
        print(percent)
        filled_len = int(bar_len * percent)
        bar = '=' * (filled_len - 1) + '>' + ' ' * (bar_len - filled_len)
        sys.stdout.write(f"\r{int(percent * 100)}%|[{bar}]| {i}/{total}")
        sys.stdout.flush()
        yield item
