name = [f'Дискретный вход {i}' for i in range(1, 17)]

channels_dict = [*range(17)]

params = dict(zip(name, channels_dict))
print(params)