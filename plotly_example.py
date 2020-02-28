import plotly.express as px


# Violin plot example
df = px.data.tips()
fig = px.violin(df, y="tip", x="smoker", color="sex", box=True, points="all", hover_data=df.columns)
fig.show()

with open('example_1.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))


# Scatter plot example
gapminder = px.data.gapminder()

fig = px.scatter(
    gapminder.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    height=400,
    width=650,
)

with open('example_2.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))