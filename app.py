"""
This file is part of the flask+d3 Hello World project.
"""
import json
import flask
import numpy as np
import pydot


app = flask.Flask(__name__)


@app.route("/")
def index():
    """
    When you request the root path, you'll get the index.html template.

    """

    graph = pydot.graph_from_dot_file("dot.dot")
    d3_graph_source =""

    dot_content = graph.to_string().strip()
    '''
    for d in dot_content.split("\n"):
        print d
        #raw_input()
        '''
    print "loaded"
    #d3_graph_source = "\\n\t".join(dot_content.split("\n"))
    d3_graph_source = dot_content.replace("\n","").replace(";","")
    print [d3_graph_source]
    #d3_graph_source= 'digraph{ a }'
    #return flask.render_template("index.html")
    return flask.render_template("second.html", graph=d3_graph_source)
    #return flask.render_template("0.html", graph=d3_graph_source)


@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])


if __name__ == "__main__":
    import os

    host = "0.0.0.0"
    port = 8000

    # Open a web browser pointing at the app.
    #os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port,host=host)
