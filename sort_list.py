# sort_list.py

def remove_duplicates(numbers: list) -> list:
    # Remove duplicates by converting to set, and then convert back to list
    unique_numbers = list(set(numbers))

    return unique_numbers
    
    
def reverse_list(numbers: list) -> list:
    # Sort list in reverse
    sorted_numbers = sorted(unique_numbers, reverse=True)
    
    return sorted_numbers

def validate_list_members(input_list: list) -> bool:
    # Validate list members for conditions

    if len(input_list) != 10:
        print("List not correct size: " + str(len(input_list)))
        return False 
        
    for x in input_list:
        #Check list for non numerics
        if x.isnumeric:
            #Check list for 
            if x < 1 or x > 100: 
                print("Outside boundaries: " + str(x))
                return False
        else: 
            print("Non numeric: " + str(x))
            return False
    
    # No issues above, return True for valid list 
    return True


def main(input_list: list) -> list:
    # Check list for invalid members
    if not validate_list_members(input_list):
        print("Invalid list members")
    else:
        unique_list = remove_duplicates(input_list)
        
        #Check if more than 4 duplicates
        if len(unique_list) - len(input_list) != 4:
            print("Invalid number of duplicates")
        else:
            sorted_list = reverse_list(unique_list)
            return sorted_list
            
    return None

if __name__ == '__main__':
    import sys
    input_list = sys.argv[0:10]
    input_list = [int(x) for x in input_list]
    main(input_list)

