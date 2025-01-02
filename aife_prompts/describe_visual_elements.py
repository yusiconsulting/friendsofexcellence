describe_visual_elements = """Describe the visual elements of this page by addressing the following questions and tasks:

1. What chart elements, tables, matrices and/or other specialised layouts are shown? Describe each visual element you observed, including:
   - Statistical and comparative: bar charts, line charts, pie charts, scatter plots, area charts, heat maps, box plots, histograms, bubble charts, radar charts, funnel charts, etc.
   - Relationship and flow: tree graphs, network graphs, Venn diagrams, tree maps, Sankey diagrams, chord diagrams, force-directed graphs, etc.
   - Temporal and spatial: time series plots, Gantt charts, candlestick charts, geographic thematic maps, flow maps, etc.
   - Tables, matrices and other visualisations of data and/or logic.

2. For each chart element, convey all the knowledge you obtained from it:
   - For those with labelled data, present each piece of data and its significance with linear narratives.
   - For those without labelled data, state the conclusions you obtained.

3. For each table or matrix, endeavour to extract all cell contents in all rows and columns, preserving their precise original appearance. Avoid omitting any information or data from any cell.

4. For any text with specialised layouts, endeavour to present all words and characters in human reading order, excluding references, notes, page numbers, headers and footers.

Output in Markdown format using the same language as shown in the image."""