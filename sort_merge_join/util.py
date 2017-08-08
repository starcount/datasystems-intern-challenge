from itertools import product


def cartesian_join(left_rows, right_rows):
    return list(product(left_rows, right_rows))


def rows_sorted_by_field(rows, field_id):
    return sorted(rows, key=lambda x: x[field_id])


def advance(subset, rows, field_id, field_value):
    while len(rows) > 0 and (rows[0][field_id] is field_value):
        subset.append(rows.pop(0))

