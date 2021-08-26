import pathlib
import time


class RequestFlowController:
    def __init__(
        self,
        flow_capacity: int,
        time_range: int,
        state_file: pathlib.Path = None,
    ) -> None:
        '''The constructor.

        Args:
            flow_capacity (int): The maximum request allowed
                in the given time range.
            time_range (int): The time range (in seconds).
            state_file (pathlib.Path): The file that used to
                store the flow state.
        '''

        self._flow_capacity: int = flow_capacity
        self._time_range: int = time_range
        self._ref_timestamp: float = None
        self._req_count: int = 0
        self._state_file: pathlib.Path = state_file

        if self._state_file:
            self._recover_state()

    def _recover_state(self) -> None:
        '''Recover the flow state from the given file.
        If the file is empty, create it.

        Raises:
            StateRecoveryError: If no file is given or
                if data is corrupted.
        '''

        if not self._state_file:
            raise StateRecoveryError('No state file given.')

        if not self._state_file.exists():
            self._state_file.touch()

        if states := self._state_file.read_text().split():
            try:
                self._ref_timestamp = float(states[0])
                self._req_count = int(states[1])
            except (IndexError, ValueError):
                self._ref_timestamp = None
                self._req_count = 0

                raise StateRecoveryError(
                    'The file data seems to be corrupted.'
                )

    def _save_state(self) -> None:
        '''Save the self._ref_timestamp and self._req_count attributes
        to the state file.
        '''

        if self._state_file:
            self._state_file.write_text(
                f'{self._ref_timestamp} {self._req_count}'
            )

    def wait_for_free_flow(self) -> None:
        '''Update the flow state and wait until the flow
        is free.
        Save the current state if the state file is given.
        '''

        if not self._ref_timestamp:
            self._ref_timestamp = time.time()

        self._req_count += 1
        cur_timestamp: float = time.time()

        if (secs := cur_timestamp - self._ref_timestamp) < self._time_range:
            if self._req_count >= self._flow_capacity:
                time.sleep(self._time_range - secs)
                self._req_count = 1
        else:
            self._req_count = 1
            self._ref_timestamp = time.time()

        self._save_state()


class StateRecoveryError(Exception):
    ...
