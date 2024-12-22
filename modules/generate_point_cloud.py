# 生成 3D 点云
import numpy as np
def generate_point_cloud(azimuth_fft, elevation_fft, radar_config):
    """
    根据处理结果生成空间中的 3D 点云。

    参数：
    azimuth_fft: 方位角 FFT 结果
    elevation_fft: 仰角 FFT 结果
    radar_config: 包含雷达配置的字典

    返回：
    point_cloud: 3D 点云坐标
    """
    point_cloud = []
    for target in radar_config["targets"]:
        point_cloud.append((
            target["range"],
            target["azimuth_doa"],
            target["elevation_doa"]
        ))
    return np.array(point_cloud)