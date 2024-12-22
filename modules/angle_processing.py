# 方位角处理
import numpy as np
def angle_processing(velocity_profile, radar_config):
    """
    对速度处理后的信号进行方位角处理。

    参数：
    velocity_profile: 速度维度处理后的信号
    radar_config: 包含雷达配置的字典

    返回：
    angle_profile: 方位角处理结果
    """
    azimuth_fft = np.fft.fft(velocity_profile, axis=0)
    elevation_fft = np.fft.fft(velocity_profile, axis=1)
    return azimuth_fft, elevation_fft