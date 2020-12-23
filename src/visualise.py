
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.palettes import plasma
from bokeh.plotting import figure
from bokeh.transform import transform

def visualise(tweet_df):
    x = tweet_df['x_coord'].values
    y = tweet_df['y_coord'].values
    desc = tweet_df['tweet_text'].values

    source = ColumnDataSource(data=dict(x=x, y=y, desc=desc))
    hover = HoverTool(tooltips=[
        ("index", "$index"),
        ("(x,y)", "(@x, @y)"),
        ('desc', '@desc'),
    ])
    mapper = LinearColorMapper(palette=plasma(256), low=min(y), high=max(y))

    p = figure(plot_width=1000, plot_height=1000, tools=[hover], title="Scatter Plot")
    p.circle('x', 'y', size=10, source=source,
            fill_color=transform('y', mapper))

    output_file('plot.html')
    show(p)