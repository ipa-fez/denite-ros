import typing

from denite.filter.base import Base
from denite.util import Nvim, UserContext, Candidates


class Filter(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'matcher/ignore_system_ros_pkgs'
        self.description = 'hide ROS packages installed to /opt/ros'

    def filter(self, context: UserContext) -> Candidates:
        return [x for x in context['candidates'] if not 'ros_pkg_path' in x or not x['ros_pkg_path'].startswith('/opt/ros')]
