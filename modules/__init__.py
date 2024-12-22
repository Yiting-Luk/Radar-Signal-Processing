# modules/__init__.py

# 导入模块中所有的主要函数
from .configure_radar import configure_radar
from .generate_fmcw_signal import generate_fmcw_signal
from .simulate_reflection import simulate_target_reflection
from .range_processing import range_processing
from .velocity_processing import velocity_processing
from .angle_processing import angle_processing
from .generate_point_cloud import generate_point_cloud

# 可选：定义 __all__，明确模块中允许导入的内容
__all__ = [
    "configure_radar",
    "generate_fmcw_signal",
    "simulate_target_reflection",
    "range_processing",
    "velocity_processing",
    "angle_processing",
    "generate_point_cloud",
]
