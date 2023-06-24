from pathlib import Path


def parse_fractal(frac_config_file):
    """
    Given the path to a fractal configuration file, parse the file and return a dictionary with the information
    required to construct Fractal, Palette, and ImagePainter objects.
    """
    fractal_info = {}

    # process configuration file
    with open(frac_config_file) as f:
        for line in f:
            line = line.strip().replace(" ", "")
            if "#" in line or len(line) == 0:
                continue
            if ":" not in line:
                continue
            key_value = line.split(sep=":", maxsplit=1)
            if key_value[0].lower() not in ["type", "centerx", "centery", "axislength", "pixels", "iterations", "phoenix", "julia", "preal", "pimag", "creal", "cimag"]:
                continue
            fractal_info[key_value[0].lower()] = key_value[1].lower()

    # error handling
    required_keys = ["type", "centerx", "centery", "axislength", "pixels", "iterations"]
    for key in required_keys:
        if key not in fractal_info.keys():
            raise RuntimeError("The required parameter of '{}' is missing".format(key))

    if fractal_info["type"] in ["phoenix", "julia"]:
        required_keys_c = ["creal", "cimag"]
        for key in required_keys_c:
            if key not in fractal_info.keys():
                raise RuntimeError("This is a {} fractal, but the '{}' parameter is missing".format(fractal_info["type"], key))

    if fractal_info["type"] == "phoenix":
        required_keys_phoenix = ["preal", "pimag"]
        for key in required_keys_phoenix:
            if key not in fractal_info.keys():
                raise RuntimeError("This is a Phoenix fractal, but the '{}' parameter is missing".format(key))

    for key in fractal_info.keys():
        if len(fractal_info[key]) == 0:
            raise RuntimeError("Value for the '{}' parameter is missing".format(key))

    integer_keys = ["pixels", "iterations"]
    for key in integer_keys:
        try:
            fractal_info[key] = int(fractal_info[key])
        except ValueError:
            raise RuntimeError("The value of the '{}' parameter is not an integer".format(key))

    float_keys = ["centerx", "centery", "axislength", "creal", "cimag", "preal", "pimag"]
    for key in float_keys:
        if key not in fractal_info.keys():
            continue
        try:
            fractal_info[key] = float(fractal_info[key])
        except ValueError:
            raise RuntimeError("The value of the '{}' parameter is not a number".format(key))

    # calculated fields
    fractal_info["min"] = {"x": fractal_info["centerx"] - (fractal_info["axislength"] / 2.0),
                           "y": fractal_info["centery"] - (fractal_info["axislength"] / 2.0)}
    fractal_info["max"] = {"x": fractal_info["centerx"] + (fractal_info["axislength"] / 2.0),
                           "y": fractal_info["centery"] + (fractal_info["axislength"] / 2.0)}

    fractal_info["pixelsize"] = fractal_info["axislength"] / fractal_info["pixels"]
    
    fractal_info["imagename"] = "{}.png".format(Path(frac_config_file).stem)

    return fractal_info
