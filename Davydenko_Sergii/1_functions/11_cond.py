from hw_start import insights


# sum, sum_level, sum_general  .... period

def summary(insights):
    if isinstance(insights, dict):
        for key, value in insights.items():

            if key == 'period' and value > 4:
                insights[key] = 7
            elif key == 'period' and value is None:
                insights[key] = 7

            if key == 'metric_sums':
                for values in value:
                    if values['sum_general'] != 0:

                        if insights['api'] == 1:
                            values[
                                'summary'] = f"{(values['sum'] * values['sum_level'] / values['sum_general']) / insights['period']}"
                        elif insights['api'] == 2:
                            values[
                                'summary'] = f"{(values['sum'] * values['sum_level'] ** 2 / values['sum_general']) / insights['period']}"
                        elif insights['api'] == 3:
                            values['summary'] = f"{(values['sum_level'] / values['sum_general']) / insights['period']}"
                        elif insights['api'] == 4:
                            values['summary'] = f"{(values['sum_level'] * 100) / insights['period']}"
                        else:
                            values["summary"] = "Zero division problem!"

                    return print(values)

    elif isinstance(insights, list):
        for insight in insights:
            summary(insight)


summary(insights)
