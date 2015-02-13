
def is_pandigital(n):
        return len(set(sorted(n.replace('0', '')))) == 9
