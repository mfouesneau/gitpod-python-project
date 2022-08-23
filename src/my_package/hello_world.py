def hello_world():
    return "Hello World!"


def hello_name(name: str) -> str:
    """_summary_

    Args:
        name (str): _description_

    Returns:
        str: _description_
    """
    return "Hello {}!".format(name)


if __name__ == "__main__":
    hello_world()
