---
icon: polytoria/Camera
weight: 8
---

# Camera

{{ service() }}

{{ clientexclusive() }}

{{ notnewable() }}

:polytoria-Camera: Camera is the local player's camera.

{{ inherits("Instance") }}

## Properties

### Distance:int { property }

The distance between the camera and the player when the camera is in FollowPlayer mode.

### FOV:int { property }

Sets or return the camera's field of view.

### FastFlySpeed:int { property }

The camera speed when the camera is in FreeCam mode while holding shift.

### FastFlySpeed:int { property }

The camera speed when the camera is in FreeCam mode.

### FollowLerp:bool { property }

Determines whether or not to use lerping in FollowPlayer mode.

### FreeLookSensitivity:int { property }

The mouse sensitivity while in FreeCam mode.

### HorizontalSpeed:int { property }

The horizontal movement speed of the camera in FollowPlayer mode.

### IsFirstPerson:bool { property }

Returns whether or not the camera is in first person.

{{ readonly() }}

### LerpSpeed:int { property }

The lerp speed of the camera when lerping is enabled.

### MaxDistance:int { property }

The camera's maximum distance from the player in FollowPlayer mode.

### MinDistance:int { property }

The camera's minimum distance from the player in FollowPlayer mode.

### Mode:CameraMode { property }

Sets or returns the camera's current mode.

### Orthographic:bool { property }

Determines whether or not the camera should render in orthographic (2D) mode or not (3D).

### OrthographicSize:int { property }

Determines the half-size of the camera when in orthographic mode.

### ScrollSensitivity:int { property }

Determines the scroll move speed of the camera.

### VerticalSpeed:int { property }

Determines the vertical move speed of the camera.
