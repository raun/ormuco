def compare_version(version1, version2):
    """
    Args:
        version1: first version number string
        version2: first version number string

    Returns: Integer
        Returns 0 in case the versions are equal
        Returns positive integer if the first version is later than second
        Returns negative integer if the first version is earlier than second

    """
    version1, version2 = (map(int, version.split('.')) for version in [version1, version2])
    version1, version2 = zip(*map(lambda part1, part2: (part1 or 0, part2 or 0), version1, version2))

    for i in range(len(version1)):
        if version1[i] != version2[i]:
            return version1[i] - version2[i]
    return 0
