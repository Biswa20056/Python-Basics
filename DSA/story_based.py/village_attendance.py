def attendance(attendance):
    max_attendance = 0
    curr_attendance = 0
    for val in attendance:
        if val==1:
            curr_attendance+=1
            if curr_attendance > max_attendance:
                max_attendance = curr_attendance
        else:
            curr_attendance = 0
    return max_attendance

att = [1, 1, 1, 0, 1, 0, 1, 1]
print(attendance(att))