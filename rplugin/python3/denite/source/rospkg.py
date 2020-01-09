import typing

from denite.source.base import Base
from denite.util import Nvim, UserContext, Candidates

try:
    from rospkg import RosPack
except ImportError:
    class RosPack:
        def list(self):
            return []

        def get_path(self, pkg):
            return ""


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
        self.name = 'rospkg'
        self.kind = 'rospkg'

    def gather_candidates(self, context: UserContext) -> Candidates:
        rosp = RosPack()
        pkg_list = context['args'] if context['args'] else rosp.list()
        return [{'word': pkg, 'ros_pkg_path': rosp.get_path(pkg)} for pkg in pkg_list]
