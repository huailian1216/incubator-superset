# export SUPERSET_CONFIG_PATH=~/superset/conf/superset_config.py

from typing import Any, Callable, Dict, List, Optional, Type, TYPE_CHECKING

from dateutil import tz

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'mysql://root:jsohua@127.0.0.1/superset_0.38'

# tz.gettz('Asia/Shanghai') : Using the time zone with specific name
# [TimeZone List]
# See: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# other tz can be overridden by providing a local_config
DRUID_TZ = tz.gettz('Asia/Shanghai')

# Setup default language
BABEL_DEFAULT_LOCALE = "zh"

# CORS Options
ENABLE_CORS = True
# vue前端保存cookie
CORS_OPTIONS = {
    # 'supports_credentials': True,

    # 'allow_headers': [
    #     'X-CSRFToken', 'Content-Type', 'Origin', 'X-Requested-With', 'Accept',
    # ],
    # 'resources': [
    #     '/login/',
    #      '/superset/csrf_token/',  # auth
    #      '/api/v1/formData/',  # sliceId => formData
    #      '/superset/explore_json/*',  # legacy query API, formData => queryData
    #      '/api/v1/query/',  # new query API, queryContext => queryData
    #      '/superset/fetch_datasource_metadata/'  # datasource metadata
    #
    # ],

    'origins': ['http://10.28.127.229:8089', 'http://10.28.117.183:8081']
}

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False
WTF_CSRF_EXEMPT_LIST = ["superset.views.core.log", "superset.charts.api.data", "superset.views.core.explore_json"]
WTF_CSRF_TIME_LIMIT = None

#
# Flask session cookie options
#
# See https://flask.palletsprojects.com/en/1.1.x/security/#set-cookie-options
# for details
#
# SESSION_COOKIE_HTTPONLY = False  # Prevent cookie from being read by frontend JS?
# SESSION_COOKIE_SECURE = False  # Prevent cookie from being transmitted over non-tls?
SESSION_COOKIE_SAMESITE = None  # One of [None, 'None', 'Lax', 'Strict']

# APP_THEME = "spacelab.css"

from superset.custom_security_manager import CustomSecurityManager
CUSTOM_SECURITY_MANAGER = CustomSecurityManager

# Will allow user self registration
# AUTH_USER_REGISTRATION = True  # 允许用户注册

# The default user self registration role
# AUTH_USER_REGISTRATION_ROLE = "Gamma"  # 设置默认添加用户角色

# PUBLIC_ROLE_LIKE = "Alpha"
# AUTH_ROLE_PUBLIC = "Admin"
# PUBLIC_ROLE_LIKE_GAMMA = True

# Enables the replacement react views for all the FAB views (list, edit, show) with
# designs introduced in SIP-34: https://github.com/apache/incubator-superset/issues/8976
# This is a work in progress so not all features available in FAB have been implemented
ENABLE_REACT_CRUD_VIEWS = True
