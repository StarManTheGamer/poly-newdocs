---
icon: polytoria/BodyPosition
---

# BodyPosition

:polytoria-BodyPosition: BodyPosition are objects that apply a force to their parent until it moves toward the target position.

{{ inherits("Instance") }}

## Properties
### AcceptableDistance:int { property }
Determines how close the body has to be to the target position to stop applying forces to it.

### Force:int { property }
Determines how much force the body applies.

### TargetPosition:Vector3 { property }
Determines the target position that the body applies forces to get to.