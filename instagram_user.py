from dataclasses import dataclass, field
from typing import Dict, Tuple, List
import datetime

def default_field(obj):
    return field(default_factory=lambda: obj)


# @dataclass(frozen=True)
# class Status():
#     STATUS_UNFOLLOWING: ClassVar[int] = 0
#     STATUS_FOLLOWING: ClassVar[int] = 1
#     STATUS_REQUESTED: ClassVar[int] = 2
#     STATUS_BLOCKED: ClassVar[int] = 3


@dataclass(unsafe_hash=True)
class User():
    username: int
    name: str
    status: int = 0
    # status_hist: List[Tuple[int, datetime.datetime]] = default_field([(0,datetime.datetime.now())])

    def set_status(self, status:str) -> None:
        button_text = {
            "Follow": 0,
            "Following": 1,
            "Requested": 2,
            "Unblock": 3,
        }
        if self.status != status:
            # self.status_hist.append((self.status, datetime.datetime.now()))
            self.status = button_text.get(status)
    
    # # TODO: Change it to get_history later
    # def view_history(self) -> None:
    #     for (status, time) in self.status_hist:
    #         print(self.convert_status_description(status), time)
    #     return '\n'.join([" > {}: modified at {}".format(status_int, date.strftime("%Y-%m-%d %H:%M")) for (status_int, date) in self.status_hist])

    def view_status(self) -> None:
        print(self.convert_status_description(self.status))

    def convert_status_description(self, status) -> str:
        enum = {
            0: "Not following",
            1: "Following",
            2: "Requested",
            3: "Blocked"
        }
        return enum.get(status)
    
    def __repr__(self):
        return (f'\n{self.__class__.__name__} @{self.username}: {self.name!r} ({self.convert_status_description(self.status)})')

def store_user_json():
    pass