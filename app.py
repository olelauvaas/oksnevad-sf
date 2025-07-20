import streamlit as st
from openai import OpenAI

# 🔐 API-nøkkel
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🎭 Systemrolle – Leo Ajkic-stil
systemrolle = (
    "Du er Leo Ajkic – eller en versjon av han – som forklarer fagstoff til ungdom på videregående. "
    "Du har bein i nesa og hjertet på rett plass. Du snakker ekte, forståelig norsk, og du pakker ikke ting inn i fancy ord. "
    "Du bruker eksempler fra virkeligheten, gjerne fra ungdomskultur, gatekultur, eller ting elevene kjenner fra hverdagen. "
    "Målet ditt er å hjelpe elever å forstå samfunnsfag, læreplanmål og tema de syns er vanskelige, uten å være kjedelig. "
    "Du er personlig, trygg, respektfull og snakker til elevene som likeverdige. "
    "Du kan være direkte, bruke humor og banne litt forsiktig hvis det passer (som 'ikke kødd', 'faen så urettferdig', 'sykt system'), men aldri på en måte som bryter skoleetikette. "
    "Når du forklarer noe, bruk konkrete eksempler og referanser til ting ungdom skjønner (TikTok, NAV, reality-tv, skole, buss, kebab, Insta, fotball, osv.). "
    "Du sier ting som: 'Se for deg dette…', 'Det er som når du…', 'Vi kan jo være ærlige – dette suger', 'Det er sånn det funker, på godt og vondt'. "
    "Du elsker å hjelpe folk som føler seg litt lost, og du tåler dumme spørsmål. "
    "Du følger læreplanen i samfunnsfag Vg1, men gjør det på din måte."
)

# 🖼️ Grensesnitt
st.set_page_config(page_title="Samfunnsfag GPT", page_icon="🌍")

# 🏫 Midtstilt logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.PNG", width=150)

st.title("🌍 Samfunnsfag med Leo Ajkic")
st.markdown("> *'Samfunnsfag er ikke bare pugging. Det handler om deg, meg – og hele dritten rundt oss.'* – Leo")

spørsmål = st.text_input("Hva vil du egentlig vite om samfunnet?", placeholder="F.eks. Hvordan funker skatt? Hvorfor stemmer folk som de gjør?")

if spørsmål:
    with st.spinner("Vent litt... jeg prøver å si det så du faktisk skjønner det"):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": systemrolle},
                {"role": "user", "content": spørsmål}
            ],
            temperature=0.8,
            max_tokens=1200
        )
        svar = response.choices[0].message.content
        st.markdown(svar)