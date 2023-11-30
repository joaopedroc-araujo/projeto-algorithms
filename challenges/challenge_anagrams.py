def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    def quick_sort(string):
        if len(string) <= 1:
            return string
        else:
            pivot = string[0]
            left = [char for char in string[1:] if char <= pivot]
            right = [char for char in string[1:] if char > pivot]
            return quick_sort(left) + [pivot] + quick_sort(right)

    if first_string == "" and second_string == "":
        return (first_string, second_string, False)
    else:
        first_string_lowered = first_string.lower()
        second_string_lowered = second_string.lower()
        ordinated_first_string = "".join(quick_sort(first_string_lowered))
        ordinated_second_string = "".join(quick_sort(second_string_lowered))
        if ordinated_first_string == ordinated_second_string:
            return (ordinated_first_string, ordinated_second_string, True)
        else:
            return (ordinated_first_string, ordinated_second_string, False)
