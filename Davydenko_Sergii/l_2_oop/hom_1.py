from hw_start import insights
from Davydenko_Sergii.l_2_oop.BaseInsight import BaseInsight


for insight in insights:

    try:
        apisnik = BaseInsight(**insight)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(apisnik.__dict__)
