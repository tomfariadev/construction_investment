### Construction Investment Dashboard (Japan)
Interactive data dashboard built with Python, Pandas, Plotly and Streamlit to analyze construction investment trends in Japan.

## Objective
Understand how construction investment evolved over time and how resources are distributed between sectors, construction types, and public vs private participation.

## Key Insights Provided
This dashboard answers:
- Is the construction sector growing or shrinking?
- Who invests more: Government or Private sector?
- Is investment focused on residential or non-residential construction?
- Is the industrial sector (mining & industry) expanding?
- Is the country building new infrastructure or focusing on renovations?

## Metrics
# 1 - Total sales investment by year
- Total construction investment for selected year
# 2 - Growth X last year
- Mostra se o setor está aquecido ou em crise
- Economic trend indicator
# 3-  % Architecture 
- Share of investment in buildings
# 4 - % Civil Engineering
- Share of infrastructure investment

## Graphics
# 1- Government X Private Investment Over Time
- Sector participation over time
- Mostra total + participação ao mesmo tempo
- Permite ver a mudança de dependência ao longo dos anos

# 2- Residential X Non-Residential Construction
- Housing vs economic infrastructure
- Casas e apartamentos vs prédios comerciais/indústria
 
# 3- Private Investment in Mining & Industry Over Time
- Industrial sector strength
- Mostra força industrial.

# 4- Renovation vs New Construction Over Time
- Market behavior (expansion vs maintenance)
- Compara reforma vs construção nova, indica se o mercado está construindo novo ou reformando.

## Run Locally
pip install -r requirements.txt
streamlit run main.py