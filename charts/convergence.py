import plotly.graph_objects as go
import numpy as np


def plot_convergence_chart(on_time_array):
    arr = np.asarray(on_time_array, dtype=float)
    cumulative = np.cumsum(arr) / (np.arange(len(arr)) + 1) * 100
    x = np.arange(1, len(arr) + 1)
    final_value = float(cumulative[-1])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x, y=cumulative,
        mode="lines",
        line=dict(color="#4f46e5", width=2),
        name="On-Time Probability",
        hovertemplate="After %{x:,} simulations<br>On-Time: %{y:.1f}%<extra></extra>",
    ))

    fig.add_hline(
        y=final_value,
        line_dash="dash", line_color="#ef4444", line_width=1.5,
        annotation_text=f"  Converged at {final_value:.1f}%",
        annotation_font_color="#ef4444", annotation_font_size=12,
    )

    fig.update_layout(
        title=dict(
            text="Monte Carlo Convergence — Probability Stabilises Over Simulations",
            font=dict(size=15, color="#0f172a"),
        ),
        xaxis_title="Number of Simulations Run",
        yaxis_title="On-Time Probability (%)",
        yaxis=dict(range=[0, 100]),
        plot_bgcolor="#fafafa",
        paper_bgcolor="#ffffff",
        showlegend=False,
        height=420,
    )
    return fig
