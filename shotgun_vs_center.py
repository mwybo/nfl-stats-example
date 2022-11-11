import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
import nfl_data_py as nfl

# Load data and slice to get only catches
pbp_df = nfl.import_pbp_data([2022])
shotgun_center_df = pbp_df[['posteam', 'yards_gained', 'shotgun', 'play_type']]
# get only passes, group the df by team and shotgun, and calculate the mean within those groups
shotgun_center_df = shotgun_center_df.loc[shotgun_center_df['play_type'] == 'pass'].groupby(['posteam', 'shotgun']).mean()

# now go through that df and get those means into an easier plotting format
dfs = []
for team in shotgun_center_df.index.get_level_values(0).unique():
    print(team)
    dfs.append(pd.DataFrame({
        'posteam': team,
        'Yards/Catch Under Center': shotgun_center_df.loc[(team, 0)].values,
        'Yards/Catch in Shotgun': shotgun_center_df.loc[(team, 1)].values
    }))
mean_df = pd.concat(dfs)

# load up your logos
logo_df = pd.read_csv('logos/logo_df.csv').set_index('Team Abbr')

#helper function to make the code below a little cleaner
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=.05, alpha=1)


# work in base matplotlib because its easier to work with images directly on the ax and have a bit more control
fig, ax = plt.subplots()
ax.set_title('X and Y Axis Equal')
ax.plot(mean_df['Yards/Catch Under Center'], mean_df['Yards/Catch in Shotgun'], '.')
for index, row in mean_df.iterrows():
    ab = AnnotationBbox(getImage(logo_df.loc[row['posteam'], 'Logo Path']),
                        (row['Yards/Catch Under Center'], row['Yards/Catch in Shotgun']), frameon=False)
    ax.add_artist(ab)
ax.set_xlim(0,12)
ax.set_ylim(0,12)
ax.plot([0, 12], [0, 12], 'k--')
ax.set_xlabel('Yards/Catch Under Center')
ax.set_ylabel('Yards/Catch in Shotgun')
ax.grid()

# do it again, with uneven axes, but still include the 45 line to give context
fig, ax = plt.subplots()
ax.set_title('Auto Scale Both X and Y Axis')
ax.plot(mean_df['Yards/Catch Under Center'], mean_df['Yards/Catch in Shotgun'], '.')
for index, row in mean_df.iterrows():
    ab = AnnotationBbox(getImage(logo_df.loc[row['posteam'], 'Logo Path']),
                        (row['Yards/Catch Under Center'], row['Yards/Catch in Shotgun']), frameon=False)
    ax.add_artist(ab)
ax.set_xlim(ax.get_xlim())  # fix axes so my 45 line doesnt mess it up
ax.set_ylim(ax.get_ylim())  # fix axes so my 45 line doesnt mess it up
ax.plot([0, 12], [0, 12], 'k--')
ax.set_xlabel('Yards/Catch Under Center')
ax.set_ylabel('Yards/Catch in Shotgun')
ax.grid()

# not a big fan of that scaling, going to do some pading on the yaxis
fig, ax = plt.subplots()
ax.set_title('Auto Scale X, add some pad to y to make it a bit more intuitive')
ax.plot(mean_df['Yards/Catch Under Center'], mean_df['Yards/Catch in Shotgun'], '.')
for index, row in mean_df.iterrows():
    ab = AnnotationBbox(getImage(logo_df.loc[row['posteam'], 'Logo Path']),
                        (row['Yards/Catch Under Center'], row['Yards/Catch in Shotgun']), frameon=False)
    ax.add_artist(ab)
ax.set_xlim(ax.get_xlim())  # fix axes so my 45 line doesnt mess it up
ax.set_ylim(2, 10)  # fix axes so my 45 line doesnt mess it up
ax.plot([0, 12], [0, 12], 'k--')
ax.set_xlabel('Yards/Catch Under Center')
ax.set_ylabel('Yards/Catch in Shotgun')
ax.grid()