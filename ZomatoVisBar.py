import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '/Users/JasonWeisenfeld/206FINAL/alldata1.db')
with sqlite3.connect(db_path) as db:
    cur = db.cursor()
    cur.execute("Select * from ZomatoData")
    rows = cur.fetchall()
    Dal_rate = {4.4: 0, 4.5: 0, 4.6: 0, 4.7: 0, 4.8: 0, 4.9: 0}
    LA_rate = {4.4: 0, 4.5: 0, 4.6: 0, 4.7: 0, 4.8: 0, 4.9: 0}
    NYC_rate = {4.4: 0, 4.5: 0, 4.6: 0, 4.7: 0, 4.8: 0, 4.9: 0}
    Mia_rate = {4.4: 0, 4.5: 0, 4.6: 0, 4.7: 0, 4.8: 0, 4.9: 0}
    for row in rows[0:25]:
        if row[2] not in Dal_rate:
            Dal_rate[row[2]] = 1
        else:
            Dal_rate[row[2]] += 1
    dal_lst = []
    dal_lst = sorted(Dal_rate.items(), key = lambda x: x[0])
    dal_lst1 = []
    for tup in dal_lst:
        dal_lst1.append(tup[1])

    for row in rows[25:50]:
        if row[2] not in LA_rate:
            LA_rate[row[2]] = 1
        else:
            LA_rate[row[2]] += 1  
    LA_lst = []
    LA_lst = sorted(LA_rate.items(), key = lambda x: x[0])
    LA_lst1 = []
    for tup in LA_lst:
        LA_lst1.append(tup[1])

    for row in rows[50:75]:
        if row[2] not in NYC_rate:
            NYC_rate[row[2]] = 1
        else:
            NYC_rate[row[2]] += 1
    NYC_lst = []
    NYC_lst = sorted(NYC_rate.items(), key = lambda x: x[0])
    NYC_lst1 = []
    for tup in NYC_lst:
        NYC_lst1.append(tup[1])

    for row in rows[75:100]:
        if row[2] not in Mia_rate:
            Mia_rate[row[2]] = 1
        else:
            Mia_rate[row[2]] += 1
    Mia_lst = []
    Mia_lst = sorted(Mia_rate.items(), key = lambda x: x[0])
    Mia_lst1 = []
    for tup in Mia_lst:
        Mia_lst1.append(tup[1])




category_names = ['4.4', '4.5',
                  '4.6', '4.7', '4.8', '4.9']


results = {
    'Dallas': dal_lst1,
    'Los Angeles': LA_lst1,
    'New York City': NYC_lst1,
    'Miami': Mia_lst1
}


def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 6))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


survey(results, category_names)
plt.suptitle("Discrete Distribution Horizontal Bar Chart\n" + "of Ratings of 25 Highest Ranked Restaurants Per City")
plt.show()