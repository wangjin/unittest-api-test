import os
from configparser import ConfigParser


def get_options(section, key):
    """
    获取指定区域的配置项key value
    :param config_file_name: 配置文件名称
    :param section: 需要读取的区域
    :return: 对应配置
    """
    file = os.path.abspath(os.path.join(os.getcwd(), '..', 'config', 'config.ini'))
    cp = ConfigParser()
    cp.read(file, encoding='utf-8')
    return cp.get(section, key)
