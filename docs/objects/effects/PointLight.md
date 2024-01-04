---
title: PointLight
description: PointLight is a source of light that can be placed in the world.
icon: polytoria/PointLight
---

# PointLight

PointLight is a source of light that can be placed in the world.

{{ inherits("DynamicInstance") }}

## Properties

### Brightness:int { property }

Specifies how bright/intense the light is.

### Color:Color { property }

Specifies the color of the light.

### Range:int { property }

Specifies how far out the light can reach.

### Shadows:bool { property }

Specifies whether this light emits shadows or not.

!!! note "Shadows"

    Having many lights with shadows enabled will cause a massive hit in performance. Consider minimzing the amount of lights with shadows to ensure every player is enjoying your place with minimal framerate issues.
