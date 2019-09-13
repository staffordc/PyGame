class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
                        """
        You find yourself waking up on the catwalk
        above the reactor core of the ship. Its light
        is fading fast. You can't remember anything
        after getting your crew to safety, after the
        beasts attacked.The hull has been breached, 
        and you're running out of oxygen.

        You need to destroy the ship, you can't let
        them survive and get to the homeworld. Where
        is the neutron destruct bomb again? The Weapons
        Armory! You feel some of the tendrils of those...
        things just outside of your peripherey vision.
        You swear they feed on fear...
        """)

laser_weapon_armory = Room("Laser Weapon Armory",
                           """
        There is the armory. You know
        that it is locked with a 3 digit
        code. It's reset often. 3 numbers 1-9.
        You're going to have to guess to get out
        """)

the_bridge = Room("TheBridge",
                  """
        You look around the hall to the bridge.
        You want to maintain a slow heart beat.
        You move about your ship breathing slowly.
        As you blink your foot slips on the floor.
        Quickly you pull the bomb close to you and
        look around to see if you were discovered.
        Woo! Watch out!
        """)

escape_pod = Room("Escape Pod",
                  """
        Your instincts are telling you that you
        forgot something important. You can't remeber
        what though... what was it? Something about
        a control stick or an emergency button...?
        """
                  )

the_end_winner = Room("The End Win",
                      """
        You see that the control is not in it's proper starting position.
        You right it as you start your ship and turn everything on.
        The emergency button flashes, and you remember that after
        2 years outside of port your emergency button always did that.
        """
                      )

the_end_loser = Room("The End Lose",
                     """
        You see the button flashing, and try to determine what is
        making it go off. As you think of the seconds you have left
        your heart rate and respiration skyrockets. The creatures all
        are standing outside of the pod. At least you know they'll be fried
        along with you.
        """)

escape_pod.add_paths({
    'control stick': the_end_winner,
    'emergency button': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'look down': generic_death,
    'look up': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})
central_corridor.add_paths({
    'jump': generic_death,
    'run': generic_death,
    'boot knife': laser_weapon_armory
})
START = 'central_corridor'


def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable
    """

    return globals().get(name)


def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution tham thes globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key
