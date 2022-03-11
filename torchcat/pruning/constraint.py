from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple


class Constraint(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def feasible(self, solution: Any) -> bool:
        pass


class ConstraintContainer(Constraint):
    def __init__(self, *constraints: Constraint) -> None:
        super().__init__()

        self._constrs = constraints

    def feasible(self, solution: Any) -> bool:
        return all(constr.feasible(solution) for constr in self._constrs)


class ChannelConstraint(Constraint):
    def __init__(self, channel_map: Dict[str, Tuple[int, int]]) -> None:
        super().__init__()

        self._map = channel_map

    def feasible(self, solution: Any) -> bool:
        for start, lenght in self._map.values():
            if not any(solution[start : start + lenght]):
                return False

        return True


class LZeroNorm(Constraint):
    def __init__(self, max_nonzero: int) -> None:
        super().__init__()

        self._max_nonzero = max_nonzero

    def feasible(self, solution: Any) -> bool:
        return sum(solution) <= self._max_nonzero
