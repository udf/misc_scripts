import os
from PIL import Image


def get_cmd(
    infile,  # input filname
    outfile,  # output filename
    width,  # new width
    height,  # new height
    layer_name='empty',  # layer name (empty for active layer)
    pres_layer_name='empty',  # preservation layer name (empty for none)
    pres_coeff=1000,  # preservation coefficient (default=1000)
    disc_layer_name='empty',  # discard layer name (empty for none)
    disc_coeff=1000,  # discard coefficient (default=1000)
    rigidity=0,  # overall rigidity coefficient
    rigmask_layer_name='empty',  # rigidity mask layer name (empty for none)
    delta_x=1,  # max displacement along a seam (default=1)
    enlargement_step=150,  # enlargement step percentage (default=150)
    resize_aux_layers=True,  # whether to resize auxiliary layers (0=False [1=True])
    resize_canvas=True,  # whether to resize canvas (0=False [1=True])
    output_target=0,  # output target ([0=Selected layer] 1=New layer)
    output_seams=False,  # whether to output the seam map(s) ([0=False] 1=True)
    gradient_function=3,  # gradient function to use (0=Norm 2=SumAbs [3=xAbs] 5=Null)
    resize_order=0,  # resize order ([0=HorizontalFirst] 1=VerticalFirst)
    mask_behaviour=0,  # what to do when a mask is found ([0=Apply] 1=Discard)
    scale_back=False,  # whether to scale back when done ([0=False] 1=True)
    scaleback_mode=0,  # scale back mode ([0=LqR] 1=Standard 2=StdW 3=StdH)
    ignore_discard_layer=False,  # ignore discard layer upon enlargement (0=False [1=True])
):
    param_names = (
        'infile', 'outfile', 'width', 'height', 'layer_name', 'pres_layer_name', 'pres_coeff',
        'disc_layer_name', 'disc_coeff', 'rigidity', 'rigmask_layer_name', 'delta_x',
        'enlargement_step', 'resize_aux_layers', 'resize_canvas', 'output_target', 'output_seams',
        'gradient_function', 'resize_order', 'mask_behaviour', 'scale_back', 'scaleback_mode',
        'ignore_discard_layer'
    )
    cmd = '(batch-gimp-lqr-full'
    param_vals = locals()
    for param_name in param_names:
        param = param_vals[param_name]
        cmd += ' '
        cmd += {
            str: lambda s: f'"{s}"',
            bool: lambda x: ('FALSE', 'TRUE')[x]
        }.get(type(param), str)(param)

    return cmd + ')'


cmds = ''
src_dir = os.path.expanduser('~/host/LittlecutegirlMomo(Y)(scale)(x2.000000)')
for filename in os.listdir(src_dir):
    im = Image.open(os.path.join(src_dir, filename))
    cmds += get_cmd(filename, f'r{filename}', im.width // 2, im.height // 2)
cmds += '(gimp-quit 0)'

print(cmds)
