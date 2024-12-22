import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 主程序 - 调用分模块的雷达信号处理
# ===============================
from modules import configure_radar, generate_fmcw_signal, simulate_target_reflection, range_processing, velocity_processing, angle_processing, generate_point_cloud

if __name__ == "__main__":
    # 配置雷达参数
    radar_config = configure_radar()

    # 生成 FMCW 信号
    chirp = generate_fmcw_signal(radar_config)

    # 模拟目标反射信号
    received_signal = simulate_target_reflection(radar_config, chirp)

    # 距离处理
    range_profile = range_processing(received_signal, radar_config)

    # 速度处理
    velocity_profile = velocity_processing(range_profile, radar_config)

    # 方位角处理
    azimuth_fft, elevation_fft = angle_processing(velocity_profile, radar_config)

    # 生成 3D 点云
    point_cloud = generate_point_cloud(azimuth_fft, elevation_fft, radar_config)

    print("3D Point Cloud:")
    print(point_cloud)

    # 可视化点云
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2])
    ax.set_xlabel('Range (m)')
    ax.set_ylabel('Azimuth (deg)')
    ax.set_zlabel('Elevation (deg)')
    plt.show()
