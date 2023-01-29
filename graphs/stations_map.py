import plotly.graph_objs as go


def create_stations_map(stations, mapbox_access_token, station_select=None):

    # if station_select is not None:
    slct_idx = stations.index.get_loc(station_select)
    # clat = stations.loc[station_select].lat
    # clon = stations.loc[station_select].lon
    # zm = 6
    # else:
    clat = 0
    clon = 190
    zm = 2.4
    # slct_idx = None

    lats = stations.lat.tolist()
    lons = stations.lon.tolist()

    m = go.Figure(
        [
            # go.Scattermapbox(
            #     lat=lats,
            #     lon=lons,
            #     mode="markers",
            #     marker=dict(color="#fff", size=15),
            #     opacity=0.8,
            #     hoverinfo="none",
            #     text=stations.name.to_list(),
            # ),
            # go.Scattermapbox(
            #     lat=[lats[slct_idx]],
            #     lon=[lons[slct_idx]],
            #     mode="markers",
            #     marker=dict(color="#fff", size=22),
            #     opacity=0.8,
            #     hoverinfo="none",
            #     text=stations.name.to_list(),
            # ),
            go.Scattermapbox(
                lat=lats,
                lon=lons,
                mode="markers",
                marker=dict(color="#69BCEC", size=12),
                opacity=0.8,
                line=dict(width=2),
                selectedpoints=[slct_idx],
                selected=dict(marker=dict(color="#E69F00", size=18)),
                customdata=[
                    dict(id=s, name=stations.name.loc[s]) for s in stations.index
                ],
                hovertemplate="%{text}<extra></extra>",
                text=stations.name.to_list(),
            ),
        ]
    )

    m.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=0, b=0, pad=0),
        modebar=dict(
            remove=["pan", "toImage", "lasso", "select"],
            orientation="v",
            color="#333333",
            bgcolor=None,
        ),
        clickmode="event+select",
        hovermode="closest",
        showlegend=False,
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(lat=clat, lon=clon),
            pitch=0,
            zoom=zm,
            # style="mapbox://styles/mapbox/light-v10",
            style="satellite",
        ),
    )

    return m
