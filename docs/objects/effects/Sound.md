---
icon: polytoria/Sound
weight: 2

---

# Sound

Sounds are objects that can be placed in the world and that emit audio.

{{ inherits("DynamicInstance") }}

## Properties

### Autoplay:bool { property }
Determines whether the sound should start playing automatically.

### Length:int { property }
Returns the length of the currently loaded audio

### Loop:bool { property }
Determines whether the sound should loop or not.

### Pitch:int { property }
The pitch property of this sound

### PlayInWorld:bool { property }
When enabled, the sound will be played in 3D world space rather than having the same volume for everyone.

### Playing:bool { property }
Determines whether the sound is currently playing or not.

### Size:Vector3 { property }
Property description (what?? change this later)

### SoundID:int { property }
The asset ID of the sound.

### Time:int { property }
The time position the track is currently on.

### Volume:int { property }
The volume of the sound.