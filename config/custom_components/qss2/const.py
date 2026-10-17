"""Constants for the QuestDB State Storage integration."""

from enum import StrEnum

NAME = "QuestDB State Storage (QSS)"
DOMAIN = "qss2"
ISSUES_URL = "https://github.com/jesch59/qss2/issues"

CONF_TABLE_NAME = "table_name"
CONF_MAX_BATCH_SIZE = "max_batch_size"
CONF_FLUSH_INTERVAL_SECONDS = "flush_interval_seconds"

DEFAULT_TABLE_NAME = "qss2"
DEFAULT_MAX_BATCH_SIZE = 500
DEFAULT_FLUSH_INTERVAL_SECONDS = 5

CONF_AUTH = "authentication"
CONF_AUTH_SSL_CHECK = "ssl_check"
CONF_AUTH_KID = "kid"
CONF_AUTH_D_KEY = "d_key"
CONF_AUTH_X_KEY = "x_key"
CONF_AUTH_Y_KEY = "y_key"
CONF_CONV = "conversion"
CONF_DATA_TYPE = "data_type"
CONF_PRECISION = "precision"

RETRY_WAIT_SECONDS = 5
RETRY_ATTEMPTS = 150

class DataType(StrEnum):
    """Data types used by sensor etc."""

    STRING = "string"
    INT16 = "int16"
    INT32 = "int32"
    INT64 = "int64"
    UINT16 = "uint16"
    UINT32 = "uint32"
    UINT64 = "uint64"
    FLOAT16 = "float16"
    FLOAT32 = "float32"
    FLOAT64 = "float64"



STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
Custom integration: {NAME}
In case of any problem, please open a new issue here:
{ISSUES_URL}
-------------------------------------------------------------------
"""
