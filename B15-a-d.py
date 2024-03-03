#a
import pandas as pd
from darts import TimeSeries
from darts.models import ExponentialSmoothing
from darts.metrics import mape

# Đọc dữ liệu từ file Day00.csv (giả sử dữ liệu nằm trong cột đầu tiên)
data = pd.read_csv('Day00.csv', header=None, squeeze=True)

# Tạo chuỗi thời gian từ dữ liệu
ts = TimeSeries.from_dataframe(data, 's')

# Mô hình Exponential Smoothing
model = ExponentialSmoothing()
model.fit(ts)

# Dự đoán 2 giờ tiếp theo
forecast = model.predict(n=7200)

# Làm tròn giá trị dự đoán thành số nguyên
rounded_forecast = forecast.pd_series().round().astype(int)

# Lưu dự đoán vào file CSV (Forecasting.csv)
rounded_forecast.to_csv('Forecasting.csv', index=False, header=False)

print("Dự đoán đã được lưu vào Forecasting.csv")
#b
def doc_dinh(filename):
    dinh = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('n'):
                _, id_dinh, _, toa_do = line.strip().split()
                x, y = map(int, toa_do[1:-1].split(','))
                dinh[int(id_dinh)] = (x, y)
    return dinh

def doc_canh(filename):
    canh = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('a'):
                _, dinh_goc, dinh_dich, _, _, _ = line.strip().split()
                canh.append((int(dinh_goc), int(dinh_dich)))
    return canh

def tao_ma_tran_lien_ke(dinh, canh):
    so_dinh = len(dinh)
    ma_tran_lien_ke = [[0] * so_dinh for _ in range(so_dinh)]
    for dinh_goc, dinh_dich in canh:
        ma_tran_lien_ke[dinh_goc - 1][dinh_dich - 1] = 1
    return ma_tran_lien_ke

def luu_ma_tran_lien_ke(ma_tran, filename):
    with open(filename, 'w') as file:
        for hang in ma_tran:
            file.write(' '.join(map(str, hang)) + '\n')

def main():
    file_dinh = 'Vertices.txt'
    file_canh = 'Edges.txt'
    file_lien_ke = 'Adj.txt'

    dinh = doc_dinh(file_dinh)
    canh = doc_canh(file_canh)
    ma_tran_lien_ke = tao_ma_tran_lien_ke(dinh, canh)
    luu_ma_tran_lien_ke(ma_tran_lien_ke, file_lien_ke)

if __name__ == '__main__':
    main()
#c
# Đọc số đỉnh của đồ thị từ file Vertices.txt
N = int(input("Nhập số đỉnh của đồ thị: "))

# Đọc thông tin đỉnh từ file Vertices.txt
originalNodes = []
with open('Vertices.txt', 'r') as file:
    for line in file:
        if line.startswith('n'):
            _, id_dinh, _, toa_do = line.strip().split()
            x, y = map(int, toa_do[1:-1].split(','))
            originalNodes.append([int(id_dinh), x, y, line.strip()])

# Đọc số dòng của file Forecasting.csv
H = int(input("Nhập số dòng của file Forecasting.csv: "))

# Tạo mảng nodes
nodes = [[0] * 4 for _ in range(N * H)]
for i in range(N * H):
    nodes[i][0] = originalNodes[i % N][0]
    nodes[i][1] = i + 1
    nodes[i][2] = 0
    nodes[i][3] = originalNodes[i % N][3] + f' {i % N} {i // N}'

# Lưu nodes vào file TimeSpaceVertices.txt
with open('TimeSpaceVertices.txt', 'w') as file:
    for node in nodes:
        file.write(' '.join(map(str, node)) + '\n')

# Đọc số cạnh từ file Edges.txt
E = int(input("Nhập số cạnh của đồ thị: "))

# Đọc thông tin cạnh từ file Edges.txt
originalEdges = []
with open('Edges.txt', 'r') as file:
    for line in file:
        if line.startswith('a'):
            _, dinh_goc, dinh_dich, _, _, _ = line.strip().split()
            originalEdges.append([int(dinh_goc), int(dinh_dich), line.strip()])

