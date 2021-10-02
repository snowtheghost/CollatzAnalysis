def odd_results(limit):
    results = {}
    for n in range(limit):
        if n % 2 != 0:
            results[n] = 3 * n + 1
    return results


def exponential_results(limit):
    results = {}
    for x in range(limit):
        results[x] = 2 ** x
    return results


def find_common(results1, results2):
    matches = []
    for key in results1:
        if results1[key] in results2.values():
            matches.append(key * 2)
    return matches


def even_to_odd_results(limit):
    results = {}
    for n in range(limit):
        if n % 2 == 0:
            result = n / 2
            if result.is_integer() and result % 2 != 0:
                results[n] = int(result)
    return results


def print_results(results, name=None):
    if name is not None:
        for i in results:
            print(f"{name} = {i}: {results[i]}")
    else:
        for i in results:
            print(results[i])


def extend(results, factor):
    if isinstance(results[list(results.keys())[0]], int):
        for i in results:
            results[i] = [results[i]]

    for i in results:
        for _ in range(factor):
            if results[i][-1] % 2 == 0:
                results[i].append(results[i][-1] // 2)
            else:
                results[i].append(results[i][-1] * 3 + 1)


def remove_decreasing(results):
    to_pop = []
    for i in results:
        if i > min(results[i]) or i == 1:
            to_pop.append(i)
    for i in to_pop:
        results.pop(i)
    return to_pop


def get_pattern(removed):
    i = 0
    if len(removed) <= 1:
        return "No pattern found"
    else:
        delta = removed[i+1] - removed[i]

    while i + 1 < len(removed):
        if removed[i+1] - removed[i] != delta:
            return "No pattern found"
        i += 1

    pattern = f"{delta}x {sign(removed[i] - delta)} {abs(delta - removed[0])}"
    return pattern


def sign(number):
    if number >= 0:
        return "+"
    else:
        return "-"


if __name__ == "__main__":
    results = odd_results(100)
    print_results(odd_results(100), "n")
    input()

    while len(results.keys()) > 0:
        extend(results, 1)
        removed = remove_decreasing(results)
        if len(removed) > 0:
            print(removed)
            print(get_pattern(removed))
            print_results(results, "n")
            input()
        # print(get_pattern(remove_decreasing(results)))
