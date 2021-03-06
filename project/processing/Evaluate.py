import glob
import itertools
import os.path
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from processing import Prepare, InteractiveSelectors

DATASETS = ('sr', 'svrt1', 'random_board_placement_diff5',
            'random_board_placement_diff1', 'sd', 'svrt19', 'fixed_pos_diff5',
            'fixed_pos_diff1', 'svrt20', 'svrt21', 'camera_rotation_diff5',
            'camera_rotation_diff1')
GEOMETRY = (703, 54, 512, 512)
PATH = "processing/prepared/{}/{}/"
IMAGE_NAME_REGEX = r'[^\/]+\/\d+_([^\/]+)\.'
IMAGE_NUMBER_REGEX = r'[^\/]+\/(\d+)_[^\/]+\.'
STAT_STRING = "Duration: {} seconds\nSwitches fixations: {}\nFixations: {}\n% NaN: {}\nPredicted: {}\nTrue: {}"

RANGE_PIC = [[0, 512], [0, 512]]
PLOT_SIZE = [512, 512]
BINS = 50
DPI = 100
FIG_SIZE = [51.2, 51.2]
DEFAULT_CALIBRATION = (6.4, 32.0)


def range_from_geo(g):
    return [[g[0], g[0] + g[2]], [g[1], g[1] + g[3]]]


def get_trial(file1: str) -> int:
    return int(re.findall(IMAGE_NUMBER_REGEX, file1)[0])


def get_file_paths(path):
    f = glob.glob(path + '*.pkl')
    f.sort(key=get_trial)
    images = [i for i in f if 'calibration' not in i]
    files = []
    for image in images:
        cali, im_path = None, None
        if os.path.exists(image[:-4] + '_calibration.pkl'):
            cali = image[:-4] + '_calibration.pkl'
        if os.path.exists(image[:-4] + '.jpg'):
            im_path = image[:-4] + '.jpg'
        elif os.path.exists(image[:-4] + '.png'):
            im_path = image[:-4] + '.png'

        files.append([image, cali, im_path])
    return files


def trim_image(listxy):
    xpic, ypic, width, height = GEOMETRY

    coords = [[x - xpic, y - ypic] for x, y in listxy if
              xpic <= x <= xpic + width and ypic <= y <= ypic + height]
    if not coords:
        return None

    c = np.asarray(coords, dtype=np.int)
    return np.asarray([c[:, 0], c[:, 1]])


def trim_fixations(fix: dict):
    tx, ty, tdur = [], [], []
    xpic, ypic, width, height = GEOMETRY

    for x, y, dur in zip(fix['x'], fix['y'], fix['dur']):
        if xpic <= x <= xpic + width and ypic <= y <= ypic + height:
            tx.append(x - xpic)
            ty.append(y - ypic)
            tdur.append(dur)
    return {'x': np.asarray(tx), 'y': np.asarray(ty), 'dur': np.asarray(tdur)}


def trim_saccades(sac: list):
    n = []
    xpic, ypic, width, height = GEOMETRY
    for st, et, dur, sx, sy, ex, ey in sac:
        if (xpic <= sx <= xpic + width and ypic <= sy <= ypic + height
                and xpic <= ex <= xpic + width and ypic <= ey <= ypic + height):
            n.append([st, et, dur, sx - xpic, sy - ypic, ex - xpic, ey - ypic])

    return n


