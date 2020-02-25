from Serhii_Hidenko.l_4_iterators_generators.hw.baseinsight import BaseInsight
from Serhii_Hidenko.source.hw_start import insights


if __name__ == "__main__":

    for insight in insights:

        try:
            bi = BaseInsight.from_dict(insight)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(bi.to_dict())
            bi["test"] = "test"
            print(bi["test"])
            del bi["test"]
