def recommend_colors(skin_tone):
    warm_colors = ["Mustard", "Coral", "Olive Green", "Gold"]
    cool_colors = ["Royal Blue", "Emerald Green", "Silver", "Deep Purple"]
    neutral_colors = ["Beige", "Gray", "Peach", "Soft Pink"]

    if "Warm" in skin_tone:
        return warm_colors
    elif "Cool" in skin_tone:
        return cool_colors
    else:
        return neutral_colors
