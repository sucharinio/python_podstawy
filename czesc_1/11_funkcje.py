def sum_list(_to_sum = None):
    if _to_sum is None:
        _to_sum = []

    _sum = 0
    for ii in _to_sum:
        _sum = _sum + ii

    return _sum


print(sum_list())
print(sum_list([1, 2, 3, 4]))
