# 模拟雷达目标反射信号
import numpy as np
def simulate_target_reflection(radar_config, chirp):
    """
    根据目标配置模拟雷达接收到的目标反射信号。

    参数：
    radar_config: 包含雷达配置的字典
    chirp: 发射的 FMCW 信号

    返回：
    reflected_signals: 接收到的反射信号矩阵
    """
    num_samples = len(chirp)
    reflected_signals = np.zeros((radar_config["rx_array"], num_samples), dtype=complex)
    for target in radar_config["targets"]:
        delay = 2 * target["range"] / 3e8  # 往返时间
        doppler_shift = 2 * target["velocity"] * radar_config["fc"] / 3e8  # 多普勒频移
        reflection = target["rcs"] * np.exp(1j * 2 * np.pi * doppler_shift * np.arange(num_samples) / radar_config["fs"])
        delayed_chirp = np.roll(chirp, int(delay * radar_config["fs"]))
        reflected_signals += reflection[:, None] * delayed_chirp
    return reflected_signals
