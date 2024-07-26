from queue import PriorityQueue
# Tạo PriorityQueue và thêm sinh viên
pq = PriorityQueue()
for sv in sinh_viens:
    pq.put(sv)

# Lấy sinh viên theo thứ tự tuổi tăng dần
while not pq.empty():
    sv = pq.get()
    print(f"Tên: {sv.ten}, Tuổi: {sv.tuoi}")
    
    
class SinhVien:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def __lt__(self, other):
        return self.tuoi < other.tuoi

# Tạo danh sách sinh viên
sinh_viens = [
    SinhVien("An", 20),
    SinhVien("Bình", 18),
    SinhVien("Cường", 22),
]


