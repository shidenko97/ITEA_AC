from Serhii_Hidenko.l_3_oop.hw.baseinsight import BaseInsight
from Serhii_Hidenko.source.hw_start import insights


if __name__ == "__main__":

    try:
        bi = BaseInsight(**insights[7])
    except ValueError as err:
        print(f"Error: {err}")
    else:
        print(f"dict: {bi.__dict__}")
        print(
            f"get attr `report_name`: {bi.get_attribute_by_name('report_name')}"
        )
        print(f"print attr `report_name`: ", end="")
        bi.print_attribute_by_name("report_name")
        print(bi.currency)
        print(bi.unit)
        print(bi.print)
        print(bi.get_report_name_uppercase())
        print(bi.api_name)
