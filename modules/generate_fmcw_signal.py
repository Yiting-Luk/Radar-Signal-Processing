# 生成 FMCW 信号
import numpy as np
def generate_fmcw_signal(radar_config):
    """
    根据雷达配置生成 FMCW 信号。

    参数：
    radar_config: 包含雷达配置的字典

    返回：
    signal: 仿真的 FMCW 信号矩阵
    """
    num_samples = int(radar_config["fs"] * radar_config["t_chirp"])
    t = np.linspace(0, radar_config["t_chirp"], num_samples)
    chirp = np.exp(1j * 2 * np.pi * (radar_config["fc"] * t + (radar_config["bw"] / radar_config["t_chirp"]) * (t**2) / 2))
    return chirp