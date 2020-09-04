# 依据节点度，生成网络拓扑，保存为txt
# 包含链路延迟，链路带宽
# 拓扑生成原理：
# 1.生成节点数量
# 2.每个节点从其他节点随机选取节点
import random
import copy


node_amount     = 15      # 节点数量
node_degree     = [5,10]  # 节点度

total_node_list = []  # 所有节点列表
for i in range(0, node_amount):
    total_node_list.append(i)
links = {}
for i in total_node_list:
    links[i] = []


while True:

    for i in total_node_list:
        zxcv = copy.deepcopy(total_node_list)
        zxcv.remove(i)
        for j in links[i]:
            zxcv.remove(j)
        choose = random.sample(zxcv, 1)
        choose = choose[0]
        links[i].append(choose)
        links[choose].append(i)
    for k in links:
        links[k].sort()
        print('nums:', len(links[k]), ',   ', k, ':', links[k])
    print('###########################################################################')
for i in links:
    print('%d:'%i, links[i])

