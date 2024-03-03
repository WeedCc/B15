#e
# Đọc thông tin từ file TimeSpace.txt
with open('TimeSpace.txt', 'r') as file:
    lines = file.readlines()

# Tách thông tin đỉnh và cạnh
vertices_lines = []
edges_lines = []
for line in lines:
    if line.startswith('n'):
        vertices_lines.append(line.strip())
    elif line.startswith('a'):
        edges_lines.append(line.strip())

# Tạo ma trận liền kề mới
num_vertices = len(vertices_lines)
new_adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

# Điền giá trị vào ma trận liền kề mới dựa trên thông tin cạnh
for edge_line in edges_lines:
    _, dinh_goc, dinh_dich, _, _, _ = edge_line.split()
    new_adj_matrix[int(dinh_goc) - 1][int(dinh_dich) - 1] = 1

# Lưu ma trận liền kề mới vào file TimeSpaceAdj.txt
with open('TimeSpaceAdj.txt', 'w') as file:
    for row in new_adj_matrix:
        file.write(' '.join(map(str, row)) + '\n')

print("Ma trận liền kề mới đã được lưu vào TimeSpaceAdj.txt")
