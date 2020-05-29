import plotly
import plotly.graph_objs

plotly.offline.plot({
"data": [
       plotly.graph_objs.Bar(x=['food','service','environment'],y=[3.4,4.2,4.3])
]
})