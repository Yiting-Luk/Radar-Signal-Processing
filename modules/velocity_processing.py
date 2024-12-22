# 速度处理
import numpy as np
def velocity_processing(range_profile, radar_config):
    """
    对距离处理后的信号进行速度处理。

    参数：
    range_profile: 距离维度处理后的信号
    radar_config: 包含雷达配置的字典

    返回：
    velocity_profile: 速度维度的FFT结果
    """
    velocity_profile = np.fft.fft(range_profile, axis=0)
    return velocity_profile