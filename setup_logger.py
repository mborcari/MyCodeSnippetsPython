
# Função auxiliar para registrar log.
def setup_logger(file_name, path_log, name="caapi", file_level='INFO'):
    """ Gera um instância de logger

    Args:
        file_name (string): Nome do arquivo txt onde será registrado o log
        path_log (string): Caminho do arquivo txt
        name (str, optional): Nome do setup. Defaults to "caapi".
        file_level (string, optional): Nível do debug. Defaults to 'INFO'.

    Returns:
        [logger]: Instância do logger
    """

    from time import localtime, strftime
    import logging

    if file_level == "DEBUG":
        level = logging.DEBUG
    elif file_level == "INFO":
        level = logging.INFO
    elif file_level == "WARNING":
        level = logging.WARNING
    elif file_level == "ERROR":
        level = logging.ERROR
    elif file_level == "CRITICAL":
        level = logging.CRITICAL
    else:
        level = logging.INFO

    # definição do formato do log
    local_time = localtime()
    #time_string = strftime("%m_%d_%Y_%H_%M_%S", local_time)
    time_string = strftime("%d_%m_%Y", local_time)
    log_file = path_log + file_name + "_" + time_string + ".log"
    FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s")
    file_handler = logging.FileHandler(log_file, "w", encoding="UTF-8")
    file_handler.setFormatter(FORMATTER)
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    logger.setLevel(level)
    return logger