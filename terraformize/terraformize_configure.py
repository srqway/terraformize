from parse_it import ParseIt


def read_configurations(config_folder: str = "config"):
    """
    Will create a config dict that includes all of the configurations for terraformize by aggregating from all valid
    config sources (files, envvars, cli args, etc) & using sane defaults on config params that are not declared

    Arguments:
        :param config_folder: the folder which all configuration file will be read from recursively

    Returns:
        :return config: a dict of all configurations needed for terraformize to work
    """
    print("reading config variables")

    config = {}
    parser = ParseIt(config_location=config_folder, recurse=True)

    config["basic_auth_user"] = parser.read_configuration_variable("basic_auth_user", default_value=None)
    config["basic_auth_password"] = parser.read_configuration_variable("basic_auth_password", default_value=None)
    config["auth_token"] = parser.read_configuration_variable("auth_token",  default_value=None)
    config["max_timeout"] = parser.read_configuration_variable("max_timeout",  default_value=600)
    config["terraform_binary_path"] = parser.read_configuration_variable("terraform_binary_path", default_value=None)
    config["terraform_modules_path"] = parser.read_configuration_variable("terraform_modules_path",
                                                                          default_value="/www/terraform_modules")
    return config