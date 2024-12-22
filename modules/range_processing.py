# 距离处理
import numpy as np
def range_processing(received_signal, radar_config):
    """
    对接收信号进行距离处理。

    参数：
    received_signal: 接收到的反射信号
    radar_config: 包含雷达配置的字典

    返回：
    range_profile: 距离维度的FFT结果
    """
    range_profile = np.fft.fft(received_signal, axis=1)
    return range_profile