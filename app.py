#pip install deep-translate
import deepl
import streamlit as st

LANGUAGE = {"英語": "EN", "日本語":"JA"}

def deepl_translate(text, src_lang="JA", target_lang="EN"):
    translate_text = deepl.translate(
        source_language = src_lang, target_language= target_lang, text=text
    )
    print(translate_text)
    return translate_text

def main():
    st.title("Deepl by Streamlit")
    main_container = st.container()
    left_col, right_col = main_container.columns(2)
    #left area contents
    src_lang = left_col.selectbox(
        "入力テキストの言語",
        options=LANGUAGE
    )
    print(src_lang)
    input_text = left_col.text_area("テキストを入力して下さい。", height=500)
    # right area contents
    target_lang = right_col.selectbox(

        "翻訳後のテキスト言語",
        options=LANGUAGE
    )
    right_col.text_area(
        "翻訳後のtext",
        value=deepl_translate(
            input_text, src_lang=LANGUAGE[src_lang], target_lang=LANGUAGE[target_lang]
        ),
        height=500
    )

if __name__ =='__main__':
    main()