def offset_calibration(image_df: pd.DataFrame, calibration_df: pd.DataFrame):
    xyt = image_df.values
    xy_cali = calibration_df.values

    xybins = 40
    bin_middle = GEOMETRY[2] / xybins / 2
    h, xedges, yedges = np.histogram2d(xy_cali[:, 0], xy_cali[:, 1], bins=xybins, range=RANGE_PIC)
    x_cent, y_cent = np.unravel_index(h.argmax(), h.shape)
    x_offset = xedges[x_cent] + bin_middle - (RANGE_PIC[0][1] // 2)
    y_offset = yedges[y_cent] + bin_middle - (RANGE_PIC[1][1] // 2)

    new = [[x - x_offset, y - y_offset, t] for x, y, t in xyt]
    return np.asarray(new, dtype=np.int)


def offset_calibration_default(image_df: pd.DataFrame):
    xyt = image_df.values
    new = [[x - DEFAULT_CALIBRATION[0], y - DEFAULT_CALIBRATION[1], t] for x, y, t in xyt]
    return np.asarray(new, dtype=np.int)


def draw_plots(trim_fix: dict, stat_string: str, image_path: str, save_path: str, ):
    img = Image.open(image_path)
    img = img.resize(PLOT_SIZE)
    figure = Figure(figsize=(10, 10), dpi=DPI)
    canvas = FigureCanvas(figure)
    axes = figure.subplots(ncols=2, nrows=2)
    axes[0][0].set_title('Original')
    axes[0][0].imshow(img, zorder=1)

    axes[0][1].set_title('Fixation Heatmap')
    axes[0][1].hist2d(trim_fix['x'], trim_fix['y'], weights=trim_fix['dur'], bins=BINS,
                      range=RANGE_PIC, alpha=0.8, zorder=2, cmin=0.0001)
    axes[0][1].invert_yaxis()
    axes[0][1].imshow(img, zorder=1)

    axes[1][0].set_title('Numbered Fixations')
    axes[1][0].imshow(img, zorder=1)
    for i in range(len(trim_fix['x'])):
        axes[1][0].annotate(str(i), (trim_fix['x'][i], trim_fix['y'][i]), zorder=4, alpha=1,
                            horizontalalignment='center', verticalalignment='center',
                            multialignment='center', color='g')

    axes[1][1].set_title('Stats')
    axes[1][1].text(0.01, 0.99, stat_string, horizontalalignment='left',
                    verticalalignment='top', multialignment='left')

    figure.canvas.print_png(save_path)
    figure.clf()


def draw_fixation_heatmap(trim_fix: dict, image_path: str, save_path: str, ):
    img = Image.open(image_path)
    img = img.resize(PLOT_SIZE)
    fig = plt.figure(figsize=[5.12, 5.12], dpi=DPI)
    fig.gca().hist2d(trim_fix['x'], trim_fix['y'], weights=trim_fix['dur'], bins=BINS,
                     range=RANGE_PIC, alpha=0.9, zorder=2, cmin=0.0001)

    plt.margins(0, 0)
    fig.gca().invert_yaxis()
    fig.gca().xaxis.set_major_locator(plt.NullLocator())
    fig.gca().yaxis.set_major_locator(plt.NullLocator())
    fig.gca().set_axis_off()
    plt.imshow(img, zorder=1)
    fig.savefig(save_path, bbox_inches='tight', pad_inches=0)
    fig.clf()


def find_middle_lines(ids=(3, 15), dats=DATASETS):
    image_df = Prepare.load_images_dataframe()
    for i in range(ids[0], ids[1]):
        for d in dats:
            print('id: {}, dat: {}'.format(i, d))
            ici = get_file_paths(PATH.format(i, d))
            for im, cali, im_path in ici:
                image_name = re.findall(IMAGE_NAME_REGEX, im_path)[0]
                impk = pd.read_pickle(im)

                trim = trim_image(impk.dropna().drop('times', axis=1).values)
                if trim is not None:
                    x, y, = trim
                    line_start, line_end = InteractiveSelectors.get_line_coords(x, y, im_path)
                    image_df.at[(i, d, image_name), 'line_start_x'] = line_start[0]
                    image_df.at[(i, d, image_name), 'line_start_y'] = line_start[1]
                    image_df.at[(i, d, image_name), 'line_end_x'] = line_end[0]
                    image_df.at[(i, d, image_name), 'line_end_y'] = line_end[1]

        cont = input("ID " + str(i) + " done, e for exit")
        if cont == "e":
            print("stopped at {}".format(i))
            break

    image_df.to_csv(Prepare.IMAGE_CSV_PATH)


def calculate_switches(ids=(3, 15), dats=DATASETS):
    image_df = Prepare.load_images_dataframe()
    for i in range(ids[0], ids[1]):
        for d in dats:
            print('id: {}, dat: {}'.format(i, d))
            ici = get_file_paths(PATH.format(i, d))
            for im, cali, im_path in ici:
                image_name = re.findall(IMAGE_NAME_REGEX, im_path)[0]
                impk = pd.read_pickle(im)

                trim = trim_image(impk.dropna().drop('times', axis=1).values)
                if trim is not None:
                    xy = np.column_stack(trim)
                    switches = _calculate_switches(d, i, image_df, image_name, xy)
                    image_df.at[(i, d, image_name), 'switches'] = switches

    image_df.to_csv(Prepare.IMAGE_CSV_PATH)


def _calculate_switches(d, i, image_df, image_name, xy):
    line_start = np.array(
        (image_df.at[(i, d, image_name), 'line_start_x'], image_df.at[(i, d, image_name), 'line_start_y']))
    line_end = np.array((image_df.at[(i, d, image_name), 'line_end_x'], image_df.at[(i, d, image_name), 'line_end_y']))
    line_vec = line_end - line_start

    def calculate_cross(x): return np.cross(line_vec, (x - line_start))

    cross_product = calculate_cross(xy)
    # remove 1 because first number is no sign switch
    switches = len(list(itertools.groupby(cross_product, lambda y: y > 0))) - 1
    return switches


def calculate_nan(ids=(3, 15), dats=DATASETS):
    image_df = Prepare.load_images_dataframe()
    for i in range(ids[0], ids[1]):
        for d in dats:
            print('id: {}, dat: {}'.format(i, d))
            ici = get_file_paths(PATH.format(i, d))
            for im, cali, im_path in ici:
                image_name = re.findall(IMAGE_NAME_REGEX, im_path)[0]
                impk = pd.read_pickle(im)
                if len(impk) == 0:
                    nan = 100
                else:
                    nan = round(100 - (impk['x'].count() / len(impk) * 100), 2)
                image_df.at[(i, d, image_name), 'p_nan'] = nan
                image_df.at[(i, d, image_name), 'len'] = len(impk)

    image_df.to_csv(Prepare.IMAGE_CSV_PATH)


if __name__ == '__main__':
    pass
