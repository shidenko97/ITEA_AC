import os
import Serhii_Hidenko.l_6_files.hw.task_1

if __name__ == "__main__":

    if os.environ["output_file"]:
        Serhii_Hidenko.l_6_files.hw.task_1.output_file = os.environ["output_file"]

    Serhii_Hidenko.l_6_files.hw.task_1.main()
