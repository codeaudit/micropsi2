"""
Central initialization of fixtures for Runtime etc.
"""
import pytest
from micropsi_core import runtime as micropsi

DELETE_TEST_FILES_ON_EXIT = True


nn_uid = 'Testnet'


@pytest.yield_fixture(scope="function")
def fixed_nodenet(request, test_world, engine):
    """
    A test nodenet filled with some example data (nodenet_data.py)
    Structure:

          ->  A1 ->  A2
        /
       S                     ACTA
        \
          ->  B1 ->  B2

    S: Sensor, brightness_l
    A1: Pipe
    A2: Pipe
    B1: Pipe
    B2: Pipe
    ACTA: Activator, por
    """
    from micropsi_core.tests.nodenet_data import fixed_nodenet_data
    if engine == "theano_engine":
        fixed_nodenet_data = fixed_nodenet_data.replace('Root', 's0001')
    success, uid = micropsi.new_nodenet("Fixednet", engine=engine, worldadapter="Braitenberg", owner="Pytest User", world_uid=test_world, uid='fixed_test_nodenet')
    micropsi.get_nodenet(uid)
    micropsi.merge_nodenet(uid, fixed_nodenet_data, keep_uids=True)
    micropsi.save_nodenet(uid)
    yield uid
    try:
        micropsi.delete_nodenet(uid)
    except:
        pass
