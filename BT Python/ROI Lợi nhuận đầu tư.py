def ROI(DT,CT):
    return((DT-CT)/CT)
def Tuvan(roi):
    if roi < 0.75:
        return "Không đầu tư"
    else:
        return "Đầu tư"
print("Nhập Doanh thu của dự án:")
DT=int(input())
CT=int(input("Nhập chi tiêu chủa dự án:"))
roi=ROI(DT,CT)
print("Tỉ lệ đầu tư:",roi)
print("==>",Tuvan(roi))