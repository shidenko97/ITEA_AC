from Serhii_Hidenko.l_3_oop.hw.baseinsight import BaseInsight
from Serhii_Hidenko.source.hw_start import insights


if __name__ == "__main__":

    try:
        bi = BaseInsight(**insights[7])
    except ValueError as err:
        print(f"Error: {err}")
    else:
        print(f"dict: {bi.__dict__}")
