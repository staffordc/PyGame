from nose.tools import *
from planisphere import *


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)


def test_death_jump_corridor():
    start_room = load_room(START)
    assert_equal(start_room.go('jump'), death_jump_corridor)


def test_death_run_corridor():
    start_room = load_room(START)
    assert_equal(start_room.go('run'), death_run_corridor)


def test_space_start_room3():
    start_room = load_room(START)
    room = start_room.go('boot knife')
    assert_equal(room, laser_weapon_armory)


def test_space_armory_room():
    sec_room = load_room("laser_weapon_armory")
    room = sec_room.go('012')
    assert_equal(room, the_bridge)


def test_space_armory_room_glob():
    sec_room = load_room("laser_weapon_armory")
    room = sec_room.go('*')
    assert_equal(room, death_wrong_code_armory)


def test_the_bridge():
    thi_room = load_room("the_bridge")
    room = thi_room.go('look down')
    assert_equal(room, death_look_down_bridge)


def test_the_bridge1():
    fou_room = load_room("the_bridge")
    room = fou_room.go('look up')
    assert_equal(room, escape_pod)


def test_escape_pod():
    fif_room = load_room("escape_pod")
    room = fif_room.go('control stick')
    assert_equal(room, the_end_winner)


def test_escape_pod1():
    fif_room = load_room("escape_pod")
    room = fif_room.go('emergency button')
    assert_equal(room, the_end_loser)
