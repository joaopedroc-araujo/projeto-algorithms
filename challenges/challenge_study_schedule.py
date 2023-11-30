def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    if not all(
        isinstance(i, tuple)
        and len(i) == 2
        and isinstance(i[0], (int, float))
        and isinstance(i[1], (int, float))
        for i in permanence_period
    ):
        return None
    return sum(start <= target_time <= end for start, end in permanence_period)
