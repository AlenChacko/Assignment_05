# original list
original_list = [1,2,3,4,5,6,7,8,9,10]
extract_limit = 5


def extract_list(lst, lim):
    try:
        if not isinstance(lst, list):
            raise TypeError("Values should be in a list")
        if not isinstance(lim, int):
            raise TypeError("Limit should be integer")
        if lim < 0:
            raise ValueError("Limit cannot be negative")

        return lst[:lim]

    except (ValueError, TypeError) as err:
        print(f"Error: {err}")
        return None


def reverse_list(lst):
    try:
        if lst is None:
            return None
        if not isinstance(lst, list):
            raise TypeError("Values should be in a list")

        return lst[::-1]

    except TypeError as err:
        print(f"Error: {err}")
        return None


extracted_list = extract_list(original_list, extract_limit)
reversed_list = reverse_list(extracted_list)

if extracted_list is not None and reversed_list is not None:
    print(f"Original list: {original_list}")
    print(f"Extracted elements: {extracted_list}")
    print(f"Reversed extracted elements: {reversed_list}")
else:
    print("Operation failed due to invalid input")
