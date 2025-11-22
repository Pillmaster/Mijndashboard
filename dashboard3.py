import streamlit as st

# --- 1. Dashboard Configuration ---
st.set_page_config(
    page_title="Overview of My Applications",
    layout="wide", 
    page_icon="🔗"
)

# --- 2. Application Definitions (INCLUDING CATEGORY) ---
FINANCIAL_EMOJIS = ["📈", "💰", "💱", "🪙"] 

apps_data = [
    # Category: THE WEATHER
    {"naam": "☀️ Regional Weather Dashboard", "url": "https://regioweer.streamlit.app/", "beschrijving": "Current and historical temperature comparison in the Region.", "categorie": "The Weather"},
    {"naam": "❄️ Malmån Meteo", "url": "https://malman-meteo.streamlit.app/", "beschrijving": "The weather stations in Malmån.", "categorie": "The Weather"},
    {"naam": "🌡️ Malmån Klimaat", "url": "https://klimaat.streamlit.app/", "beschrijving": "The climate data for Malmån.", "categorie": "The Weather"},
    {"naam": "🏆 Historische Sneeuwrecords", "url": "https://sneeuwdata.streamlit.app/", "beschrijving": "Analyse van historische sneeuwdiepte records (Top 10 hoogste, vroegste/laatste start/einde) voor Malmån.", "categorie": "The Weather"},
    {"naam": "🌧️ Graninge Weather Station", "url": "https://weerdata-analyse-app.streamlit.app/", "beschrijving": "The weather station in Graningen.", "categorie": "The Weather"},
    
    # Category: FINANCIAL
    {"naam": f"{FINANCIAL_EMOJIS[0]} Private Sweden Withdrawal Simulator", "url": "https://withdrawal-strategy-with-capital-gains-tax-sweden.streamlit.app/", "beschrijving": "Analysis of various withdrawal strategies for a private person in Sweden.", "categorie": "Financial"},
    {"naam": f"{FINANCIAL_EMOJIS[1]} Montecarlo Private Sweden Withdrawal Simulator", "url": "https://montecarlosimulatiemetzweedsekapitaalbelasting.streamlit.app/", "beschrijving": "Montecarlo analysis of various withdrawal strategies for a private person in Sweden.", "categorie": "Financial"},
    {"naam": f"{FINANCIAL_EMOJIS[2]} DGA Withdrawal Simulator", "url": "https://dgawithdrawalsimulator-031125.streamlit.app/", "beschrijving": "Analysis of various withdrawal strategies for DGA (Director-Major Shareholder).", "categorie": "Financial"},
    {"naam": f"{FINANCIAL_EMOJIS[3]} Montecarlo DGA Withdrawal Simulator", "url": "https://dga-montecarlo.streamlit.app/", "beschrijving": "Montecarlo analysis of various withdrawal strategies for DGA (Director-Major Shareholder).", "categorie": "Financial"},
    
    # Category: OTHER 
    
]

# Group applications by category
gegroepeerde_apps = {}
for app in apps_data:
    categorie = app['categorie']
    if categorie not in gegroepeerde_apps:
        gegroepeerde_apps[categorie] = []
    gegroepeerde_apps[categorie].append(app)

# Definition of categories and their corresponding emojis (English)
CATEGORIEËN = {
    "Financial": "💰 Financial",
    "The Weather": "🌡️ The Weather",
    "Other": "🛠️ Other",
}

# --- 3. Main Layout: Create a Centered Area ---
col_spacer_left, col_content, col_spacer_right = st.columns([1, 12, 1])

with col_content:
    # 3.1. Title and Introduction (Centered)
    st.title("🔗 My Streamlit Applications Overview")
    st.write("Welcome to the central overview of all my tools and dashboards. Click the title of a block to open the application.")
    st.divider()

    # 3.2. The Three Vertical Columns for the Categories
    col_financial, col_weather, col_other = st.columns(3)

    # Mapping of category key to the Streamlit column object
    kolom_mapping = {
        "Financial": col_financial,
        "The Weather": col_weather, 
        "Other": col_other,
    }

    # --- 4. Rendering per Category in the Columns ---
    for categorie_sleutel, categorie_titel_emoji in CATEGORIEËN.items():
        
        if categorie_sleutel in kolom_mapping:
            
            target_column = kolom_mapping[categorie_sleutel]
            apps_in_categorie = gegroepeerde_apps.get(categorie_sleutel, [])
            
            with target_column:
                # Display the heading as a subheader in the column
                st.subheader(f"{categorie_titel_emoji}")
                
                if not apps_in_categorie:
                    st.markdown("<p style='font-size: 14px; color: #aaaaaa; opacity: 0.7;'>No apps currently available in this category.</p>", unsafe_allow_html=True)


                for app in apps_in_categorie:
                    # Render the block for the app using the traditional styling
                    st.markdown(
                        f"""
                        <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                            <div style="
                                border: 2px solid #30353c;
                                border-radius: 8px;
                                padding: 10px;        
                                margin-bottom: 10px;  
                                height: 100px; 
                                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1); 
                                overflow: hidden;
                            ">
                                <h4 style="margin-top: 0; color: #1e88e5; font-size: 18px; line-height: 1.3;">{app['naam']}</h4>
                                <p style="font-size: 13px; color: #cccccc; opacity: 1.0; margin-bottom: 0; line-height: 1.2;">{app['beschrijving']}</p>
                            </div>
                        </a>
                        """,
                        unsafe_allow_html=True
                    )
    
    # The infobox at the bottom of the centered section
    st.markdown("<br><br>", unsafe_allow_html=True) 
    st.divider()
    st.info("Note: Links open in a new tab to preserve the central navigation page.")
