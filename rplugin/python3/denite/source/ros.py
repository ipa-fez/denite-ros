import typing

from denite.source.base import Base
from denite.util import Nvim, UserContext, Candidates
import rospkg


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
        self.name = 'rosed'
        self.kind = 'ros'

    def gather_candidates(self, context: UserContext) -> Candidates:
        rosp = rospkg.RosPack()
        pkg_list = context['args'] if context['args'] else rosp.list()
        return [{'word': pkg, 'ros_pkg_path': rosp.get_path(pkg)} for pkg in pkg_list]
