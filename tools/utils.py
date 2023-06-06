import logging
import yaml
CONFIG_PATH=".conf/send-webhook.yaml"

def get_logger():
    # create logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    return logger

def load_conf(conf_path: str):
    """
    Load yaml file.
    Parameters
    ----------

    Return
    ------
    Dictionary
        Dictionary with yaml file content
    """
    try:
        with open(conf_path) as stream:
            try:
                yaml_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.error('Error when opening YAML file.', exc_info=1)
    except FileNotFoundError:
        logger.error('Error when opening YAML file.')
        return

    return yaml_dict

conf_yaml=load_conf(CONFIG_PATH)
