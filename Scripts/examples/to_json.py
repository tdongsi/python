import collections
import json


def generate_count_queries():
    return "TODO"


class OrderedConfig(collections.OrderedDict):
    pass


class Config(object):
    pass


def get_hive_config():
    """ Get pre-defined Hive configuration.

    :return: Config object for Hive.
    """

    conn = Config()
    conn.type = "hive"
    conn.host = "192.168.5.184"
    conn.user = "cloudera"
    conn.password = "password"
    conn.url = "jdbc:hive2://192.168.5.184:10000/DWH"

    return conn


def get_vertica_config():
    """ Get pre-defined Vertica configuration.

    :return: Config object for Vertica.
    """

    conn = Config()
    conn.type = "vertica"
    conn.host = "192.168.5.174"
    conn.user = "dbadmin"
    conn.password = "password"
    conn.url = "jdbc:vertica://192.168.5.174:5433/VMart"

    return conn


def create_config_file(filename, query_generator):

    hive_source = get_hive_config()
    vertica_target = get_vertica_config()

    config = Config()
    config.source = hive_source
    config.target = vertica_target
    config.testName = "count"
    config.queries = query_generator

    with open(filename, 'w') as config_file:
        json.dump(config, config_file, default=lambda o: o.__dict__, indent=4)


def ordered_config_file(filename, query_generator):

    hive_source = OrderedConfig()
    hive_source["type"] = "hive"
    hive_source["url"] = "jdbc:hive2://192.168.5.184:10000/DWH"
    vertica_target = OrderedConfig()
    vertica_target["type"] = "vertica"
    vertica_target["url"] = "jdbc:vertica://192.168.5.174:5433/VMart"

    config = OrderedConfig()
    config["source"] = hive_source
    config["target"] = vertica_target
    config["testName"] = "count"
    config["queries"] = query_generator

    with open(filename, 'w') as config_file:
        json.dump(config, config_file, indent=4)


def main():

    FILE_NAME = "hive_vertica_count.json"
    query_generator = generate_count_queries()
    create_config_file(FILE_NAME, query_generator)
    ordered_config_file(FILE_NAME, query_generator)


if __name__ == "__main__":
    main()