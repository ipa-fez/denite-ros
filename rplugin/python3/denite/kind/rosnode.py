import typing

from denite.kind.base import Base
from denite.util import Nvim, UserContext
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy
try:
    import rosgraph
    import rosnode

    def get_node_pid(node: str) -> int:
        master = rosgraph.Master('denite-ros')
        uri = rosnode.get_api_uri(master, node)
        node = ServerProxy(uri)
        pid = node.getPid(self._rosapi_caller_id)[-1]
        return pid

except ModuleNotFoundError:
    def get_node_pid(node: str) -> int:
        raise "imports missing"


class Kind(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'rosnode'
        self.default_action = 'gdb'

    def action_gdb(self, context: UserContext) -> None:
        pid = get_node_pid(context['targets'][0]['word'])
        self.vim.call('nvimgdb#Spawn', 'gdb', 'gdb_wrap.sh', 'gdb -q --pid {}'.format(pid))
