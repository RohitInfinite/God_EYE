IMPORTANT_OBJECTS = [
    "person",
    "car",
    "bus",
    "truck",
    "bicycle",
    "motorcycle",
    "chair",
    "table",
    "chair",
    "cell phone",
    "mouse",
    "cup",
    "bottle"
]
def get_direction(cx, frame_width):

    if cx < frame_width / 3:
        return "left"

    elif cx < 2 * frame_width / 3:
        return "center"

    else:
        return "right"


def generate_sentence(label, direction, distance):

    distance = int(distance)

    if distance <= 1:
        return f"Warning! {label} very close. Stop."

    elif distance <= 3:
        return f"{label} nearby on {direction} at {distance} meters"

    elif distance <= 6:
        return f"{label} ahead on {direction} at {distance} meters"

    else:
        return f"{label} far on {direction} at {distance} meters"