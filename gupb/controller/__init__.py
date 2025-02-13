from abc import abstractmethod
from typing import Protocol

from gupb.model import arenas
from gupb.model import characters


class Controller(Protocol):

    @abstractmethod
    def decide(self, knowledge: characters.ChampionKnowledge) -> characters.Action:
        raise NotImplementedError

    @abstractmethod
    def praise(self, score: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def reset(self, arena_description: arenas.ArenaDescription) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def preferred_tabard(self) -> characters.Tabard:
        raise NotImplementedError

