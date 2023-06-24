from Palette import PaletteOne, PaletteTwo


def palette_factory(fractal_info, palette_name="palettetwo"):
    """
    Given the name of a palette and a fractal information dictionary,
    return a palette object of the type palette_name
    """
    if palette_name.lower().strip() == "paletteone":
        return PaletteOne(fractal_info)
    elif palette_name.lower().strip() == "palettetwo":
        return PaletteTwo(fractal_info)
    else:
        raise NotImplementedError("The palette '{}' does not exist".format(palette_name))
