import plotly.graph_objects as go
import numpy as np


def plot_duration_histogram(days_array, deadline):
    on_time = days_array[days_array <= deadline]
    late    = days_array[days_array > deadline]

    fig = go.Figure()
    if len(on_time):
        fig.add_trace(go.Histogram(
            x=on_time, nbinsx=50,
            marker_color="#4f46e5", opacity=0.85,
            name=f"On Time ({len(on_time):,})",
            hovertemplate="Duration: %{x} days<br>Count: %{y}<extra></extra>",
        ))
    if len(late):
        fig.add_trace(go.Histogram(
            x=late, nbinsx=50,
            marker_color="#ef4444", opacity=0.85,
            name=f"Late ({len(late):,})",
            hovertemplate="Duration: %{x} days<br>Count: %{y}<extra></extra>",
        ))

    fig.update_layout(barmode="overlay")

    fig.add_vline(
        x=deadline,
        line_dash="dash", line_color="#ef4444", line_width=2.5,
        annotation_text=f"  Deadline ({deadline}d)",
        annotation_font_color="#ef4444", annotation_font_size=13,
    )

    p50 = float(np.median(days_array))
    fig.add_vline(
        x=p50,
        line_dash="dot", line_color="#16a34a", line_width=2,
        annotation_text=f"  Median ({int(p50)}d)",
        annotation_font_color="#16a34a", annotation_font_size=13,
        annotation_position="top left",
    )

    on_time_pct = (days_array <= deadline).mean() * 100
    fig.update_layout(
        title=dict(
            text=f"Project Duration Distribution  —  {on_time_pct:.1f}% finish on time",
            font=dict(size=15, color="#0f172a"),
        ),
        xaxis_title="Duration (days)",
        yaxis_title="Number of Simulations",
        plot_bgcolor="#fafafa",
        paper_bgcolor="#ffffff",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        bargap=0.02,
        height=420,
    )
    return fig


def plot_cost_histogram(cost_array, budget):
    under  = cost_array[cost_array <= budget]
    over   = cost_array[cost_array > budget]

    fig = go.Figure()
    if len(under):
        fig.add_trace(go.Histogram(
            x=under, nbinsx=50,
            marker_color="#4f46e5", opacity=0.85,
            name=f"Under Budget ({len(under):,})",
            hovertemplate="Cost: $%{x:,.0f}<br>Count: %{y}<extra></extra>",
        ))
    if len(over):
        fig.add_trace(go.Histogram(
            x=over, nbinsx=50,
            marker_color="#ef4444", opacity=0.85,
            name=f"Over Budget ({len(over):,})",
            hovertemplate="Cost: $%{x:,.0f}<br>Count: %{y}<extra></extra>",
        ))

    fig.update_layout(barmode="overlay")

    fig.add_vline(
        x=budget,
        line_dash="dash", line_color="#ef4444", line_width=2.5,
        annotation_text=f"  Budget (${budget:,})",
        annotation_font_color="#ef4444", annotation_font_size=13,
    )

    p50 = float(np.median(cost_array))
    fig.add_vline(
        x=p50,
        line_dash="dot", line_color="#16a34a", line_width=2,
        annotation_text=f"  Median (${int(p50):,})",
        annotation_font_color="#16a34a", annotation_font_size=13,
        annotation_position="top left",
    )

    on_budget_pct = (cost_array <= budget).mean() * 100
    fig.update_layout(
        title=dict(
            text=f"Project Cost Distribution  —  {on_budget_pct:.1f}% stay on budget",
            font=dict(size=15, color="#0f172a"),
        ),
        xaxis_title="Total Cost ($)",
        yaxis_title="Number of Simulations",
        xaxis_tickprefix="$", xaxis_tickformat=",",
        plot_bgcolor="#fafafa",
        paper_bgcolor="#ffffff",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        bargap=0.02,
        height=420,
    )
    return fig
