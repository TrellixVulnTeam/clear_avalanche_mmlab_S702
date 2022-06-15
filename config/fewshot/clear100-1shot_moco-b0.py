_base_ = [
    '../_base_/clear100.py',
    '../_base_/naive.py'
]

name = 'clear100-1shot_moco-b0'

shot = 1
scenario = dict(
    feature_type='moco_b0',
    evaluation_protocol='iid',
    seed=0,
    shot=shot)

model = dict(
    head=dict(
        type='LinearClsHead',
        num_classes=100,
        in_channels=2048))

work_dir = f'./work_dirs/{name}'
loggers = [
    dict(type='TextLogger', file=f'{work_dir}/log.txt'),
    dict(type='InteractiveLogger'),
    dict(type='WandBLogger', project_name='clear100', run_name=name,
         params=dict(entity='clear_avalanche_mmlab'))
]
