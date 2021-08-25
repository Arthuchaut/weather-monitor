import pathlib
import time
import pytest
from weather.libs.api.request_flow_controller import (
    RequestFlowController,
    StateRecoveryError,
)


class TestRequestFlowController:
    def test_init(self, tmp_path: pathlib.Path) -> None:
        state_file: pathlib.Path = tmp_path / '.owm_flow_state'
        req_flow: RequestFlowController = RequestFlowController(
            state_file=state_file,
            flow_capacity=600,
            time_range=60,
        )
        assert req_flow._state_file == state_file
        assert req_flow._flow_capacity == 600
        assert req_flow._time_range == 60
        assert hasattr(req_flow, '_ref_timestamp')
        assert hasattr(req_flow, '_req_count')

    @pytest.mark.parametrize(
        'should_raise, state_data',
        [
            (False, '1629923065.9253566 10'),
            (True, 'hello 1629923065.9253566'),
            (True, '1629923065.9253566'),
            (False, ''),
        ],
    )
    def test__recover_state(
        self, should_raise: bool, state_data: str, tmp_path: pathlib.Path
    ) -> None:
        state_file: pathlib.Path = tmp_path / '.owm_flow_state'
        state_file.write_text(state_data)
        req_flow: RequestFlowController = RequestFlowController(
            flow_capacity=600,
            time_range=60,
        )

        assert req_flow._ref_timestamp == None
        assert req_flow._req_count == 0

        req_flow._state_file = state_file

        if should_raise:
            with pytest.raises(StateRecoveryError):
                req_flow._recover_state()

            assert req_flow._ref_timestamp == None
            assert req_flow._req_count == 0
        else:
            req_flow._recover_state()

            if state_data:
                assert req_flow._ref_timestamp == 1629923065.9253566
                assert req_flow._req_count == 10

    def test__save_state(self, tmp_path: pathlib.Path) -> None:
        state_file: pathlib.Path = tmp_path / '.owm_flow_state'
        req_flow: RequestFlowController = RequestFlowController(
            state_file=state_file,
            flow_capacity=600,
            time_range=60,
        )
        req_flow._ref_timestamp = 1629923065.9253566
        req_flow._req_count = 10
        req_flow._save_state()

        assert state_file.read_text() == '1629923065.9253566 10'

    def test_wait_for_free_flow(self, tmp_path: pathlib.Path) -> None:
        state_file: pathlib.Path = tmp_path / '.owm_flow_state'
        req_flow: RequestFlowController = RequestFlowController(
            state_file=state_file,
            flow_capacity=2,
            time_range=1,
        )
        req_flow._ref_timestamp = time.time()
        begin_time: float = time.time()

        for _ in range(4):
            req_flow.wait_for_free_flow()
            time.sleep(0.1)

        assert int(time.time() - begin_time) == 2
