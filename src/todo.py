"""todo
TODOのモデル
"""

import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Todo:
    """
    TODOのモデル
    """

    id: int
    created_at: datetime
    deadline: datetime
    title: str
    description: str
    is_finished: bool
