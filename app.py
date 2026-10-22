import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="LLM Prompt Injection Detector",
    layout="wide"
)


# 2. Core Scanning Logic
def check_prompt(prompt):

    if not prompt.strip():
        return (
            "⚠️ Empty Input",
            "Please type something to test the detector."
        )

    jailbreak_keywords = [
        "ignore instructions",
        "ignore previous",
        "system prompt",
        "developer mode",
        "dan mode",
        "you are now",
        "act as"
    ]

    found_keywords = [
        word
        for word in jailbreak_keywords
        if word in prompt.lower()
    ]

    if found_keywords:

        return (
            "RISK DETECTED [HIGH RISK]",
            f"Prompt blocked! The system detected malicious keywords "
            f"trying to hijack the LLM: {', '.join(found_keywords)}"
        )

    else:

        return (
            "SAFE [VERIFIED]",
            "This prompt is safe and clean. "
            "It is safe to pass this input to the primary LLM model."
        )


# 3. Neon Cyber CSS
dynamic_neon_css = """
<style>

/* ========================================= */
/* MAIN BACKGROUND */
/* ========================================= */

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"] {

    background-color: #000000 !important;

    background:
        radial-gradient(
            circle at 50% -20%,
            rgba(127, 0, 255, 0.28) 0%,
            rgba(255, 0, 127, 0.15) 40%,
            transparent 80%
        ),
        radial-gradient(
            rgba(255, 255, 255, 0.15) 1px,
            transparent 1px
        ),
        radial-gradient(
            rgba(255, 255, 255, 0.1) 1px,
            transparent 1px
        ) !important;

    background-size:
        100% 100%,
        40px 40px,
        90px 90px !important;

    background-position:
        0 0,
        0 0,
        20px 20px !important;

    background-attachment: fixed !important;

    color: #ffffff !important;
}


/* ========================================= */
/* TITLE */
/* ========================================= */

.cyber-title {

    background:
        linear-gradient(
            90deg,
            #ff007f,
            #7f00ff,
            #ff007f
        );

    background-size: 200% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: textShine 3s linear infinite;

    font-weight: 800 !important;

    text-align: center;

    font-size: 3em !important;

    letter-spacing: 1.5px;

    filter:
        drop-shadow(
            0 4px 20px rgba(127, 0, 255, 0.6)
        );

    margin-bottom: 2px !important;
}


.cyber-sub-text {

    background:
        linear-gradient(
            90deg,
            #7f00ff,
            #ff007f,
            #7f00ff
        );

    background-size: 200% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: textShine 4s linear infinite;

    text-align: center;

    font-size: 1.15em !important;

    font-weight: 600 !important;

    filter:
        drop-shadow(
            0 2px 10px rgba(255, 0, 127, 0.3)
        );

    margin-top: 5px !important;

    margin-bottom: 25px !important;
}


@keyframes textShine {

    to {
        background-position: 200% center;
    }

}


/* ========================================= */
/* MOVING NEON PROMPT BOX */
/* ========================================= */

div[data-testid="stTextArea"]:has(
    textarea[placeholder="Type your malicious or safe prompt here..."]
) {

    position: relative !important;

    padding: 3px !important;

    border-radius: 16px !important;

    overflow: hidden !important;

    background:
        conic-gradient(
            from 0deg,
            #7f00ff,
            #7f00ff 30%,
            #ff007f 45%,
            #ff007f 55%,
            #7f00ff 70%,
            #7f00ff
        ) !important;

    animation:
        rotatingNeon 2.5s linear infinite !important;

    box-shadow:
        0 0 15px rgba(127, 0, 255, 0.45),
        0 0 30px rgba(255, 0, 127, 0.20) !important;
}


/* Actual input area */

div[data-testid="stTextArea"]:has(
    textarea[placeholder="Type your malicious or safe prompt here..."]
) textarea {

    background-color: #0c0816 !important;

    color: #ffffff !important;

    border: none !important;

    outline: none !important;

    border-radius: 13px !important;

    box-shadow:
        inset 0 0 20px rgba(127, 0, 255, 0.12) !important;

}


/* Moving border */

@keyframes rotatingNeon {

    0% {

        background:
            conic-gradient(
                from 0deg,
                #ff007f,
                #7f00ff 20%,
                #7f00ff 70%,
                #ff007f
            );

    }

    25% {

        background:
            conic-gradient(
                from 90deg,
                #ff007f,
                #7f00ff 20%,
                #7f00ff 70%,
                #ff007f
            );

    }

    50% {

        background:
            conic-gradient(
                from 180deg,
                #ff007f,
                #7f00ff 20%,
                #7f00ff 70%,
                #ff007f
            );

    }

    75% {

        background:
            conic-gradient(
                from 270deg,
                #ff007f,
                #7f00ff 20%,
                #7f00ff 70%,
                #ff007f
            );

    }

    100% {

        background:
            conic-gradient(
                from 360deg,
                #ff007f,
                #7f00ff 20%,
                #7f00ff 70%,
                #ff007f
            );

    }

}


/* ========================================= */
/* OTHER INPUT FIELDS */
/* ========================================= */

textarea,
input[type="text"] {

    color: #ffffff !important;

    background-color:
        rgba(12, 8, 22, 0.95) !important;

    border-radius: 12px !important;

}


/* ========================================= */
/* SCAN BUTTON */
/* ========================================= */

div.stButton > button {

    background: #0d091a !important;

    border:
        2px solid #ff007
