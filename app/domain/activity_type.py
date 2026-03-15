from enum import Enum


class ActivityType(str, Enum):
    RUN = "run"
    WALK = "walk"
    HIKE = "hike"
    TRAIL_RUN = "trail_run"

    RIDE = "ride"
    MOUNTAIN_BIKE_RIDE = "mountain_bike_ride"
    GRAVEL_RIDE = "gravel_ride"
    E_BIKE_RIDE = "e_bike_ride"
    HANDCYCLE = "handcycle"
    VELOMOBILE = "velomobile"

    SWIM = "swim"

    ALPINE_SKI = "alpine_ski"
    BACKCOUNTRY_SKI = "backcountry_ski"
    NORDIC_SKI = "nordic_ski"
    SNOWBOARD = "snowboard"
    SNOWSHOE = "snowshoe"
    ICE_SKATE = "ice_skate"

    ROWING = "rowing"
    KAYAKING = "kayaking"
    CANOEING = "canoeing"
    KITESURF = "kitesurf"
    SURFING = "surfing"
    SAIL = "sail"
    STAND_UP_PADDLING = "stand_up_paddling"
    WINDSURF = "windsurf"

    ROCK_CLIMBING = "rock_climbing"

    INLINE_SKATE = "inline_skate"
    SKATEBOARD = "skateboard"

    WORKOUT = "workout"
    WEIGHT_TRAINING = "weight_training"
    YOGA = "yoga"
    CROSSFIT = "crossfit"

    VIRTUAL_RIDE = "virtual_ride"
    VIRTUAL_RUN = "virtual_run"