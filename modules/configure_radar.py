# 雷达参数配置
def configure_radar():
    """
    配置雷达参数，包括发射和接收阵列、信号参数和目标属性。

    返回：
    radar_config: 包含雷达配置的字典
    """
    radar_config = {
        "fs": 1e6,  # 采样频率 (Hz)
        "fc": 77e9,  # 雷达载频 (Hz)
        "bw": 4e9,  # 调频带宽 (Hz)
        "t_chirp": 1e-6,  # Chirp 持续时间 (s)
        "tx_array": 4,  # 发射阵列天线数量
        "rx_array": 4,  # 接收阵列天线数量
        "azimuth_dim": 8,  # Azimuth 维度
        "elevation_dim": 2,  # Elevation 维度
        "targets": [
            {"range": 50, "velocity": 20, "rcs": 10, "azimuth_doa": 30, "elevation_doa": 10},
            {"range": 70, "velocity": -10, "rcs": 15, "azimuth_doa": -20, "elevation_doa": 5},
        ],
    }
    return radar_config