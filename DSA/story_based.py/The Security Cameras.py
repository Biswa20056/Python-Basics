def security_camera(cameras):
    n = len(cameras)
    for i in range(n-1):
        if cameras[i] > cameras[i+1]:
            return False
    return True

Cameras = [10, 15, 15, 20, 25]
print(security_camera(Cameras))