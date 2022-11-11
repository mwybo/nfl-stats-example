import pandas as pd
import os
import nfl_data_py as nfl
import urllib


logos = nfl.import_team_desc()
logos = logos[['team_abbr', 'team_logo_espn']]

logo_paths = []
team_abbr = []
if not os.path.exists('logos'):
    os.makedirs('logos')

for team in range(len(logos)):
    fname = 'logos/{}.png'.format(logos['team_abbr'][team])
    urllib.request.urlretrieve(logos['team_logo_espn'][team], fname)
    logo_paths.append(fname)
    team_abbr.append(logos['team_abbr'][team])

logo_df = pd.DataFrame({'Team Abbr': team_abbr, 'Logo Path': logo_paths})
logo_df.to_csv('logos/logo_df.csv', index=False)
