def min_in_neighborhood(values, location):
    assert len(values) > 0 
    assert 0 <= location < len(values)
    "return the lowest value of neighbors in a string"
    if location == 0:
        if values[location] < values[location + 1]:
            return values[location]
        return values[location + 1]