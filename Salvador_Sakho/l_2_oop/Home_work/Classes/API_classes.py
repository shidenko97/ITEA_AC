from Salvador_Sakho.l_2_oop.Home_work.Classes.BaseInsight_class \
    import BaseInsight


class FacebookInsight(BaseInsight):
    facebook_insight = {}

    def __init__(self):
        for api_val, dimension_data, dimensions_dict_data in \
                zip(BaseInsight().get_task_1_dict()['api'],
                    BaseInsight().get_task_1_dict()['dimensions'],
                    BaseInsight().get_task_1_dict()['dimensions_dict']):
            if api_val == 1 and len(self.facebook_insight.keys()) > 0:
                self.facebook_insight['dimensions_data_collection'].append(
                    {'dimensions': dimension_data,
                     'dimensions_dict': dimensions_dict_data})
            elif api_val == 1 and api_val not in self.facebook_insight.keys():
                self.facebook_insight['dimensions_data_collection'] = [
                    {'dimensions': dimension_data,
                     'dimensions_dict': dimensions_dict_data}
                ]

    def get_insight(self):
        return self.facebook_insight['dimensions_data_collection']


class GoogleInsight(BaseInsight):
    google_insight = {}

    def __init__(self):
        for api_val, actions_data in \
                zip(BaseInsight().get_task_1_dict()['api'],
                    BaseInsight().get_task_1_dict()['actions']):
            if api_val == 2 and len(self.google_insight.keys()) > 0:
                self.google_insight['actions_data_collection'].append(
                    actions_data
                )
            elif api_val == 2 and api_val not in self.google_insight.keys():
                self.google_insight['actions_data_collection'] = [actions_data]

    def get_insight(self):
        return self.google_insight['actions_data_collection']


class TwitterInsight(BaseInsight):
    twitter_insight = {}

    def __init__(self):
        for api_val, first_date_data, last_date_data in \
                zip(BaseInsight().get_task_1_dict()['api'],
                    BaseInsight().get_task_1_dict()['first_date'],
                    BaseInsight().get_task_1_dict()['last_date']):
            if api_val == 1 and len(self.twitter_insight.keys()) > 0:
                self.twitter_insight['twitter_data_collection'].append(
                    {'first_date': first_date_data,
                     'last_date': last_date_data})
            elif api_val == 1 and api_val not in self.twitter_insight.keys():
                self.twitter_insight['twitter_data_collection'] = [
                    {'first_date': first_date_data,
                     'last_date': last_date_data}
                ]

    def get_insight(self):
        return self.twitter_insight['twitter_data_collection']


class SnapchatInsight(BaseInsight):
    snapchat_insight = {}

    def __init__(self):
        for api_val, weight_data, type_data in \
                zip(BaseInsight().get_task_1_dict()['api'],
                    BaseInsight().get_task_1_dict()['weight'],
                    BaseInsight().get_task_1_dict()['type']):
            if api_val == 1 and len(self.snapchat_insight.keys()) > 0:
                self.snapchat_insight['snapchat_data_collection'].append(
                    {'weight': weight_data,
                     'type': type_data})
            elif api_val == 1 and api_val not in self.snapchat_insight.keys():
                self.snapchat_insight['snapchat_data_collection'] = [
                    {'weight': weight_data,
                     'type': type_data}
                ]

    def get_insight(self):
        return self.snapchat_insight['snapchat_data_collection']
