import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram_kde(data, column, bins=30, kde=True, xlim=None, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.histplot(data[column], bins=bins, kde=kde)

    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    plt.title(f'Histogram and KDE of {column}')
    plt.show()


def plot_box(data, column, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=data[column])

    if ylim:
        plt.ylim(ylim)

    plt.title(f'Box Plot of {column}')
    plt.show()


def plot_count_column(data, column, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.countplot(x=data[column])

    if ylim:
        plt.ylim(ylim)

    plt.title(f'Box Plot of {column}')
    plt.show()


def plot_violin(data, column, hue=None, split=False, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.violinplot(x=data[column], hue=hue, split=split)

    if ylim:
        plt.ylim(ylim)

    plt.title(f'Violin Plot of {column}')
    plt.show()


def plot_scatter(data, x_col, y_col, hue=None, style=None, size=None, xlim=None, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.scatterplot(data=data, x=x_col, y=y_col,
                    hue=hue, style=style, size=size)

    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    plt.title(f'Scatter Plot of {x_col} vs {y_col}')
    plt.show()


def plot_line(data, x_col, y_col, hue=None, style=None, size=None, xlim=None, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=data, x=x_col, y=y_col, hue=hue, style=style, size=size)

    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    plt.title(f'Line Plot of {y_col} over {x_col}')
    plt.show()


def plot_bar(data, x_col, y_col, hue=None, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.barplot(data=data, x=x_col, y=y_col, hue=hue)

    if ylim:
        plt.ylim(ylim)

    plt.title(f'Bar Plot of {y_col} by {x_col}')
    plt.show()


def plot_box_categorical(data, x_col, y_col, hue=None, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=data, x=x_col, y=y_col, hue=hue)

    if ylim:
        plt.ylim(ylim)

    plt.title(f'Box Plot of {y_col} by {x_col}')
    plt.show()


def plot_violin_categorical(data, x_col, y_col, hue=None, split=False, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.violinplot(data=data, x=x_col, y=y_col, hue=hue, split=split)

    if ylim:
        plt.ylim(ylim)

    plt.title(f'Violin Plot of {y_col} by {x_col}')
    plt.show()


def plot_line(data, x_col, y_col, hue=None, style=None, size=None, xlim=None, ylim=None):
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=data, x=x_col, y=y_col, hue=hue, style=style, size=size)

    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    plt.title(f'Line Plot of {y_col} over {x_col}')
    plt.show()


def plot_corr_heatmap(data, annot=True, cmap='coolwarm'):
    plt.figure(figsize=(8, 8))
    sns.heatmap(data.corr(), annot=annot, cmap=cmap)

    plt.title('Correlation Heatmap')
    plt.show()


def plot_joint(data, x_col, y_col, kind="scatter", xlim=None, ylim=None):
    g = sns.jointplot(data=data, x=x_col, y=y_col, kind=kind)

    if xlim:
        g.ax_joint.set_xlim(xlim)
    if ylim:
        g.ax_joint.set_ylim(ylim)

    plt.show()
