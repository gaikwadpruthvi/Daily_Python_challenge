def find_unique_keys(dict1, dict2):
    # Find keys present in dict1 but not in dict2
    unique_keys = set(dict1.keys()) - set(dict2.keys())
    return list(unique_keys)

# Example usage
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5}

print("Keys in dict1 but not in dict2:", find_unique_keys(dict1, dict2))
