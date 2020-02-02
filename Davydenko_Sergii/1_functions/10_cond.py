from hw_start import insights
# Done


def tens_deal(insights):
    if isinstance(insights, dict):
        copy_insights = insights.copy()
        for key, value in insights.items():
            if key == 'page_id' and value == "(not set)":
                change = {'page_id': 'None'}
                copy_insights.update(change)
            else:
                tens_deal(value)

        return print(copy_insights)

    elif isinstance(insights, list):
        for insight in insights:
            tens_deal(insight)


tens_deal(insights)
