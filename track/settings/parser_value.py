from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class TrackValue:
    project_name: str
    time: list[str | int]


@dataclass(frozen=True, kw_only=True)
class StatValue:
    project_name: str
    days: int


TrackData = dict[str, list[str | int]]
JsonData = dict[str, list[list[str | int]]]
