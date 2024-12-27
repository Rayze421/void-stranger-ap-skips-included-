from dataclasses import dataclass

from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions

class Locustsanity(Toggle):
    """
    When enabled, Locust Idols are shuffled into the item pool and their chests award checks. Each chest capable of
    tripling its contents adds an item worth 3 locusts to the pool. Using an atoner no longer sets your count to 0 but instead to
    the number received.
    """
    display_name = "Locustsanity"

class Brandsanity(Toggle):
    """
    When enabled, the ability to carve each lord's brand into rooms are shuffled into the item pool and
    the inspecting the murals depicting them awards a check.
    """
    display_name = "Brandsanity"

class Idolsanity(Toggle):
    """
    When enabled, the Lover, Smiler, and Killer Idols are eggs until their respective items are received, and
    once restored, talking to them with the void memory awards a check.
    """
    display_name = "Idolsanity"

class Shortcutsanity(Toggle):
    """
    When enabled, the ability to use each of Mon's shortcuts are shuffled into the item pool. The locust requirements
    for Mon to appear are removed, and talking to them awards a check.

    Note: enabling this will count these shortcuts in logic with regards to skipping past any applicable locked Mural 
    rooms (assuming Brandsanity is also enabled).
    """
    display_name = "Shortcutsanity"

class B053skips(Toggle):
    """
    When enabled, generation expects you to know how to abuse both B053 and B157 (and any other Brand input room that can have several 
    solutions) to skip large chunks of floors to get around missing "Sign" items. (Only applicable when Brandsanity is also enabled).
    """
    display_name = "Brand_Skips"

class Beeskips(Toggle):
    """
    When enabled, generation expects you to use Smiler (Bee) statues to skip past locked mural rooms (Only applicable with Brandsanity 
    enabled, and if Idolsanity is enabled requires "Idol of Gluttony" to be recieved).

    Note: this has potential to make logic quite cryptic with other skips in logic. Enable with caution.
    """
    display_name = "Statue_Skips"

class UIskips(Toggle):
    """
    When enabled, generation expects you to know how to abuse your locust count (be that with your hp, existing locusts, and floor values) 
    to skip past otherwise locked mural rooms when "Learn to Cheat" item is recieved. 

    Note: enabling this can tend to make logic even more cryptic, and is largely only advised to use for those already very familiar with 
    abusing the UI to skip around the Void.
    """
    display_name = "Cheat_Skips"

@dataclass
class VoidStrangerOptions(PerGameCommonOptions):
    locustsanity: Locustsanity
    brandsanity: Brandsanity
    idolsanity: Idolsanity
    shortcutsanity: Shortcutsanity
    uiskips: UIskips
    beeskips: Beeskips
    b053skips: B053skips