from hw_start import insights
from Remove_unused import ROOT_KEYS, ENTITI_KEYS_TO_DEL
# Done


def all_in(insights):
    if isinstance(insights, dict):
        copy_ins = insights.copy()
        for key, value in copy_ins.items():
            if key in ROOT_KEYS:
                del insights[key]

    if isinstance(insights, list):
        for insight in insights:
            all_in(insight)

    return print(insights)


all_in(insights)


def in_ent_aff(entitie_lvl):
    entitie_lvl_c = entitie_lvl.copy()
    for key, value in entitie_lvl_c.items():
        if key == 'entities':
            for point in ENTITI_KEYS_TO_DEL:
                for keys in value:
                    if point in keys:
                        del keys[point]
    return entitie_lvl


def all_in(insights):
    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == 'entities_affected':
                in_ent_aff(value)
            else:
                all_in(value)

    if isinstance(insights, list):
        for insight in insights:
            all_in(insight)

    return insights


print(all_in(insights))
