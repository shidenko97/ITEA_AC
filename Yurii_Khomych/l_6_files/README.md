# HW
1. Develop program that:
    * Get all breakdowns and project_id_to_project_execution from input data `l_6_files/hw_files/input_data.json`
    * For each project execution read analyzer files that endswith `-1.json` inside each `project_id` and `project_execution_id` 
     `l_6_files/hw_files/analyzer/project_id-{9231}/project_execution-{797449}/2-function_name-generate_nb_insights`
     and count number insights with breakdowns in `dimensions` key and all insights.
     Note: You need to check if any "breakdowns" in dimension name, but you also need to 
     use endswith or create new string from each breakdown for comparing.
     `"dimension:age"`
    * Do the same for each project_execution_id `mid` folder `l_6_files/hw_files/mid`.
    Count number of records and count number of records with breakdowns in `dimensions` column.
    * Do the same for `l_6_files/hw_files/final_results`.
    * Make three steps of program that make final output.
    Final output must be:
    ```
    project_id: 9212, project_execution_id: 798275
    analyzer_insights_len: 20
    analyzer_insights_with_br_len: 12
    mid_insights_len: 25
    mid_insights_with_br_len: 14
    final_insights_len: 3
    final_insights_with_br_len: 2
    ```

2. Add to your program ability to get from CLI arguments value `all`, `breakdowns` or `without-breakdowns`
which count only needed insights.

Note:
You should write your realization using functions
and best practices like `main()` function and `if __name__ == '__main__'`.
