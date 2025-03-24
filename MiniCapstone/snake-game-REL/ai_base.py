from abc import ABC, abstractmethod
from snake import GameOutcome

class SystemState:
    def __init__(self):
        # Information about food
        self.food_north = False
        self.food_south = False
        self.food_east = False
        self.food_west = False
        
        # Obstacles around the snake
        self.obj_north = 0
        self.obj_south = 0
        self.obj_east = 0
        self.obj_west = 0
        self.obj_north_east = 0
        self.obj_north_west = 0
        self.obj_south_east = 0
        self.obj_south_west = 0
        
        # Current movement direction of the snake
        self.dir_x = 0
        self.dir_y = 0

class DecayingFloat:
    # A float variable that can decay over time
    def __init__(self, value: float, factor: float = None, minval: float = None, mode: str = "exp"):
        self.init = value
        self.value = value
        self.factor = factor
        self.minval = minval
        self.mode = mode

    def __float__(self):
        return float(self.value)

    def reset(self):
        # Reset to the initial value
        self.value = self.init

    def decay(self):
        # Decrease the value according to the specified mode (exponential or linear)
        if self.factor is None:
            return

        if self.mode == "exp":
            self.value *= self.factor
        elif self.mode == "linear":
            self.value -= self.factor
        
        if self.minval is not None and self.value < self.minval:
            self.value = self.minval

class AI_Base(ABC):
    # Base class for the snake AI
    def __init__(self):
        self._name = "Human Player"
        self._state = None

    def get_name(self) -> str:
        return self._name

    def state_str(self, state: SystemState) -> str:
        # Return a string representation of the current state
        return f"[{'> ' if state.food_east else ' '}" \
               f"{'v' if state.food_south else ' '}" \
               f"{'< ' if state.food_west else ' '}" \
               f"{'^' if state.food_north else ' '}]," \
               f"[{state.obj_north:+d},{state.obj_south:+d},{state.obj_east:+d},{state.obj_west:d}]" \
               f"-{'U' if state.dir_y==-1 else 'D' if state.dir_y==1 else 'L' if state.dir_x==-1 else 'R'}"

    def is_keyboard_allowed(self) -> bool:
        # By default, AI does not allow manual keyboard control
        return False

    @abstractmethod
    def callback_take_action(self, state: SystemState) -> (int, int):
        # AI selects an action based on the current state
        return state.dir_x, state.dir_y

    @abstractmethod
    def callback_action_outcome(self, state: SystemState, outcome: GameOutcome):
        # Receive feedback from the environment after taking an action
        pass

    def callback_terminating(self):
        # Handle game termination (e.g., save data, log information, etc.)
        pass
