class Interval(object):
    """
        Class to store intervals
    """
    def __init__(self, *args):
        if len(args) > 2:
            raise OverflowError("Can accept 2 points. Got : {}".format(len(args)))
        self.start = min(args)
        self.end = max(args)

    def __str__(self):
        return "({}, {})".format(self.start, self.end)

    def __repr__(self):
        return self.__str__()

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end


def compare_start(interval1, interval2):
    """
    Args:
        interval1: object of Interval
        interval2: object of Interval

    Returns: Boolean
        It returns True when the start of second interval is higher

    """
    return interval1.get_start() < interval2.get_start()


def is_overlap_internal(set_of_line1, set_of_line2):
    """
    Args:
        set_of_line1: object of interval
        set_of_line2: object of interval

    Returns: Boolean
        It returns True when the overlap is possible otherwise False

    """
    if compare_start(set_of_line1, set_of_line2):
        first = set_of_line1
        second = set_of_line2
    else:
        first = set_of_line2
        second = set_of_line1
    return first.get_end() > second.get_start()


def is_overlap(x1, x2, x3, x4):
    """

    Args:
        x1: First line on x-axis
        x2: Second line on x-axis
        x3: Third line on x-axis
        x4: Fourth line on x-axis

    Returns: Boolean
        It returns True when the overlap is possible otherwise False

    """
    point1 = (x1, x2)
    point2 = (x3, x4)
    interval1 = Interval(*point1)
    interval2 = Interval(*point2)
    return is_overlap_internal(interval1, interval2)