from pressure import excel 
import numpy as np
import matplotlib.pyplot as plt
import pygal

##################### TWO DIMENSIONAL PLOT ##############################
# x = excel.df.Upper
# y = excel.df.Down

# def scatter_hist(x, y, ax, ax_histx, ax_histy):
#     # no labels
#     ax_histx.tick_params(axis="x", labelbottom=False)
#     ax_histy.tick_params(axis="y", labelleft=False)

#     # the scatter plot:
#     ax.scatter(x, y)

#     # now determine nice limits by hand:
#     binwidth = 0.25
#     xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
#     lim = (int(xymax/binwidth) + 1) * binwidth

#     bins = np.arange(-lim, lim + binwidth, binwidth)
#     ax_histx.hist(x, bins=bins)
#     ax_histy.hist(y, bins=bins, orientation='horizontal')

# # definitions for the axes
# left, width = 0.1, 0.65
# bottom, height = 0.1, 0.65
# spacing = 0.005

# rect_scatter = [left, bottom, width, height]
# rect_histx = [left, bottom + height + spacing, width, 0.2]
# rect_histy = [left + width + spacing, bottom, 0.2, height]

# # start with a square Figure
# fig = plt.figure(figsize=(8, 8))

# ax = fig.add_axes(rect_scatter)
# ax_histx = fig.add_axes(rect_histx, sharex=ax)
# ax_histy = fig.add_axes(rect_histy, sharey=ax)

# # use the previously defined function
# scatter_hist(x, y, ax, ax_histx, ax_histy)

# plt.show()


##################### SIMPLE PLOT ##############################
# Data for plotting
# var = excel.df.Pulse
# time = excel.df.Date

# fig, ax = plt.subplots()

# ax.plot(time, var, 'y')

# ax.set(xlabel='Date', ylabel='Pulse',
#        title='Pulse')
# ax.grid()

# plt.show()


##################### THIRD PLOT ##############################
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime as dt

# Make a series of events 1 day apart
x = mpl.dates.drange(dt.datetime(2009,10,1), 
                     dt.datetime(2010,1,15), 
                     dt.timedelta(days=1))
# Vary the datetimes so that they occur at random times
# Remember, 1.0 is equivalent to 1 day in this case...
x += np.random.random(x.size)

# We can extract the time by using a modulo 1, and adding an arbitrary base date
times = x % 1 + int(x[0]) # (The int is so the y-axis starts at midnight...)

# I'm just plotting points here, but you could just as easily use a bar.
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot_date(x, times, 'ro')
ax.yaxis_date()
fig.autofmt_xdate()

plt.show()

