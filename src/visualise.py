
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.palettes import plasma
from bokeh.plotting import figure
from bokeh.transform import transform

def visualise(points):
    x = points[:,0]
    y = points[:,1]
    desc = [str(i) for i in y]

    source = ColumnDataSource(data=dict(x=x, y=y, desc=desc))
    hover = HoverTool(tooltips=[
        ("index", "$index"),
        ("(x,y)", "(@x, @y)"),
        ('desc', '@desc'),
    ])
    mapper = LinearColorMapper(palette=plasma(256), low=min(y), high=max(y))

    p = figure(plot_width=400, plot_height=400, tools=[hover], title="Scatter Plot")
    p.circle('x', 'y', size=10, source=source,
            fill_color=transform('y', mapper))

    output_file('plot.html')
    show(p)