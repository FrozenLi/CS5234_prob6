import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects, ax, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


def draw_stats(result1, result2, benchmark, labels):
    ind = np.multiply(np.arange(len(result1)), 2)  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width, result1, width,
                    color='SkyBlue', label='Algo 1', align='center')
    rects2 = ax.bar(ind, result2, width,
                    color='IndianRed', label='Algo 2', align='center')
    rects3 = ax.bar(ind + width, benchmark, width,
                    color='g', label='Actual Result', align='center')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number')
    ax.set_title('Algorithm Query Result')
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    ax.legend()
    autolabel(rects1, ax, "left")
    autolabel(rects2, ax, "center")
    autolabel(rects3, ax, "right")
    plt.show()


def draw_diff(result1, result2, labels):
    ind = np.multiply(np.arange(len(result1)), 1)  # the x locations for the groups
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, result1, width,
                    color='SkyBlue', label='Algo 1', align='center')
    rects2 = ax.bar(ind + width / 2, result2, width,
                    color='IndianRed', label='Algo 2', align='center')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number')
    ax.set_title('Algorithm Query Result')
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    ax.legend()
    autolabel(rects1, ax, "left")
    autolabel(rects2, ax, "right")
    plt.show()
