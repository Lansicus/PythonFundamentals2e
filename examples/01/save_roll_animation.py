# save_roll_animation.py
import importlib.util
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")   # non-GUI backend for saving files
from matplotlib.animation import PillowWriter

MODULE_PATH = Path(__file__).parent / "RollDieDynamic.py"
if not MODULE_PATH.exists():
    raise FileNotFoundError(f"{MODULE_PATH} not found")

# Load RollDieDynamic.py as a module named rollmod
spec = importlib.util.spec_from_file_location("rollmod", str(MODULE_PATH))
rollmod = importlib.util.module_from_spec(spec)
sys.modules["rollmod"] = rollmod
spec.loader.exec_module(rollmod)

# Candidate function names that commonly return an Animation object
candidates = [
    "create_animation",
    "make_animation",
    "build_animation",
    "roll_die_animation",
    "roll_animation",
    "main",
]

anim = None

# Try calling candidate functions with (600, 1)
for name in candidates:
    fn = getattr(rollmod, name, None)
    if callable(fn):
        try:
            result = fn(600, 1)
            # If the function returns an Animation, use it
            if hasattr(result, "save") and hasattr(result, "event_source"):
                anim = result
                print(f"Used function: {name}() -> Animation")
                break
            # Some functions may return (fig, anim) or set a global variable
            if isinstance(result, tuple):
                for item in result:
                    if hasattr(item, "save") and hasattr(item, "event_source"):
                        anim = item
                        print(f"Used function: {name}() returned tuple with Animation")
                        break
                if anim:
                    break
        except TypeError:
            # function signature didn't accept (600,1); try calling without args
            try:
                result = fn()
                if hasattr(result, "save") and hasattr(result, "event_source"):
                    anim = result
                    print(f"Used function: {name}() -> Animation (no args)")
                    break
            except Exception:
                pass
        except Exception as e:
            # ignore other exceptions for now
            print(f"Calling {name} raised {e!r}; continuing")

# If still not found, check module globals for an Animation object
if anim is None:
    for k, v in vars(rollmod).items():
        if hasattr(v, "save") and hasattr(v, "event_source"):
            anim = v
            print(f"Found Animation object in module global: {k}")
            break

if anim is None:
    raise RuntimeError(
        "Could not find an Animation object. "
        "Open RollDieDynamic.py and check which function returns the animation."
    )

# Save as GIF using PillowWriter
out_file = Path("roll_animation.gif")
writer = PillowWriter(fps=10)   # adjust fps if you want
anim.save(str(out_file), writer=writer)
print(f"Saved animation to {out_file.resolve()}")
