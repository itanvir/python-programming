import plotly

fig = {
    "data": [{"x": [1, 2, 3], "y": [2, 5, 3], "type": "bar"}],
    "layout": {"width": 450, "height": 350, 'margin': {'l': 50, 'r': 50, 't': 50, 'b': 50}}
}

graph_1 = plotly.offline.plot(
    fig,
    config={"displayModeBar": False},
    show_link=False,
    include_plotlyjs=False,
    output_type="div",
)

graph_2 = plotly.offline.plot(
    fig,
    config={"displayModeBar": False},
    show_link=False,
    include_plotlyjs=False,
    output_type="div",
)

html_string = (
    """
<!DOCTYPE html>
<html lang="en">
<body style="background-color:#fafbfe;">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <style>
    /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
    .row.content {height: 550px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      background-color: #fafbfe;
      height: 100%;
    }
        
    /* On small screens, set height to 'auto' for the grid */
    @media screen and (max-width: 767px) {
      .row.content {height: auto;} 
    }

    /* Set white background color for the cards */
    .well {
    background-color: white;
    }

    /* Nav colors */
    .nav-pills>li.active>a, .nav-pills>li.active>a:focus, .nav-pills>li.active>a:hover {
    background-color: #636EFA;
    }

    .nav>li>a {
    color: #636EFA;
    }

  </style>
</head>
<body>

<nav class="navbar navbar-inverse visible-xs">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#">Logo</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Dashboard</a></li>
        <li><a href="#">Age</a></li>
        <li><a href="#">Gender</a></li>
        <li><a href="#">Geo</a></li>
      </ul>
    </div>
  </div>
</nav>

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-2 sidenav hidden-xs">
      <h2>Logo</h2>
      <ul class="nav nav-pills nav-stacked">
        <li class="active"><a href="#section1">Dashboard</a></li>
        <li><a href="#section2">Age</a></li>
        <li><a href="#section3">Gender</a></li>
        <li><a href="#section3">Geo</a></li>
      </ul><br>
    </div>
    <br>
    
    <div class="col-sm-10">
      <div class="well">
        <h2 style="color:#636EFA">Dashboard</h2>
        <p>Some text..</p>
      </div>
      <div class="row">
<div class="col-sm-6">
          <div class="well">
            <h4>Pages</h4>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            """ + graph_1 + """
          </div>
        </div>
        <div class="col-sm-6">
          <div class="well">
            <h4>Pages</h4>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            """ + graph_2 + """
          </div>
        </div>
        <div class="col-sm-6">
          <div class="well">
            <h4>Sessions</h4>
            <p>10 Million</p> 
          </div>
        </div>
        <div class="col-sm-6">
          <div class="well">
            <h4>Bounce</h4>
            <p>30%</p> 
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-4">
          <div class="well">
            <p>Text</p> 
            <p>Text</p> 
            <p>Text</p> 
          </div>
        </div>
        <div class="col-sm-4">
          <div class="well">
            <p>Text</p> 
            <p>Text</p> 
            <p>Text</p> 
          </div>
        </div>
        <div class="col-sm-4">
          <div class="well">
            <p>Text</p> 
            <p>Text</p> 
            <p>Text</p> 
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-8">
          <div class="well">
            <p>Text</p> 
          </div>
        </div>
        <div class="col-sm-4">
          <div class="well">
            <p>Text</p> 
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""
)

with open("index.html", "w") as f:
    f.write(html_string)