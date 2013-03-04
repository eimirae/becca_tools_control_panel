
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

border = 0.01

def figure():
    #bg_filename = os.path.join('images', 'brown_rectangle.png')
    #bg_filename = os.path.join('images', 'black_rectangle.png')
    #bg_filename = os.path.join('becca_utils_control_panel', 'images', 'brown_rectangle.png')
    bg_filename = os.path.join('becca_utils_control_panel', 'images', 'black_rectangle.png')
    fig = plt.figure(num=1, figsize=(16., 9.))
    rect = (0., 0., 1., 1.)
    bg_ax = fig.add_axes(rect, frame_on=False, label='background')
    bg_ax.get_xaxis().set_visible(False)
    bg_ax.get_yaxis().set_visible(False)
    bg_image = plt.imread(bg_filename)
    plt.imshow(bg_image, aspect='auto')
    return fig

    
def subfigure(fig, left=0.1, bottom=0.1, width=0.8, height=0.8):
    
    #sub_filename = os.path.join('images', 'tan_rectangle_round.png')
    #sub_filename = os.path.join('images', 'grey_rectangle.png')
    #sub_filename = os.path.join('becca_utils_control_panel', 'images', 'tan_rectangle_round.png')
    sub_filename = os.path.join('becca_utils_control_panel', 'images', 'grey_rectangle.png')
    rect = (left + border, bottom + border, width - 2 * border, height- 2 * border)
    ax = fig.add_axes(rect, frame_on=False, label='background')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    sub_image = plt.imread(sub_filename)
    plt.imshow(sub_image, aspect='auto')

    rect = (left + 5 * border, bottom + 5 * border, width - 9 * border, height- 9 * border)
    data_ax = fig.add_axes(rect, frame_on=False, label='data')
    data_ax.tick_params( length=4, width=1, colors=(0.2, 0.2, 0.2), labelsize=7, pad=2, top='off', right='off')
    
    #for label in data_ax.get_xticklabels() :
    #    label.set_fontproperties(mpl.font_manager.FontProperties(family='sans-serif'))
    
    return data_ax
    
    
if __name__ == '__main__':
    fig = figure()
    ax = subfigure(fig, left=0., bottom=0., height=1., width=1.)
    plt.show()
    