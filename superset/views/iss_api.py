from flask_appbuilder import expose
from flask_appbuilder.security.decorators import has_access, has_access_api
from superset.views.base import BaseSupersetView


class IssApi(BaseSupersetView):  # pylint: disable=too-many-public-methods
    """The base views for Superset!"""
    @has_access_api
    @expose("/iss_api_test/", methods=["GET", "POST"])
    def vue_api(self):
        return "hello"