# Tạo mảng edges
edges = [[-1] * 6 for _ in range(H * E)]
F = np.loadtxt('Forecasting.csv', dtype=int)
for i in range(H):
    for j in range(E):
        u = originalEdges[j][0]
        v = (u - 1) + i * E
        edges[j + i * E][0] = j + i * E
        edges[j + i * E][1] = nodes[v][1]
        v = i + F[i][j]
        u = originalEdges[j][1]
        v = (u - 1) + v * E
        if v // N < H:
            edges[j + i * E][2] = nodes[v][1]
            edges[j + i * E][3] = originalEdges[j][3]
            edges[j + i * E][4] = originalEdges[j][4]
            edges[j + i * E][5] = originalEdges[j][5]

# Lưu edges vào file TimeSpaceEdges.txt
with open('TimeSpaceEdges.txt', 'w') as file:
    for edge in edges:
        if edge[2] > -1:
            file.write(' '.join(map(str, edge)) + '\n')
#thử với ví dụ
# Đọc số đỉnh của đồ thị từ file Vertices.txt
N = 3

# Đọc thông tin đỉnh từ file Vertices.txt
originalNodes = [
    [1, 0, 0, '#0,0'],
    [2, 0, 0, '#4,0'],
    [3, 0, 0, '#0,3']
]

# Đọc số dòng của file Forecasting.csv
H = 7

# Tạo mảng nodes
nodes = [[0] * 4 for _ in range(N * H)]
for i in range(N * H):
    nodes[i][0] = originalNodes[i % N][0]
    nodes[i][1] = i + 1
    nodes[i][2] = 0
    nodes[i][3] = originalNodes[i % N][3] + f' {i % N} {i // N}'

# Lưu nodes vào file TimeSpaceVertices.txt
with open('TimeSpaceVertices.txt', 'w') as file:
    for node in nodes:
        file.write(' '.join(map(str, node)) + '\n')

# Đọc số cạnh từ file Edges.txt
E = 3

# Đọc thông tin cạnh từ file Edges.txt
originalEdges = [
    [3, 1, 0, 'INF', 3],
    [1, 2, 0, 'INF', 4],
    [2, 3, 0, 'INF', 5]
]

# Tạo mảng edges
edges = [[-1] * 6 for _ in range(H * E)]
F = np.loadtxt('Forecasting.csv', dtype=int)
for i in range(H):
    for j in range(E):
        u = originalEdges[j][0]
        v = (u - 1) + i * E
        edges[j + i * E][0] = j + i * E
        edges[j + i * E][1] = nodes[v][1]
        v = i + F[i][j]
        u = originalEdges[j][1]
        v = (u - 1) + v * E
        if v // N < H:
            edges[j + i * E][2] = nodes[v][1]
            edges[j + i * E][3] = originalEdges[j][3]
            edges[j + i * E][4] = originalEdges[j][4]
            edges[j + i * E][5] = originalEdges[j][5]

# Lưu edges vào file TimeSpaceEdges.txt
with open('TimeSpaceEdges.txt', 'w') as file:
    for edge in edges:
        if edge[2] > -1:
            file.write(' '.join(map(str, edge)) + '\n')
#d
# Đọc thông tin từ file Graph.txt
with open('Graph.txt', 'r') as file:
    lines = file.readlines()

# Tách thông tin đỉnh và cạnh
vertices_lines = []
edges_lines = []
for line in lines:
    if line.startswith('n'):
        vertices_lines.append(line.strip())
    elif line.startswith('a'):
        edges_lines.append(line.strip())

# Lưu thông tin đỉnh vào file TimeSpace.txt
with open('TimeSpace.txt', 'w') as file:
    for vertex_line in vertices_lines:
        file.write(vertex_line + '\n')

# Lưu thông tin cạnh vào file TimeSpace.txt
with open('TimeSpace.txt', 'a') as file:
    for edge_line in edges_lines:
        file.write(edge_line + '\n')

print("Dữ liệu đã được lưu vào file TimeSpace.txt")
