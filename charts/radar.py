import plotly.graph_objects as go


DIMENSION_LABELS = {
    "Technical":      "Technical<br>Complexity",
    "Requirements":   "Requirements<br>Clarity",
    "Integration":    "Integration<br>Complexity",
    "Team Fit":       "Team<br>Fit",
    "Feature Risk":   "Feature<br>Risk",
    "Organizational": "Organizational<br>Complexity",
}

COLOR_MAP = {
    "Low":       "#16a34a",
    "Medium":    "#f59e0b",
    "High":      "#ef4444",
    "Very High": "#7c3aed",
    "Extreme":   "#991b1b",
}

FILL_MAP = {
    "Low":       "rgba(22,163,74,0.18)",
    "Medium":    "rgba(245,158,11,0.18)",
    "High":      "rgba(239,68,68,0.18)",
    "Very High": "rgba(124,58,237,0.18)",
    "Extreme":   "rgba(153,27,27,0.18)",
}


def plot_complexity_radar(dimension_scores: dict, overall: float, label: str):
    dims   = list(dimension_scores.keys())
    values = [round(dimension_scores[d] * 100, 1) for d in dims]

    dims_closed   = dims + [dims[0]]
    values_closed = values + [values[0]]

    color     = COLOR_MAP.get(label, "#4f46e5")
    fillcolor = FILL_MAP.get(label, "rgba(79,70,229,0.18)")

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=[DIMENSION_LABELS.get(d, d) for d in dims_closed],
        fill="toself",
        fillcolor=fillcolor,
        line=dict(color=color, width=2.5),
        name="Complexity Profile",
        hovertemplate="%{theta}<br>Score: %{r:.0f}/100<extra></extra>",
    ))

    ref_vals = [50] * (len(dims) + 1)
    fig.add_trace(go.Scatterpolar(
        r=ref_vals,
        theta=[DIMENSION_LABELS.get(d, d) for d in dims_closed],
        mode="lines",
        line=dict(color="#cbd5e1", width=1, dash="dot"),
        showlegend=False,
        hoverinfo="skip",
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True, range=[0, 100],
                tickvals=[25, 50, 75, 100],
                tickfont=dict(size=10, color="#94a3b8"),
                gridcolor="#e2e8f0",
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color="#374151"),
                gridcolor="#e2e8f0",
            ),
            bgcolor="#f8faff",
        ),
        title=dict(
            text=f"Complexity Profile — Overall: <b>{int(overall*100)}/100</b> ({label})",
            font=dict(size=15, color="#0f172a"),
            x=0.5,
        ),
        showlegend=False,
        paper_bgcolor="#ffffff",
        height=460,
        margin=dict(t=80, b=40, l=80, r=80),
    )
    return fig


def plot_dimension_bars(dimension_scores: dict, drivers: list):
    dims   = list(dimension_scores.keys())
    values = [round(dimension_scores[d] * 100, 1) for d in dims]

    colors = [
        "#ef4444" if d in drivers else ("#f59e0b" if v >= 60 else "#4f46e5")
        for d, v in zip(dims, values)
    ]

    fig = go.Figure(go.Bar(
        x=dims,
        y=values,
        marker_color=colors,
        text=[f"{v:.0f}" for v in values],
        textposition="outside",
        hovertemplate="%{x}<br>Score: %{y:.0f}/100<extra></extra>",
    ))

    fig.add_hline(
        y=50,
        line_dash="dash", line_color="#94a3b8", line_width=1.5,
        annotation_text="50 — medium threshold",
        annotation_font_color="#94a3b8", annotation_font_size=11,
    )

    fig.update_layout(
        title=dict(
            text="Complexity by Dimension  (red = top risk drivers)",
            font=dict(size=15, color="#0f172a"),
        ),
        yaxis=dict(range=[0, 115], title="Score (0–100)"),
        xaxis_title="",
        plot_bgcolor="#fafafa",
        paper_bgcolor="#ffffff",
        showlegend=False,
        height=380,
    )
    return fig
