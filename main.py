#Starting and Finishing Position

def coordinate_of_position()->None:
    pos_s : str = input("Pls enter the starting position")
    pos_f : str = input("Pls enter the finishing position")

    co_pos_s : tuple = pos_s.split(",")
    co_pos_f : tuple = pos_f.split(",")

    return (co_pos_s, co_pos_f)



