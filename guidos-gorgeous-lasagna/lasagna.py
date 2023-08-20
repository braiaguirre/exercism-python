EXPECTED_BAKE_TIME = 40

def bake_time_remaining(actual_time):
    """Calculates the remaining time"""
    return EXPECTED_BAKE_TIME - actual_time

def preparation_time_in_minutes(layers):
    """Total preparation time according to the number of layers"""
    return layers * 2;

def elapsed_time_in_minutes(layers, bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(layers) + bake_time