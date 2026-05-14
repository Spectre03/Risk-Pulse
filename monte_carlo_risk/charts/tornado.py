import plotly.graph_objects as go


def plot_tornado_chart(sensitivity_impacts: dict):
    if not sensitivity_impacts:
        fig = go.Figure()
        fig.update_layout(title="No sensitivity data available.", height=420)
        return fig

    labels = list(sensitivity_impacts.keys())
    values = [max(v, 0) for v in sensitivity_impacts.values()]

    colors = [
        "#ef4444" if v > 5 else ("#f59e0b" if v > 2 else "#16a34a")
        for v in values
    ]

    max_val = max(values) if max(values) > 0 else 1

    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation="h",
        marker_color=colors,
        text=[f"+{v:.1f}d" for v in values],
        textposition="outside",
        hovertemplate="%{y}<br>Impact: +%{x:.1f} days<extra></extra>",
    ))

    fig.update_layout(
        title=dict(
            text="Sensitivity Analysis — What Causes the Most Delay?",
            font=dict(size=15, color="#0f172a"),
        ),
        xaxis=dict(
            title="Additional Days When Factor Is 30% Worse",
            range=[0, max_val * 1.25],
        ),
        yaxis=dict(autorange="reversed"),
        plot_bgcolor="#fafafa",
        paper_bgcolor="#ffffff",
        height=420,
        margin=dict(l=10, r=90, t=60, b=40),
    )
    return fig
