import functools


def log_params(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params_info = {}
        func_args = func.__code__.co_varnames

        for arg_name, arg_value in zip(func_args, args):
            params_info[arg_name] = type(arg_value).__name__

        for arg_name, arg_value in kwargs.items():
            params_info[arg_name] = type(arg_value).__name__

        print(params_info)

        return func(*args, **kwargs)
    
    return wrapper


@log_params
def example_function(a, b, c, d, e, f):
    return f"{a}, {b}, {c}, {d}, {e}, {f}"


example_function(42, "hello", c=3.14, d=[1, 2, 3], e=(1, 2, 3), f={"x": 1, "y": 2})