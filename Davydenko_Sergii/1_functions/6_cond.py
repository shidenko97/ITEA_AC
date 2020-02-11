from hw_start import insights
from Remove_unused import UNIQ_KEY
# Done


def uniq(isights):
    result = []

    if isinstance(isights, dict):
        for key, value in isights.items():
            if key == UNIQ_KEY:
                result.append(value)
                return print(result)
            else:
                uniq(value)

    elif isinstance(isights, list):
        for isight in isights:
            uniq(isight)


uniq(insights)
