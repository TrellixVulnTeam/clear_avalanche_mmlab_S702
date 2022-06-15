_base_ = [
    '../_base_/clear10.py',
    '../_base_/lwf.py'
]

name = 'clear10-5shot_moco-b0_cosine_lwf'

shot = 5
scenario = dict(
    feature_type='moco_b0',
    evaluation_protocol='iid',
    seed=0,
    shot=shot)

model = dict(
    head=dict(
        type='CosineDistanceHead',
        num_classes=11,
        in_channels=2048))

work_dir = f'./work_dirs/{name}'
loggers = [
    dict(type='TextLogger', file=f'{work_dir}/log.txt'),
    dict(type='InteractiveLogger'),
    dict(type='WandBLogger', project_name='clear10', run_name=name,
         params=dict(entity='clear_avalanche_mmlab'))
]
