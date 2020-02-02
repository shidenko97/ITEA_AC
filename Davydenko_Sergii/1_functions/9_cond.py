from hw_start import insights
# Done

def nine_cond(insights):
    if isinstance(insights, dict):
        copy_insights = insights.copy()
        for key, value in insights.items():
            if key == 'report_name' and value == 'device':
                change = {'report_name': 'DEVICE'}
                copy_insights.update(change)
            else:
                nine_cond(value)
        return print(copy_insights)

    elif isinstance(insights, list):
        for insight in insights:
            nine_cond(insight)


nine_cond(insights)
