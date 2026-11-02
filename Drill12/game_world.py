# world = [] # 1차원 리스트

world = [ [], [], [] ]

# 게임월드에 객체 추가, layer를 지정해야 한다.
def add_object(o, depth=0): # 기본 depth = 0, 즉 0번 레이어에 추가
    world[depth].append(o)

# 게임 월드에서 객체 제거
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return  # 더 이상 반복할 필요가 없으므로 return으로 함수 종료

# game logic
def update_world():
    for layer in world:
        for o in layer[:]:  # 복사본을 만들어서 반복해야 remove_object()로 인한 오류가 발생하지 않는다.
            o.update()
    for layer in world:
        for o in layer[:]:
            if hasattr(o, 'is_out_of_bounds') and o.is_out_of_bounds():
                remove_object(o)

# game rendering
def render_world():
    for layer in world:
        for o in layer[:]:
            o.draw()